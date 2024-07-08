from selenium import webdriver
import time

def test_edit_timesheet():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    # Login first
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    
    time.sleep(2)  # Wait for page to load
    
    # Navigate to Time module
    driver.find_element_by_id("menu_time_viewTimeModule").click()
    
    time.sleep(2)  # Wait for Time page to load
    
    # Select the timesheet to edit
    driver.find_element_by_link_text("View Timesheets").click()
    
    time.sleep(2)  # Wait for Timesheets page to load
    
    driver.find_element_by_link_text("2024-07-10").click()  # Selecting a timesheet by date
    
    time.sleep(2)  # Wait for timesheet details page to load
    
    # Click on Edit button
    driver.find_element_by_id("btnEdit").click()
    
    # Edit details
    driver.find_element_by_id("initialRows_0_projectName").send_keys("Updated Project Name")
    driver.find_element_by_id("btnSave").click()
    
    time.sleep(2)  # Wait for saving
    
    # Verify details are updated
    assert "Updated Project Name" in driver.page_source
    
    driver.quit()

if __name__ == "__main__":
    test_edit_timesheet()
