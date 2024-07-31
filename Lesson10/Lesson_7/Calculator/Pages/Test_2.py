from Lesson_7.Calculator.Pages.CalcPage import CalcPage

@allure.title("Автотест на калькулятор")
@allure.description("Проверка результата")    
@allure.severity("critical")
def test_calculator(chrome_browser):
    with allure.step ("обозначение параметров"):
        delay = 45
        result = 15
        keys_press = '7+8='
        
    calc = CalcPage(chrome_browser)
    with allure.step ("открытие калькулятора"): 
        calc.open()
        calc.set_delay(delay)
        calc.input_text(keys_press)
        calc.wait_result(delay, result)

    with allure.step("проверка результата"):
        assert calc.result_text() == str(result)
