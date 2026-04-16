from __future__ import annotations

from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class DashboardPage(BasePage):
    PATH = "/inventory.html"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.header_title: Locator = page.locator('[class="app_logo"]')
        self.product_items: Locator = page.locator('.inventory_item')
        self.cart_link: Locator = page.locator('a.shopping_cart_link')
        self.cart_badge: Locator = page.locator('.shopping_cart_badge')

    def is_loaded(self) -> None:
        self.wait_for_visible(self.header_title)

    def get_page_title(self) -> str:
        """Get the inventory page title."""
        return self.page.title()

    def verify_products_available(self) -> bool:
        """Verify products are displayed on the page."""
        return self.page.locator('.inventory_item').count() > 0

    def get_cart_count(self) -> str:
        """Get cart item count."""
        return self.text(self.cart_badge)

    def go_to_cart(self) -> None:
        """Navigate to cart page."""
        self.click(self.cart_link)
