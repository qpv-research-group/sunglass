# Sunglass

Sunglass is a simple - and not yet fully operational - graphical user interface for the
solar cells and semiconductors modelling framework [Solcore](https://www.solcore.solar/). 

## Using Sunglass

1. Install it from PyPI

```bash
pip install sunglass
```

2. If you want PDD support in Solcore, re-install Solcore with that support:

```bash
pip install --no-deps --force-reinstall --install-option="--with_pdd" solcore
```

3. Run it!

```bash
python -m sunglass
```

## Develop Sunglass

1. Install poetry following the instructions for your OS: https://python-poetry.org/docs/
2. `git clone` this repository.
3. Navigate to thee root folder and install sunglass with `poetry install`
4. If you want PDD support in Solcore, re-install Solcore with that support:

```bash
pip install --no-deps --force-reinstall --install-option="--with_pdd" solcore
```
