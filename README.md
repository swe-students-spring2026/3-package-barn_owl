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

A full runnable demo that calls every public function is in [`examples/demo.py`](examples/demo.py). From the repo root after `pip install barn-owl` or `pipenv install --dev`:

```bash
python -m examples.demo
```

### Owl wisdom

**`owl_wisdom(topic="life") -> str`** returns a random owl-themed quip for a given theme. Pass **`topic`** as one of `"life"` (default), `"coding"`, `"friendship"`, `"nature"`, or `"food"`. Any other value raises `ValueError` with a hint listing valid topics.

```python
from barn_owl import owl_wisdom

print(owl_wisdom())

print(owl_wisdom(topic="coding"))
```

### Owl Latin

**`to_owl_latin(text) -> str`**
returns a string containing the translation of the input into owl latin; that is, appends 'hoo' to words starting with a non-consonant, otherwise, moves leading consonants to the end and appends 'oo'. In both cases, the translation keeps all leading and trailing punctuation as-is.

```python
from barn_owl import to_owl_latin

print(to_owl_latin("hello world"))
# Prints "ellohoo orldwoo"
```

### Owl Drawing

**`owl_drawing(style) -> str`** returns a string representation of an ASCII emoji illustration of an owl based on the chosen style. Choose a style from either "wise", "cute", "spooky", "funny", "large", "duo", or "emoji". Any invalid parameters will raise a ValueError.

```python
from barn_owl import owl_drawing

print(owl_drawing("cute"))
# prints a cute owl drawing from the database
```

### Owl Jokes

**`owl_jokes(category="python") -> str`** returns a random owl-themed joke from the specified category. Choose a category from `"python"` (default), `"programming"`, or `"cold"`. Any other value raises `ValueError` with a hint listing valid categories.

```python
from barn_owl import owl_jokes

print(owl_jokes())                    # defaults to "python"
print(owl_jokes(category="programming"))
# prints a programming-related owl joke
```

### Owl Name Generator

**`owl_name_generator(style="wise") -> str`** returns a randomly generated owl name for the given style. Choose from `"wise"` (default), `"spooky"`, `"cute"`, or `"funny"`. Any other value raises `ValueError` with a hint listing valid styles.

```python
from barn_owl import owl_name_generator

print(owl_name_generator())               # defaults to "wise"
print(owl_name_generator(style="spooky"))
# prints a spooky owl name

```

## Contributing

### Prerequisites

- Python 3.11+
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
pipenv run python -m pytest
```

### Build the package

```bash
pipenv run python -m build
```

### Publish to PyPI (maintainers only)

```bash
twine upload dist/*
```

### Developer workflow

1. Create a feature branch off `main`.
2. Make your changes and add tests.
3. Open a pull request to `main` and ask a teammate to review.
4. After approval and passing CI, merge and delete the feature branch.

---

## Team

- [Aaron Hui](https://github.com/aaronthmetic)
- [Uwa Igbinedion](https://github.com/uwa00)
- [Antonio Jackson](https://github.com/antoniojacksnn)
- [Hitaansh Jain](https://github.com/hitaanshjain)
- [James Huang](https://github.com/JamesHuang2004)
