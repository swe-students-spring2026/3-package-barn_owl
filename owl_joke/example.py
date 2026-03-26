#!/usr/bin/env python3
"""
Example program demonstrating the owl_joke package functionality.
"""

from owl_joke import owl_joke, get_owl_joke, list_owl_jokes, count_owl_jokes_in_category

def main():
    # Get a random owl joke from a category
    wise_joke = owl_joke("wise")
    print(f"Random wise owl joke: {wise_joke}")

    # Get a specific owl joke by category and index
    first_funny_joke = get_owl_joke("funny", 0)
    print(f"First funny owl joke: {first_funny_joke}")

    # List all owl jokes in a category
    programming_jokes = list_owl_jokes("programming")
    print(f"Programming owl jokes: {programming_jokes[:2]}...")  # Show first 2

    # Count owl jokes in a category
    nature_count = count_owl_jokes_in_category("nature")
    print(f"Number of nature owl jokes: {nature_count}")

if __name__ == "__main__":
    main()