from __future__ import annotations

from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    PATH = "/"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.username_input: Locator = page.locator('[id="user-name"]')
        self.password_input: Locator = page.locator('[id="password"]')
        self.login_button: Locator = page.locator('[id="login-button"]')
        self.error_container: Locator = page.locator('[data-test="error"]')

    def open(self, base_url: str) -> None:
        self.visit(f"{base_url}{self.PATH}")

    def enter_username(self, username: str) -> None:
        self.fill(self.username_input, username)

    def enter_password(self, password: str) -> None:
        self.fill(self.password_input, password)

    def submit(self) -> None:
        self.click(self.login_button)

    def login(self, username: str, password: str) -> None:
        self.enter_username(username)
        self.enter_password(password)
        self.submit()

    def get_error_message(self) -> str:
        return self.text(self.error_container)

    def is_error_displayed(self) -> bool:
        return self.error_container.count() > 0
