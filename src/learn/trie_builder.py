# get list of all words in english
# build a trie of this
# pickle dump that shi

import pickle
from wordfreq import zipf_frequency

from src.constants import TRIE_PICKLE_OUTPUT_PATH, WORDLIST_PATH
from src.model.trie import Trie

from src.learn.file_fetcher import download_wordlist


def build_trie() -> Trie:
    trie = Trie()

    with WORDLIST_PATH.open() as f:
        for line in f:
            word = line.strip().lower()
            if word.isalpha() and zipf_frequency(word, "en") >= 2.5:
                trie.insert(word)
    return trie


def save_trie(trie: Trie):
    with TRIE_PICKLE_OUTPUT_PATH.open("wb") as f:
        pickle.dump(trie, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"Saved trie to {TRIE_PICKLE_OUTPUT_PATH}")


def main() -> None:
    download_wordlist()
    trie = build_trie()
    save_trie(trie)


if __name__ == "__main__":
    main()
