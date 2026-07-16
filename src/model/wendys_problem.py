class WendysSolution:
    __slots__ = "solution"

    def __init__(
        self,
        config: list[int],
        possiblity_map: dict[int, list[list[tuple[int, int]]]],
        possible_solution: list[int],
    ) -> None:
        self.solution: dict[int, list[tuple[int, int]]] = {}
        for i, word_len in enumerate(config):
            self.solution[word_len] = possiblity_map[word_len][possible_solution[i]]

    def pprint_solution(self):
        print(f"{'-'*10}SOLUTION{'-'*10}")
        for wl, sol in self.solution.items():
            print(f"Word len:{wl} is along path: {sol}", end=" ")
            yield sol
        print("-" * 30)


class WendysProblem:
    __slots__ = ("grid", "config", "grid_width", "grid_height", "solutions")

    def __init__(self, grid: list[list[str]], config: list[int]) -> None:
        # todo validation
        self.grid = grid
        self.grid_width = len(grid[0])
        self.grid_height = len(grid)
        self.config = sorted(config, reverse=True)
        self.solutions: list[WendysSolution] = []

    def get_word_along_path(self, path: list[tuple[int, int]]) -> str:
        word = ""
        for x, y in path:
            word += self.grid[x][y]
        return word

    def pprint_wend_solutions(self):
        for soln in self.solutions:
            for path in soln.pprint_solution():
                print(f"-> {self.get_word_along_path(path)}")
