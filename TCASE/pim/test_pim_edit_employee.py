from selenium import webdriver
import time

def test_edit_employee():
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
    
    # Search for employee
    driver.find_element_by_id("empsearch_employee_name_empName").send_keys("John Doe")
    driver.find_element_by_id("searchBtn").click()
    
    time.sleep(2)  # Wait for search results
    
    # Click on the employee name
    driver.find_element_by_link_text("John Doe").click()
    
    time.sleep(2)  # Wait for employee details page to load
    
    # Click on Edit button
    driver.find_element_by_id("btnSave").click()
    
    # Edit details
    driver.find_element_by_id("personal_txtEmpNickName").send_keys("Johnny")
    driver.find_element_by_id("btnSave").click()
    
    time.sleep(2)  # Wait for saving
    
    # Verify details are updated
    assert "Johnny" in driver.find_element_by_id("personal_txtEmpNickName").get_attribute("value")
    
    driver.quit()

if __name__ == "__main__":
    test_edit_employee()
