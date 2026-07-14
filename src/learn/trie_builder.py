# get list of all words in english
# build a trie of this
# pickle dump that shi

import pickle
from pathlib import Path

from src.model.trie import Trie


WORDLIST_PATH = Path("words_alpha.txt")
OUTPUT_PATH = Path("trie.pkl")


def build_trie() -> Trie:
    trie = Trie()
    with WORDLIST_PATH.open() as f:
        for line in f:
            word = line.strip().lower()
            if word.isalpha():
                trie.insert(word)
    return trie


def main() -> None:
    trie = build_trie()
    with OUTPUT_PATH.open("wb") as f:
        pickle.dump(trie, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"Saved trie to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()