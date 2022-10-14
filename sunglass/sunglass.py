import matplotlib

matplotlib.use("TkAgg")

import datetime  # noqa
import sys  # noqa
import tkinter as tk  # noqa
from tkinter import ttk  # noqa

from sunglass.log import LogTab  # noqa
from sunglass.materials import MaterialsTab  # noqa
from sunglass.solar_cells import SolarCellsTab  # noqa
from sunglass.spectrum import SpectrumTab  # noqa


class Sunglass(tk.Tk):
    """This class creates the main Sunglass window.

    This is the function one that will serve as entry point for any other tool
    """

    def __init__(self):
        """Constructor of the class

        :return: None
        """

        tk.Tk.__init__(self)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.title("Sunglass")

        # Used to force a "safe closing" of the program
        self.protocol("WM_DELETE_WINDOW", self.__quit)
        self.option_add("*tearOff", False)  # Prevents tearing the menus

        # We create the global variables
        self.create_global_variables()

        # We create the GUI
        self.create_gui()

        # Finally, we initiate the main loop.
        # This is a hack found here: http://github.com/matplotlib/matplotlib/issues/9637
        # to avoid a crashing that happens when combining certain versions of tcl
        # (what's behind tkinter) and certain versions of python
        while self.closed is False:
            try:
                self.update_idletasks()
                self.update()
            except UnicodeDecodeError:
                print("Caught Scroll Error")

    def __quit(self) -> None:
        """Quit the program in a safe way

        Return:
            None
        """
        self.closed = True

        # Needed to prevent weird errors related with Tcl/Tk. See:
        # https://stackoverflow.com/questions/15448914/python-tkinter-ttk-combobox-throws-exception-on-quit
        self.eval("::ttk::CancelRepeat")

        # And finally closeing the app
        self.destroy()  # destroys the main window
        self.quit()  # quits the program

    def create_global_variables(self):
        """Creates the global variables needed in several places of the program

        :return: None
        """
        self.closed = False

    def create_gui(self) -> None:
        """Creates the graphic components of the program.

        This calls the relevant classes to add their bit (materials, solar cells, etc).

        Return:
            None
        """
        masterframe = ttk.Frame(self)
        masterframe.grid(column=0, row=0, sticky=tk.NSEW)
        masterframe.rowconfigure(0, weight=1)
        masterframe.columnconfigure(0, weight=1)

        self.book = ttk.Notebook(masterframe)
        self.book.grid(column=0, row=0, sticky=tk.NSEW)

        # This needs to be called before the others
        self.materials = MaterialsTab(self.book, self)
        self.solar_cells = SolarCellsTab(self.book, self)
        self.output = LogTab(self.book)
        self.spectrum = SpectrumTab(self.book)

        # self.book.add(self.spectrum, text='Spectrum', sticky=tk.NSEW)
        self.book.add(self.solar_cells, text="Solar Cells", sticky=tk.NSEW)
        # self.book.add(self.materials, text='Materials', sticky=tk.NSEW)
        self.book.add(self.output, text="Log", sticky=tk.NSEW)

        sys.stdout = TextRedirector(self.output.text, "stdout")
        sys.stderr = TextRedirector(self.output.text, "stderr")


class TextRedirector(object):
    """Writes text in a chose widget. Taken from:

    https://stackoverflow.com/questions/12351786/how-to-redirect-print-statements-to-tkinter-text-widget
    """

    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        if str == "\n":
            return
        now = datetime.datetime.now().isoformat(" ") + " "
        self.widget.configure(state="normal")
        self.widget.insert("end", now, (self.tag, "red"))
        self.widget.insert("end", str + "\n", (self.tag))
        self.widget.configure(state="disabled")


if __name__ == "__main__":
    window = Sunglass()
