def getWord(grid, path: list[tuple[int, int]]):
    word = ""
    for x, y in path:
        word += grid[x][y]
    return word


def printPossibleWords(
    grid: list[list[str]], possibilities: dict[int, list[list[tuple[int, int]]]]
):

    for k, v in possibilities.items():
        for pos in v:
            print(f"{k}: {getWord(grid, pos)} @{pos}")


def get_possible_solutions(
    gridWidth: int,
    gridHeight: int,
    possibilities: dict[int, list[list[tuple[int, int]]]],
    config: list[int],
)->list[list[int]]:
    visited = [[False] * gridWidth for _ in range(gridHeight)]

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

    solns:list[list[int]] = []
    cur:list[int] = []

    def dfs(config_pos: int):
        if config_pos == len(config):
            solns.append(cur.copy())
            return

        for i, pos in enumerate(possibilities[config[config_pos]]):
            if markVisited(pos):
                cur.append(i)
                dfs(config_pos + 1)
                cur.pop()
                unmarkPath(pos)

    for i in range(len(possibilities[config[0]])):
        markVisited(possibilities[config[0]][i])
        cur.append(i)
        dfs(1)
        cur.pop()
        unmarkPath(possibilities[config[0]][i])

    return solns
