from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_admin_navigation():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    try:
        # Wait until username field is visible and interactable
        username_field = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "txtUsername"))
        )
        username_field.send_keys("Admin")
        
        password_field = driver.find_element(By.ID, "txtPassword")
        password_field.send_keys("admin123")
        
        login_button = driver.find_element(By.ID, "btnLogin")
        login_button.click()
        
        time.sleep(2)  # Wait for page to load
        
        # Navigate to Admin module
        admin_menu = driver.find_element(By.ID, "menu_admin_viewAdminModule")
        admin_menu.click()
        
        time.sleep(2)  # Wait for Admin page to load
        
        # Verify the Admin page is loaded
        assert "viewSystemUsers" in driver.current_url
    
    finally:
        driver.quit()

if __name__ == "__main__":
    test_admin_navigation()
