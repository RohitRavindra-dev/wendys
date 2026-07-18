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

TRAVERSE_DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))


WENDYS_URL = "https://www.linkedin.com/games/wend"
BOARD_SELECTOR = '[data-testid="interactive-grid"]'
SLOTS_LOCATOR = '[data-testid^="wend-word-list-slot-"]'
START_GAME_LOCATOR = 'a[href*="skipStartScreen"]'
EMPTY_CELL_ATTRIBUTE = "data-cell-is-hole"
DATA_TEST_ID_ATTRIBUTE = "data-testid"

SCRAPE_TIMEOUT = 3000
