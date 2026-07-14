from pathlib import Path

PROJECT_ROOT = (
    Path(__file__).resolve().parent.parent
)  # src/constants.py -> project root
OUTPUT_DIR = PROJECT_ROOT / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

WORDLIST_URL = (
    "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
)
WORDLIST_PATH = OUTPUT_DIR / "words_alpha.txt"
TRIE_PICKLE_OUTPUT_PATH = OUTPUT_DIR / "trie.pkl"
