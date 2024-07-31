import pytest
from Lesson_7.Data_types.Pages.Mainpage import MainPage
import allure

@allure.title("Заполнить форму значениями")
@allure.description("заполнение формы конкретными значениями")    
@allure.severity("critical")
values_dict = {'first-name': 'Иван', 'last-name': 'Петров', 'address': 'Ленина, 55-3', 'e-mail': 'test@skypro.com', 'phone': '+7985899998787', 'city': 'Москва', 'country': 'Россия', 'job-position': 'QA', 'company': 'SkyPro', 'zip-code': ''}

with allure.step ("поле Zip code подсветить красным"):
    alert_danger_color = "rgba(248, 215, 218, 1)"
with allure.step ("остальные поля подсветить зеленым"):
    alert_success_color = "rgba(209, 231, 221, 1)"

fields_to_test_success = [
    key for key in values_dict.keys() if key != 'zip-code']

@pytest.fixture(scope="function")
def detup_from(chrome_browser):
    main_page = MainPage(chrome_browser)
    main_page.open()
    main_page.fill_fields(values_dict)
    main_page.click_submit()
    return main_page

def test_alert_color(setup_from):
    color_zip = setup_from.find_element_property("zip-code")
    assert color_zip == alert_danger_color

@pytest.mark.parametrize('selector', fields_to_test_success)
def test_success_color(setup_from, selector):
    color = setup_from.find_element_property(selector)
    assert color == alert_success_color
    