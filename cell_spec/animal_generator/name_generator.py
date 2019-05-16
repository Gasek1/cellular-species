"""Generate names for specimens."""

import os
import json
from random import choices

with open(os.path.join(os.path.dirname(__file__), "name_syllables.json")) as file:
    syllables = json.load(file)


def generate_name(number_of_syllables: int):
    """Return a random animal name."""
    return "".join(choices(syllables, k=number_of_syllables)).capitalize()
