from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def test_access_dashboard():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    try:
        # Wait until username field is visible and interactable
        username_field = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, "txtUsername"))
        )
        username_field.send_keys("Admin")
        
        password_field = driver.find_element(By.ID, "txtPassword")
        password_field.send_keys("admin123")
        
        login_button = driver.find_element(By.ID, "btnLogin")
        login_button.click()
        
        # Wait until Dashboard menu is visible and interactable
        dashboard_menu = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, "menu_dashboard_index"))
        )
        dashboard_menu.click()
        
        # Wait until Dashboard page is loaded
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "dashboard-content"))
        )
        
        # Verify the Dashboard page is loaded
        assert "Dashboard" in driver.page_source
    
    except TimeoutException as ex:
        print("Timeout waiting for element:", ex)
    
    except NoSuchElementException as ex:
        print("Element not found:", ex)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    test_access_dashboard()
