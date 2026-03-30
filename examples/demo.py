"""Demonstrate every function in the barn_owl package.

Run from the repository root after installing the package, for example:

    pipenv run python examples/demo.py

or:

    python examples/demo.py
"""

from barn_owl import (
    owl_drawing,
    owl_jokes,
    owl_name_generator,
    owl_wisdom,
    to_owl_latin,
)


def main() -> None:
    print("=== Owl wisdom (topic: coding) ===")
    print(owl_wisdom(topic="coding"))
    print()

    print("=== Owl Latin ===")
    print(to_owl_latin("hello developer"))
    print()

    print("=== Owl joke (category: python) ===")
    print(owl_jokes(category="python"))
    print()

    print("=== Owl drawing (style: cute) ===")
    print(owl_drawing(style="cute"))
    print()

    print("=== Random owl name (style: wise) ===")
    print(owl_name_generator(style="wise"))


if __name__ == "__main__":
    main()
