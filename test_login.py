from selenium import webdriver
from selenium.webdriver.common.by import By 

def test_login(): 
    # --- run headless ------
    #options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    #driver = webdriver.Chrome(options=options)

    driver = webdriver.Chrome()
    driver.get("https://example.com/login")
    
    driver.find_element(By.NAME, "username").send_keys("testuser")
    driver.find_element(By.NAME, "password").send_keys("password123")
    driver.find_element(By.ID, "login-btn").click()
    
    assert "Dashboard" in driver.title 
    driver.quit() 
 
