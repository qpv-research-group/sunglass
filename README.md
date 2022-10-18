# Sunglass

Sunglass is a simple - and not yet fully operational - graphical user interface for the
solar cells and semiconductors modelling framework [Solcore](https://www.solcore.solar/).

## Using Sunglass

* Install it from PyPI

```bash
pip install sunglass
```

* If you want PDD support in Solcore, re-install Solcore with that support:

```bash
pip install --no-deps --force-reinstall --install-option="--with_pdd" solcore
```

* Run it!

```bash
python -m sunglass
```

## Develop Sunglass

- Install poetry following the instructions for your OS: <https://python-poetry.org/docs/>.
- Clone this repository with `git clone`.
- Navigate to thee root folder and install sunglass with `poetry install`.
- If you want PDD support in Solcore, re-install Solcore with that support.

```bash
pip install --no-deps --force-reinstall --install-option="--with_pdd" solcore
```
