from src.constants import TRAVERSE_DIRECTIONS
from src.filers.pickle_file_manager import load_trie
from src.model.wendys_problem import WendysProblem
from src.model.trie import TrieNode
from src.seek.possibilities import get_solutions_from_possibilities, printPossibleWords

# traverse dfs
# keep track of path
# if word and word len in config then add to possibilities
# continue until no more
# see possibilities and pick one answer
def solve_wend(problem: WendysProblem) -> None:
    print("Started to solve wendys problem")

    trie = load_trie()

    possibilities: dict[int, list[list[tuple[int, int]]]] = {
        i: [] for i in problem.config
    }

    curPath: list[tuple[int, int]] = []

    def dfs(curNode: TrieNode, i: int, j: int):
        if curNode.is_end and len(curPath) in possibilities:
            possibilities[len(curPath)].append(curPath.copy())

        for dx, dy in TRAVERSE_DIRECTIONS:
            x, y = i + dx, j + dy
            if (
                -1 < x < problem.grid_height
                and -1 < y < problem.grid_width
                and problem.grid[x][y] != "#"
                and problem.grid[x][y] in curNode.children
            ):
                temp, problem.grid[x][y] = problem.grid[x][y], "#"
                curPath.append((x, y))
                dfs(curNode.children[temp], x, y)
                curPath.pop()
                problem.grid[x][y] = temp

    for i in range(problem.grid_height):
        for j in range(problem.grid_width):
            if problem.grid[i][j] != ".":
                curPath.append((i, j))
                temp, problem.grid[i][j] = problem.grid[i][j], "#"
                dfs(trie.get_papa(temp), i, j)  # type: ignore
                problem.grid[i][j] = temp
                curPath.pop()

    printPossibleWords(problem, possibilities)
    get_solutions_from_possibilities(problem, possibilities)
    print(f"Solns for config: {problem.config} =>")
    for soln in problem.solutions:
        print(soln.solution)


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
    solve_wend(wend_problem)


if __name__ == "__main__":
    main()
