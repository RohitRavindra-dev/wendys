import urllib.request

from src.constants import WORDLIST_PATH, WORDLIST_URL


def download_wordlist() -> None:
    print(f"Downloading all the words in english language into: {WORDLIST_PATH}")
    urllib.request.urlretrieve(WORDLIST_URL, WORDLIST_PATH)


def main() -> None:
    download_wordlist()


if __name__ == "__main__":
    main()
