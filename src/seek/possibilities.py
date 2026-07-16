from src.constants import TRAVERSE_DIRECTIONS
from src.model.trie import Trie, TrieNode
from src.model.wendys_problem import WendysProblem, WendysSolution


def get_possibilities_from_problem(problem: WendysProblem, trie: Trie):

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

    return possibilities


def get_solutions_from_possibilities(
    wendys_problem: WendysProblem,
    possibilities: dict[int, list[list[tuple[int, int]]]],
):
    visited = [
        [False] * wendys_problem.grid_width for _ in range(wendys_problem.grid_height)
    ]

    def markVisited(path: list[tuple[int, int]]) -> bool:
        for i, pos in enumerate(path):
            x, y = pos
            if visited[x][y]:
                # revert
                for j in range(0, i):
                    x0, y0 = path[j]
                    visited[x0][y0] = False
                return False
            visited[x][y] = True
        return True

    def unmarkPath(path: list[tuple[int, int]]):
        for x, y in path:
            if not (visited[x][y]):
                return
            visited[x][y] = False

    cur: list[int] = []

    def dfs(config_pos: int):
        if config_pos == len(wendys_problem.config):
            wendys_problem.solutions.append(
                WendysSolution(wendys_problem.config, possibilities, cur)
            )
            return

        for i, pos in enumerate(possibilities[wendys_problem.config[config_pos]]):
            if markVisited(pos):
                cur.append(i)
                dfs(config_pos + 1)
                cur.pop()
                unmarkPath(pos)

    for i in range(len(possibilities[wendys_problem.config[0]])):
        markVisited(possibilities[wendys_problem.config[0]][i])
        cur.append(i)
        dfs(1)
        cur.pop()
        unmarkPath(possibilities[wendys_problem.config[0]][i])
