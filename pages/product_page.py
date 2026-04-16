from __future__ import annotations

from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class ProductPage(BasePage):
    PATH = "/inventory.html"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.inventory_container: Locator = page.locator('[data-test="inventory-container"]').first
        self.product_items: Locator = page.locator('.inventory_item')
        self.product_names: Locator = page.locator('.inventory_item_name')
        self.cart_link: Locator = page.locator('a.shopping_cart_link')
        self.cart_badge: Locator = page.locator('.shopping_cart_badge')

    def is_loaded(self) -> None:
        self.wait_for_visible(self.inventory_container)

    def get_product_count(self) -> int:
        """Get total number of products displayed."""
        return self.product_items.count()

    def is_product_available(self, product_name: str) -> bool:
        """Check if a specific product is available."""
        return self.page.locator('.inventory_item_name', has_text=product_name).count() > 0

    def add_product_to_cart(self, product_name: str) -> None:
        """Add a specific product to cart by name."""
        self.page.locator(
            '.inventory_item',
            has_text=product_name,
        ).locator('button:has-text("Add to cart")').click()

    def get_cart_count(self) -> str:
        """Get cart item count badge."""
        return self.text(self.cart_badge)

    def go_to_cart(self) -> None:
        """Navigate to cart page."""
        self.click(self.cart_link)
