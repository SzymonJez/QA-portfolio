# test_login_form.py
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Upewnij się, że masz zainstalowany chromedriver
driver.get("https://example.com/login")

# Znajdź pola formularza
driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
driver.find_element(By.NAME, "password").send_keys("Test1234!")

# Kliknij przycisk Zaloguj
driver.find_element(By.ID, "login-button").click()

# Sprawdź, czy użytkownik został przekierowany na dashboard
assert "dashboard" in driver.current_url

driver.quit()
