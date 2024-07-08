from selenium import webdriver
import time

def test_search_directory():
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
    
    # Verify the search results
    assert "John Doe" in driver.page_source
    
    driver.quit()

if __name__ == "__main__":
    test_search_directory()
