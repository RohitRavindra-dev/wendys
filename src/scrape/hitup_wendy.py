from collections import Counter
from playwright.sync_api import Locator, sync_playwright, Page

from src.constants import (
    BOARD_SELECTOR,
    DATA_TEST_ID_ATTRIBUTE,
    EMPTY_CELL_ATTRIBUTE,
    SCRAPE_TIMEOUT,
    SLOTS_LOCATOR,
    START_GAME_LOCATOR,
    WENDYS_URL,
)
from src.model.wendys_problem import WendysProblem


def get_board_dimensions(page: Page, board: Locator) -> tuple[int, int]:

    cols = page.evaluate(
        "(e) => getComputedStyle(e).gridTemplateColumns",
        board.element_handle(),
    )

    rows = page.evaluate(
        "(e) => getComputedStyle(e).gridTemplateRows",
        board.element_handle(),
    )

    num_cols = len(cols.split())
    num_rows = len(rows.split())

    return num_rows, num_cols


def _get_bored(page: Page) -> list[list[str]]:

    board = page.locator(BOARD_SELECTOR)
    cells = board.locator("[data-cell-idx]")
    rows, cols = get_board_dimensions(page, board)

    assert cells.count() == rows * cols, (
        f"Expected {rows * cols} cells, found {cells.count()}"
    )

    grid: list[list[str]] = []

    for r in range(rows):
        row: list[str] = []

        for c in range(cols):
            cell = cells.nth(r * cols + c)

            if cell.get_attribute(EMPTY_CELL_ATTRIBUTE) == "true":
                row.append(".")
            else:
                row.append(cell.text_content().strip())  # type: ignore

        grid.append(row)

    return grid


def _get_word_lengths(page: Page) -> list[int]:
    """Returns the hidden word lengths."""

    slots = page.locator(SLOTS_LOCATOR)

    counter = Counter()

    for i in range(slots.count()):
        testid = slots.nth(i).get_attribute(DATA_TEST_ID_ATTRIBUTE)

        # wend-word-list-slot-2-5
        word_idx = int(testid.split("-")[-2])  # type: ignore

        counter[word_idx] += 1

    return [counter[idx] for idx in sorted(counter)]


def get_latest_wendys_problem() -> WendysProblem:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto(WENDYS_URL)

        # Skip splash start screen if present
        try:
            page.locator(START_GAME_LOCATOR).click(timeout=SCRAPE_TIMEOUT)
        except Exception:
            pass

        page.wait_for_selector(BOARD_SELECTOR)

        board = _get_bored(page)
        word_lengths = _get_word_lengths(page)

        browser.close()

        return WendysProblem(board, word_lengths)


if __name__ == "__main__":
    todays_wendy_problem = get_latest_wendys_problem()

    print("Todays board:", todays_wendy_problem.grid)

    print("\nWord lengths:", todays_wendy_problem.config)
