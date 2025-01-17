from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service



def login_test():
    # Инициализация драйвера для браузера Chrome с опциями
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    try:
        driver.get('https://clientbase.pasv.us/v6/user/login')
        # time.sleep(1)

        username_field = driver.find_element(By.NAME, 'email')
        username_field.send_keys('test@gmail.com')
        time.sleep(1)

        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys('12345')
        time.sleep(1)

        # login_button = driver.find_element(By.CLASS_NAME, 'submit')
        login_button = driver.find_element(By.CSS_SELECTOR, '.btn-sign.btn.btn-primary')
        login_button.click()
        time.sleep(5)

        # Явное ожидание, пока элемент, указывающий на успешный логин, не станет видимым
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.dropdown-toggle.nav-link'))
        )
        time.sleep(2)

        userName = driver.find_element(By.CSS_SELECTOR, '.dropdown-toggle.nav-link').text
        if 'Test Test' in userName:
            print('Login test passed!')
        else:
            print('Login test failed!')
    except Exception as e:
        print('An error occurred during the login test:', e)
        time.sleep(5)
    finally:
        # Закрытие браузера
        driver.quit()

# Запуск теста
if __name__ == "__main__":
    login_test()
