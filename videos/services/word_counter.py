import re


def count_words(text):

    words = re.findall(

        r"\b[a-zA-Z']+\b",

        text.lower()
    )
    unique_words = set(words)

    return len(unique_words)