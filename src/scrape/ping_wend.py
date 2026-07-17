from collections import Counter
from playwright.sync_api import sync_playwright


START_URL = "https://www.linkedin.com/games/wend"
BOARD_SELECTOR = '[data-testid="interactive-grid"]'


def get_board_dimensions(page) -> tuple[int, int]:
    """Returns (rows, cols) of the board."""

    board = page.locator(BOARD_SELECTOR)

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


def get_board(page) -> list[str]:
    """Returns the board as list[str], using '.' for blocked cells."""

    rows, cols = get_board_dimensions(page)

    board = page.locator(BOARD_SELECTOR)
    cells = board.locator("[data-cell-idx]")

    assert (
        cells.count() == rows * cols
    ), f"Expected {rows * cols} cells, found {cells.count()}"

    grid = []

    for r in range(rows):
        row = []

        for c in range(cols):
            cell = cells.nth(r * cols + c)

            if cell.get_attribute("data-cell-is-hole") == "true":
                row.append(".")
            else:
                row.append(cell.text_content().strip())

        grid.append("".join(row))

    return grid


def get_word_lengths(page) -> list[int]:
    """Returns the hidden word lengths."""

    slots = page.locator('[data-testid^="wend-word-list-slot-"]')

    counter = Counter()

    for i in range(slots.count()):
        testid = slots.nth(i).get_attribute("data-testid")

        # wend-word-list-slot-2-5
        word_idx = int(testid.split("-")[-2])

        counter[word_idx] += 1

    return [counter[idx] for idx in sorted(counter)]


def scrape_today_puzzle():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto(START_URL)

        # Skip splash screen if present
        try:
            page.locator('a[href*="skipStartScreen"]').click(timeout=3000)
        except Exception:
            pass

        page.wait_for_selector(BOARD_SELECTOR)

        dimensions = get_board_dimensions(page)
        board = get_board(page)
        word_lengths = get_word_lengths(page)

        browser.close()

        return dimensions, board, word_lengths


if __name__ == "__main__":
    dimensions, board, word_lengths = scrape_today_puzzle()

    print(f"Board: {dimensions[0]} x {dimensions[1]}\n")

    for row in board:
        print(row)

    print("\nWord lengths:", word_lengths)