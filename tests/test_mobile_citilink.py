import allure
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


@allure.tag('Mobile')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Successfull search product')
@allure.story('Search')
def test_successfull_search_product():
    with allure.step('Open main page'):
        # browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')).click()
        browser.element((AppiumBy.ID, 'android:id/button1')).click()
    with allure.step('Type search "Смартфон"'):
        browser.element((AppiumBy.ID, 'ru.citilink:id/buttonSearch')).click()
        browser.element((AppiumBy.ID, 'ru.citilink:id/editTextSearchToolbar')).type('Смартфон').click()
    with allure.step('Open page "Смартфоны"'):
        browser.element((AppiumBy.ID, 'ru.citilink:id/textViewSearchCategoryName')).should(
            have.text('Смартфоны')).click()
    with allure.step('Check results'):
        browser.element((AppiumBy.ID, 'ru.citilink:id/textViewProductsListTitle')).should(have.text('Смартфоны'))


@allure.tag('Mobile')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Add the product to the Wishlist')
@allure.story('Wishlist')
def test_product_to_the_wishlish():
    with allure.step('Open main page'):
        # browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')).click()
        browser.element((AppiumBy.ID, 'android:id/button1')).click()
    with allure.step('Type search "Смарт-часы"'):
        browser.element((AppiumBy.ID, 'ru.citilink:id/buttonSearch')).click()
        browser.element((AppiumBy.ID, 'ru.citilink:id/editTextSearchToolbar')).type('Смарт-часы').click()
    with allure.step('Open page "Смарт-часы"'):
        browser.element((AppiumBy.ID, 'ru.citilink:id/textViewSearchCategoryName')).should(
            have.text('Смарт-часы')).click()
    with allure.step('Add the product to the Wishlist'):
        browser.element((AppiumBy.ID, 'ru.citilink:id/constraintLayoutItemProduct')).element(
            (AppiumBy.ID, 'ru.citilink:id/imageViewFavorite')).click()
    with allure.step('Check adding the product to the Wishlist'):
        browser.element((AppiumBy.XPATH,
                         '//android.widget.TextView[@resource-id="ru.citilink:id/navigation_bar_item_small_label_view" and @text="Избранное"]')).click()
        browser.element((AppiumBy.ID, 'ru.citilink:id/constraintLayoutItemProduct')).should(be.visible)


@allure.tag('Mobile')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Add product to the cart')
@allure.story('Cart')
def test_add_product_to_the_cart():
    with allure.step('Open main page'):
        # browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')).click()
        browser.element((AppiumBy.ID, 'android:id/button1')).click()
    with allure.step('Type search "Ноутбук"'):
        browser.element((AppiumBy.ID, 'ru.citilink:id/buttonSearch')).click()
        browser.element((AppiumBy.ID, 'ru.citilink:id/editTextSearchToolbar')).type('Ноутбук').click()
    with allure.step('Open page "Ноутбуки"'):
        browser.element((AppiumBy.ID, 'ru.citilink:id/textViewSearchCategoryName')).should(
            have.text('Ноутбуки')).click()
    with allure.step('Add product to the cart'):
        browser.element((AppiumBy.ID, 'ru.citilink:id/constraintLayoutItemProduct')).element(
            (AppiumBy.ID, 'ru.citilink:id/buttonProductItemAddToCart')).should(have.text('В корзину')).click()
        browser.element((AppiumBy.XPATH,
                         '//android.widget.TextView[@resource-id="ru.citilink:id/navigation_bar_item_small_label_view" and @text="Корзина"]')).click()
    with allure.step('Check adding product to the cart'):
        browser.element((AppiumBy.ID, 'ru.citilink:id/textViewCartBottomOrderTotalLabel')).should(
            have.text('Сумма к оплате'))
        browser.element((AppiumBy.ID, 'ru.citilink:id/buttonMakeOrder')).should(have.text('К оформлению'))


@allure.tag('Mobile')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Change city')
@allure.story('Profile')
def test_select_my_city():
    # with allure.step('Open main page'):
    #     browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')).click()
    with allure.step('Declain city'):
        browser.element((AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button2"]')).click()
    with allure.step('Select "Москва"'):
        browser.element((AppiumBy.XPATH,
                         '//android.widget.TextView[@resource-id="ru.citilink:id/textViewCityName" and @text="Москва"]')).click()
    with allure.step('Open profile'):
        browser.element((AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Профиль"]')).click()
    with allure.step('Check selected city'):
        browser.element((AppiumBy.XPATH,
                         '//android.widget.TextView[@resource-id="ru.citilink:id/textViewProfileCityValue"]')).should(
            have.text('Москва'))
