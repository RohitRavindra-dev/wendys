import urllib.request
from pathlib import Path

WORDLIST_URL = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
WORDLIST_PATH = Path("words_alpha.txt")

def download_wordlist() -> None:
    print(f"Downloading all the words in english language into: {WORDLIST_URL}")
    urllib.request.urlretrieve(WORDLIST_URL, WORDLIST_PATH)


def main()-> None:
    download_wordlist()
    
if __name__ == "__main__":
    main()