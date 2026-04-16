import pytest

from utils.assertions import expect_path, expect_visible, expect_contains_text


@pytest.mark.smoke
def test_valid_login_redirects_to_dashboard(login_page, dashboard_page, settings):
    """Scenario 1: Login Validation - Successful login with valid credentials."""
    # Step 1: Open application
    login_page.open(settings.base_url)
    
    # Step 2: Enter valid username and password
    login_page.enter_username(settings.username)
    login_page.enter_password(settings.password)
    
    # Step 3: Click login
    login_page.submit()
    
    # Step 4: Verify successful login
    dashboard_page.is_loaded()
    expect_path(login_page.page, dashboard_page.PATH)
    
    # Additional assertions
    assert dashboard_page.get_page_title() == "Swag Labs"
    assert dashboard_page.verify_products_available()


@pytest.mark.smoke
def test_invalid_login_shows_error(login_page, settings):
    """Scenario 2: Invalid Login - Error message displayed for incorrect credentials."""
    # Step 1: Open application
    login_page.open(settings.base_url)
    
    # Step 2: Enter incorrect credentials
    login_page.enter_username("invalid_user")
    login_page.enter_password("invalid_password")
    
    # Step 3: Click login
    login_page.submit()
    
    # Step 4: Verify error message is displayed
    assert login_page.is_error_displayed()
    error_msg = login_page.get_error_message()
    assert "Epic sadface" in error_msg or "Username" in error_msg or "Password" in error_msg
