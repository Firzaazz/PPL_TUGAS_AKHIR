from selenium import webdriver
import time

def test_add_employee():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    # Login first
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    
    time.sleep(2)  # Wait for page to load
    
    # Navigate to PIM module
    driver.find_element_by_id("menu_pim_viewPimModule").click()
    
    time.sleep(2)  # Wait for PIM page to load
    
    # Click on Add Employee
    driver.find_element_by_id("menu_pim_addEmployee").click()
    
    time.sleep(2)  # Wait for Add Employee page to load
    
    # Fill in employee details
    driver.find_element_by_id("firstName").send_keys("John")
    driver.find_element_by_id("lastName").send_keys("Doe")
    driver.find_element_by_id("btnSave").click()
    
    time.sleep(2)  # Wait for saving
    
    # Verify employee is added
    assert "personalDetails" in driver.current_url
    
    driver.quit()

if __name__ == "__main__":
    test_add_employee()
