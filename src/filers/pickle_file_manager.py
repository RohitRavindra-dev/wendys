from functools import lru_cache
import pickle
from src.constants import TRIE_PICKLE_OUTPUT_PATH
from src.model.trie import Trie


def save_trie(trie: Trie):
    with TRIE_PICKLE_OUTPUT_PATH.open("wb") as f:
        pickle.dump(trie, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"Saved trie to {TRIE_PICKLE_OUTPUT_PATH}")
    
@lru_cache(maxsize=1)
def load_trie() -> Trie:
    print(f"Starting to load trie from path: {TRIE_PICKLE_OUTPUT_PATH}")
    with TRIE_PICKLE_OUTPUT_PATH.open("rb") as f:
        trie:Trie = pickle.load(f)
        print("Trie Loaded!")
        return trie
    