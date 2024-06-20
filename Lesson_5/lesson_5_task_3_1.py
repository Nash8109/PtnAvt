from time import sleep
from selenium import webdriver

#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome()

# Запустить сайт
driver.get("http://uitestingplayground.com/classattr/")
sleep(3)

# Нахождение и нажатие на кнопку, обработка всплывающего окна с предупреждением. Повторить действия три раза
for _ in range(3):
    button = driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    sleep(1)
    driver.switch_to.alert.accept()
    sleep(2)

sleep(2)

driver.quit()