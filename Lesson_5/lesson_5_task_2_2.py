from time import sleep
from selenium import webdriver

#from selenium.webdriver.firefox.service import Service as FirefoxService
#from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# Запустить сайт
count = 0
driver.get(" http://uitestingplayground.com/dynamicid/")
sleep(3)

# Кликнуть на синюю кнопку и повторить нажатие три раза
for _ in range(3):
    button = driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']").click()
    sleep(1)
    count = count + 1
    sleep(1)
    print("Нажатие №", count)

# Закрыть браузер
driver.quit()