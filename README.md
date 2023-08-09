# Greek Stemmer

[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]

This is a Python implementation of Skroutz's Ruby Greek stemmer.

### Maintainer's Note

This fork is an attempt to help maintain the repository due to its original author's inactivity. All credit for the original work remains with Andreas Loupasakis.

### Credits

This project was originally developed by Andreas Loupasakis. All credits for the initial work go to him.

- Original repository: [@alup/python_greek_stemmer](https://github.com/alup/python_greek_stemmer)
- Author's Github: [@alup](https://github.com/alup)

## Usage

```python
from greek_stemmer import GreekStemmer
stemmer = GreekStemmer()
stemmer.stem('ΘΑΛΑΣΣΑ')
```

## Installation

To install using pip:

```bash
pip install greek-stemmer-plus
```

## Local Development

### Setting up the local environment

1. Clone the repository.
2. Install Poetry: `curl -sSL https://install.python-poetry.org | python -`
3. Install project dependencies using Poetry: `poetry install`

### Running tests

```bash
poetry run pytest tests/
```

### Proposing Changes

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and commit them using [Angular commit message conventions](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#commit).
4. Submit a pull request to the main repository.

<!-- Badges: -->

[pypi-image]: https://img.shields.io/pypi/v/greek_stemmer_plus
[pypi-url]: https://pypi.org/project/greek_stemmer_plus/
[build-image]: https://github.com/mathspp/greek_stemmer_plus/actions/workflows/build.yaml/badge.svg
[build-url]: https://github.com/mathspp/greek_stemmer_plus/actions/workflows/build.yaml
