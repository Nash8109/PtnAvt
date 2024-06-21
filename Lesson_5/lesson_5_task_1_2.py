from time import sleep
from selenium import webdriver

#from selenium.webdriver.firefox.service import Service as FirefoxService
#from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

# Запустить сайт
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Пять раз кликнуть на кнопку Add Element
for _ in range(5):
    add_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']").click()
    sleep(1)

# Собрать со страницы список кнопок Delete  
add_buttons = driver.find_elements(By.CSS_SELECTOR, 'button.added-manually')

# Вывести на экран размер списка
print('Размер списка кнопок Delete в браузере Chrome составляет:', len(add_buttons))

sleep(3)

# Закрыть браузер
driver.quit()