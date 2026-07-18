from src.scrape.hitup_wendy import get_latest_wendys_problem
from src.seek.solve_wend import solve_wendys_problem


def main():
    print("[Fetching] latest wendys problem!")
    wendys_latest_problem = get_latest_wendys_problem()
    solve_wendys_problem(wendys_latest_problem)
    wendys_latest_problem.pprint_wend_solutions()
    print("[Solved] wendys problem")


if __name__ == "__main__":
    main()
