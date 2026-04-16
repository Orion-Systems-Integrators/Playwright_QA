from __future__ import annotations

import os

import pytest
from playwright.sync_api import Page

from config.settings import get_settings
from pages.cart_page import CartPage
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.fixture(scope="session")
def settings():
    return get_settings()


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """Slow down browser actions so UI steps are visible while debugging locally."""
    slow_mo_ms = int(os.getenv("PW_SLOWMO_MS", "600"))
    return {
        **browser_type_launch_args,
        "slow_mo": slow_mo_ms,
    }


@pytest.fixture()
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture()
def dashboard_page(page: Page) -> DashboardPage:
    return DashboardPage(page)


@pytest.fixture()
def product_page(page: Page) -> ProductPage:
    return ProductPage(page)


@pytest.fixture()
def cart_page(page: Page) -> CartPage:
    return CartPage(page)
