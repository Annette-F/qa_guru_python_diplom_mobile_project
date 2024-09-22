import allure
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


@allure.tag('Mobile')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Authorization with valid login and password')
@allure.story('Authorization')
def test_successfull_authorization():
    with allure.step('Open profile'):
        browser.element((AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Профиль"]')).click()
    with allure.step('Fill Email'):
        browser.element((AppiumBy.XPATH,
                         '//android.view.View[@resource-id="nav"]/android.view.View[2]/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText')).type(
            'marivtest@mail.ru')
    with allure.step('Fill Password'):
        browser.element((AppiumBy.XPATH,
                         '//android.view.View[@resource-id="nav"]/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText')).type(
            'testing1')
        browser.element((AppiumBy.XPATH, '//android.widget.Button[@resource-id="sign-in"]')).click()
    with allure.step('Check the successful authorization'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="МАРИЯ"]')).should(have.text('МАРИЯ'))


@allure.tag('Mobile')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Search a product')
@allure.story('Search')
def test_search_goods():
    with allure.step('Enter the country of origin of the product'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Поиск"]')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.EditText')).type('Эфиопия').click()
    with allure.step('Choose the proposed option'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Кофе из Эфиопии"]')).click()
    with allure.step('Check the search result'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Эфиопия Иргачефф"]')).should(
            have.text('Эфиопия Иргачефф'))


@allure.tag('Mobile')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Adding a product to cart')
@allure.story('Cart')
def test_add_goods_to_cart():
    with allure.step('Enter the country of origin of the product'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Поиск"]')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.EditText')).type('Бразилия').click()
    with allure.step('Choose the proposed option'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Кофе из Бразилии"]')).click()
    with allure.step('Add product to cart'):
        browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Купить"]')).click()
    with allure.step('Check adding the product to cart'):
        browser.element((AppiumBy.XPATH, '//android.view.View[@content-desc=" Перейти в корзину"]')).click()
        browser.element((AppiumBy.XPATH,
                         '//android.view.View[@resource-id="nav"]/android.view.View[2]/android.view.View[1]/android.view.View[2]')).should(
            be.visible)


@allure.tag('Mobile')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Remove a product from cart')
@allure.story('Cart')
def test_remove_goods_from_cart():
    with allure.step('Add product to cart'):
        browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Купить"]')).click()
    with allure.step('Open cart'):
        browser.element((AppiumBy.XPATH, '//android.view.View[@content-desc=" Перейти в корзину"]')).click()
    with allure.step('Open action-menu'):
        browser.element((AppiumBy.XPATH, '//android.widget.Button[@text=". . ."]')).click()
    with allure.step('Remove the product from cart'):
        browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Удалить"]')).click()
    with allure.step('Check removing the product from cart'):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="ВАША КОРЗИНА ПУСТА"]')).should(
            have.text('ВАША КОРЗИНА ПУСТА'))
