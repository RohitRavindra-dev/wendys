from src.constants import TRAVERSE_DIRECTIONS
from src.filers.pickle_file_manager import load_trie
from src.model.trie import TrieNode
from src.seek.possibilities import get_possible_solutions, printPossibleWords


def solve_wend(grid: list[list[str]], config: list[int]) -> None:
    print("Started to solve wend")

    trie = load_trie()

    possibilities: dict[int, list[list[tuple[int, int]]]] = {i: [] for i in config}
    m, n = len(grid), len(grid[0])
    curPath: list[tuple[int, int]] = []

    def dfs(curNode: TrieNode, i: int, j: int):
        if curNode.is_end and len(curPath) in possibilities:
            possibilities[len(curPath)].append(curPath.copy())

        for dx, dy in TRAVERSE_DIRECTIONS:
            x, y = i + dx, j + dy
            if (
                -1 < x < m
                and -1 < y < n
                and grid[x][y] != "#"
                and grid[x][y] in curNode.children
            ):
                temp, grid[x][y] = grid[x][y], "#"
                curPath.append((x, y))
                dfs(curNode.children[temp], x, y)
                curPath.pop()
                grid[x][y] = temp

    for i in range(m):
        for j in range(n):
            if grid[i][j] != ".":
                curPath.append((i, j))
                temp, grid[i][j] = grid[i][j], "#"
                dfs(trie.get_papa(temp), i, j)  # type: ignore
                grid[i][j] = temp
                curPath.pop()

    printPossibleWords(grid, possibilities)
    print(
        f"Solns for config: {config} => {get_possible_solutions(m, n, possibilities, config)}"
    )


# traverse dfs
# keep track of path
# if word and word len in config then add to possibilities
# continue until no more
# see possibilities and pick one answer : TODO


def main():
    grid = [
        ["U", "P", ".", "O", "N"],
        ["M", "O", "O", "B", "A"],
        ["P", "K", ".", "P", "I"],
        ["K", "B", "O", "T", "M"],
        ["I", "N", ".", "T", "O"],
    ]

    config = [4, 5, 6, 7]

    solve_wend(grid, config)


if __name__ == "__main__":
    main()
