import pytest

@pytest.mark.regression
def test_product_purchase_flow(login_page, dashboard_page, product_page, cart_page, settings):
    """Scenario 3: Product Purchase Flow
    
    Steps:
    1. Login to application
    2. Add product to cart
    3. Go to cart
    4. Verify product added successfully
    """
    # Step 1: Login to application
    login_page.open(settings.base_url)
    login_page.login(settings.username, settings.password)
    dashboard_page.is_loaded()
    
    # Assertion: Verify page title and products availability
    assert dashboard_page.get_page_title() =="Swag Labs"
    product_page.is_loaded()
    assert product_page.get_product_count() > 0, "No products available"
    
    # Step 2: Add product to cart
    product_name = "Sauce Labs Backpack"
    assert product_page.is_product_available(product_name), f"Product {product_name} not available"
    product_page.add_product_to_cart(product_name)
    
    # Assertion: Verify cart count increased
    assert product_page.get_cart_count() == "1", "Product count in cart should be 1"
    
    # Step 3: Go to cart
    product_page.go_to_cart()
    
    # Step 4: Verify product added successfully
    cart_page.is_loaded()
    assert cart_page.get_cart_item_count() == 1, "Should have 1 item in cart"
    assert cart_page.is_product_in_cart(product_name), f"Product {product_name} not found in cart"
    
    # Additional assertions for product verification
    items = cart_page.get_item_names()
    assert len(items) == 1
    assert product_name in items[0]
