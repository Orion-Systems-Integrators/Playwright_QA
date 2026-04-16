from __future__ import annotations

from playwright.sync_api import Locator, Page, expect


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def visit(self, url: str) -> None:
        self.page.goto(url)

    def click(self, locator: Locator) -> None:
        locator.click()

    def fill(self, locator: Locator, value: str) -> None:
        locator.fill(value)

    def text(self, locator: Locator) -> str:
        return locator.text_content() or ""

    def wait_for_visible(self, locator: Locator) -> None:
        expect(locator).to_be_visible()
