import re

from playwright.sync_api import Locator, Page, expect


def expect_path(page: Page, path_fragment: str) -> None:
    escaped = re.escape(path_fragment)
    expect(page).to_have_url(re.compile(rf".*{escaped}(?:\?.*)?$"))


def expect_visible(locator: Locator) -> None:
    expect(locator).to_be_visible()


def expect_not_visible(locator: Locator) -> None:
    expect(locator).not_to_be_visible()


def expect_text(locator: Locator, text: str) -> None:
    expect(locator).to_have_text(text)


def expect_page_title(page: Page, title: str) -> None:
    expect(page).to_have_title(re.compile(re.escape(title), re.IGNORECASE))


def expect_element_count(locator: Locator, count: int) -> None:
    expect(locator).to_have_count(count)


def expect_contains_text(locator: Locator, text: str) -> None:
    expect(locator).to_contain_text(text)
