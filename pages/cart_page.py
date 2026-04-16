from __future__ import annotations

from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class CartPage(BasePage):
    PATH = "/cart.html"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.cart_items: Locator = page.locator('.cart_item')
        self.item_names: Locator = page.locator('.inventory_item_name')
        self.item_prices: Locator = page.locator('.inventory_item_price')
        self.checkout_button: Locator = page.locator('[data-test="checkout"]')
        self.continue_shopping: Locator = page.locator('[data-test="continue-shopping"]')

    def is_loaded(self) -> None:
        self.wait_for_visible(self.checkout_button)

    def get_cart_item_count(self) -> int:
        """Get total items in cart."""
        return self.cart_items.count()

    def get_item_names(self) -> list[str]:
        """Get all item names in cart."""
        names = []
        for i in range(self.item_names.count()):
            names.append(self.item_names.nth(i).text_content() or "")
        return names

    def is_product_in_cart(self, product_name: str) -> bool:
        """Verify specific product is in cart."""
        return self.page.locator('.inventory_item_name', has_text=product_name).count() > 0

    def proceed_to_checkout(self) -> None:
        """Click checkout button."""
        self.click(self.checkout_button)

    def continue_shopping(self) -> None:
        """Click continue shopping."""
        self.click(self.continue_shopping)
