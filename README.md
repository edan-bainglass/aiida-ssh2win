[![Build Status][ci-badge]][ci-link]
[![Coverage Status][cov-badge]][cov-link]
[![Docs status][docs-badge]][docs-link]
[![PyPI version][pypi-badge]][pypi-link]

# aiida-ssh2win

A transport plugin allowing AiiDA to run calculations on Windows machines.

This plugin is the default output of the
[AiiDA plugin cutter](https://github.com/aiidateam/aiida-plugin-cutter),
intended to help developers get started with their AiiDA plugins.

## Repository contents

- [`.github/`](.github/): [Github Actions](https://github.com/features/actions) configuration
  - [`ci.yml`](.github/workflows/ci.yml): runs tests, checks test coverage and builds documentation at every new commit
  - [`publish-on-pypi.yml`](.github/workflows/publish-on-pypi.yml): automatically deploy git tags to PyPI - just generate a [PyPI API token](https://pypi.org/help/#apitoken) for your PyPI account and add it to the `pypi_token` secret of your github repository
- [`aiida_ssh2win/`](aiida_ssh2win/): The main source code of the plugin package
  - [`transport.py`](aiida_ssh2win/transport.py): Contains `SshToWindowsTransport` - a concrete implementation of AiiDA's `Transport` interface
- [`docs/`](docs/): A documentation template ready for publication on [Read the Docs](http://aiida-ssh2win.readthedocs.io/en/latest/)
- [`tests/`](tests/): Unit testing using the [pytest](https://docs.pytest.org/en/latest/) framework. Install `pip install -e .[testing]` and run `pytest`.
- [`.gitignore`](.gitignore): Telling git which files to ignore
- [`.pre-commit-config.yaml`](.pre-commit-config.yaml): Configuration of [pre-commit hooks](https://pre-commit.com/) that sanitize coding style and check for syntax errors. Enable via `pip install -e .[pre-commit] && pre-commit install`
- [`.readthedocs.yml`](.readthedocs.yml): Configuration of documentation build for [Read the Docs](https://readthedocs.org/)
- [`LICENSE`](LICENSE): License for your plugin
- [`README.md`](README.md): This file
- [`conftest.py`](conftest.py): Configuration of fixtures for [pytest](https://docs.pytest.org/en/latest/)
- [`pyproject.toml`](setup.json): Python package metadata for registration on [PyPI](https://pypi.org/) and the [AiiDA plugin registry](https://aiidateam.github.io/aiida-registry/) (including entry points)

## Installation

```shell
pip install aiida-ssh2win
verdi quicksetup  # better to set up a new profile
verdi plugin list aiida.transports  # should now show the `ssh2win` plugins
```

## Usage

## License

MIT

## Contact

edan.bainglass@gmail.com

[ci-badge]: https://github.com/edan-bainglass/aiida-ssh2win/workflows/ci/badge.svg?branch=master
[ci-link]: https://github.com/edan-bainglass/aiida-ssh2win/actions
[cov-badge]: https://coveralls.io/repos/github/edan-bainglass/aiida-ssh2win/badge.svg?branch=master
[cov-link]: https://coveralls.io/github/edan-bainglass/aiida-ssh2win?branch=master
[docs-badge]: https://readthedocs.org/projects/aiida-ssh2win/badge
[docs-link]: http://aiida-ssh2win.readthedocs.io/
[pypi-badge]: https://badge.fury.io/py/aiida-ssh2win.svg
[pypi-link]: https://badge.fury.io/py/aiida-ssh2win
