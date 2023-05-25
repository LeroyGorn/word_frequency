import re
from collections import Counter


def word_frequency(paragraph):
    frequency = Counter()
    word_pattern = re.compile(r'\b\w+\b')

    for sentence in paragraph:
        frequency.update(word_pattern.findall(sentence.lower()))

    return dict(frequency)


paragraph = [
    "The quick brown fox",
    "jumps over the lazy dog.",
    "The dog barks,",
    "and the fox runs away."
]

print(word_frequency(paragraph))
