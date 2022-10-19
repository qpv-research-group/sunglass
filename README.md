# Sunglass
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/qpv-research-group/sunglass/develop.svg)](https://results.pre-commit.ci/latest/github/qpv-research-group/sunglass/develop)
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

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

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://www.imperial.ac.uk/admin-services/ict/self-service/research-support/rcs/research-software-engineering/"><img src="https://avatars.githubusercontent.com/u/6095790?v=4?s=100" width="100px;" alt="Diego Alonso Álvarez"/><br /><sub><b>Diego Alonso Álvarez</b></sub></a><br /><a href="#infra-dalonsoa" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#ideas-dalonsoa" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-dalonsoa" title="Maintenance">🚧</a> <a href="https://github.com/qpv-research-group/sunglass/commits?author=dalonsoa" title="Code">💻</a> <a href="https://github.com/qpv-research-group/sunglass/issues?q=author%3Adalonsoa" title="Bug reports">🐛</a></td>
      <td align="center"><a href="https://www.qpvgroup.org/phoebe-pearce"><img src="https://avatars.githubusercontent.com/u/25822065?v=4?s=100" width="100px;" alt="Phoebe Pearce"/><br /><sub><b>Phoebe Pearce</b></sub></a><br /><a href="https://github.com/qpv-research-group/sunglass/pulls?q=is%3Apr+reviewed-by%3Aphoebe-p" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/qpv-research-group/sunglass/issues?q=author%3Aphoebe-p" title="Bug reports">🐛</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
