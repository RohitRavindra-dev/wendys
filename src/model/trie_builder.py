# get list of all words in english
# build a trie of this
# pickle dump that shi

from wordfreq import zipf_frequency

from src.constants import WORDLIST_PATH
from src.filers.pickle_file_manager import save_trie
from src.model.trie import Trie

from src.filers.file_fetcher import download_wordlist


def build_trie() -> Trie:
    trie = Trie()

    with WORDLIST_PATH.open() as f:
        for line in f:
            word = line.strip().lower()
            if word.isalpha() and zipf_frequency(word, "en") >= 1.5:
                trie.insert(word.upper())
    return trie


def main() -> None:
    download_wordlist()
    trie = build_trie()
    save_trie(trie)


if __name__ == "__main__":
    main()
