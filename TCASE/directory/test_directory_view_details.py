from selenium import webdriver
import time

def test_view_directory_details():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    # Login first
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    
    time.sleep(2)  # Wait for page to load
    
    # Navigate to Directory
    driver.find_element_by_id("menu_directory_viewDirectory").click()
    
    time.sleep(2)  # Wait for Directory page to load
    
    # Search for an employee
    driver.find_element_by_id("searchDirectory_emp_name_empName").send_keys("John Doe")
    driver.find_element_by_id("searchBtn").click()
    
    time.sleep(2)  # Wait for search results
    
    # Click on the employee name to view details
    driver.find_element_by_link_text("John Doe").click()
    
    time.sleep(2)  # Wait for employee details page to load
    
    # Verify the employee details are displayed
    assert "Personal Details" in driver.page_source
    assert driver.find_element_by_id("personal_txtEmpFirstName").is_displayed()
    assert driver.find_element_by_id("personal_txtEmpLastName").is_displayed()
    
    driver.quit()

if __name__ == "__main__":
    test_view_directory_details()
