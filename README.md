# barn-owl

[![Python build & test](https://github.com/swe-students-spring2026/3-package-barn_owl/actions/workflows/build.yaml/badge.svg)](https://github.com/swe-students-spring2026/3-package-barn_owl/actions/workflows/build.yaml)

A fun owl-themed package!

**PyPI page:** [https://pypi.org/project/barn-owl/](https://pypi.org/project/barn-owl/)

---

## Installation

Install the barn_owl module with pip:

```bash
pip install barn-owl
```

---

## Usage

### Owl Latin

```python
from barn_owl import to_owl_latin

print(to_owl_latin("hello world"))
# Prints "ellohoo orldwoo"
```

**`to_owl_latin(text) -> str`**
Returns a string containing the translation of the input into owl latin; that is, appends 'hoo' to words starting with a non-consonant, otherwise, moves leading consonants to the end and appends 'oo'. In both cases, the translation keeps all leading and trailing punctuation as-is.

## Contributing

### Prerequisites

- Python 3.9+
- [pipenv](https://pipenv.pypa.io/)

### Set up the development environment

```bash
git clone https://github.com/swe-students-spring2026/3-package-barn_owl.git
cd 3-package-barn_owl
pipenv install --dev
```

This installs all dependencies and the package itself in editable mode.

### Run tests

```bash
python -m pytest
```

### Build the package

```bash
python -m build
```

### Publish to PyPI (maintainers only)

```bash
twine upload -r testpypi dist/*
```

### Developer workflow

1. Create a feature branch off `main`.
2. Make your changes and add tests.
3. Open a pull request to `main` and ask a teammate to review.
4. After approval and passing CI, merge and delete the feature branch.

---

## Team

- Aaron Hui ([Github](https://github.com/aaronthmetic))
- name
- name
- name
- name
