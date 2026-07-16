from src.model.wendys_problem import WendysProblem, WendysSolution


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
