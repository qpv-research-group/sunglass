# sunglass

Steps to use Suglass

1. Install poetry following the instructions for your OS: https://python-poetry.org/docs/
2. `git clone` this repository.
3. Navigate to thee root folder and install sunglass with `poetry install`
4. If you want PDD support in Solcore, re-install Solcore with that support:

```bash
pip install --no-deps --force-reinstall --install-option="--with_pdd" solcore
```

5. Run Sunglass with `poetry run python -m sunglass`