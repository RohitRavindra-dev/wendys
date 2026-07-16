from src.filers.pickle_file_manager import load_trie
from src.model.wendys_problem import WendysProblem
from src.seek.possibilities import (
    get_possibilities_from_problem,
    get_solutions_from_possibilities,
)


# traverse dfs
# keep track of path
# if word and word len in config then add to possibilities
# continue until no more
# see possibilities and pick one answer
def solve_wendys_problem(problem: WendysProblem) -> None:
    print("Started to solve wendys problem")

    trie = load_trie()
    possibilities = get_possibilities_from_problem(problem, trie)
    get_solutions_from_possibilities(problem, possibilities)


# problem creation from webpage (llm?, webscrape?): TODO
def main():
    grid = [
        ["U", "P", ".", "O", "N"],
        ["M", "O", "O", "B", "A"],
        ["P", "K", ".", "P", "I"],
        ["K", "B", "O", "T", "M"],
        ["I", "N", ".", "T", "O"],
    ]

    config = [4, 5, 6, 7]

    wend_problem = WendysProblem(grid, config)
    solve_wendys_problem(wend_problem)
    wend_problem.pprint_wend_solutions()


if __name__ == "__main__":
    main()
