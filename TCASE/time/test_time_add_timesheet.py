from selenium import webdriver
import time

def test_add_timesheet():
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
    
    # Click on Add Timesheet
    driver.find_element_by_id("btnAddTimesheet").click()
    
    time.sleep(2)  # Wait for Add Timesheet page to load
    
    # Fill in timesheet details
    driver.find_element_by_id("time_date").clear()
    driver.find_element_by_id("time_date").send_keys("2024-07-10")
    driver.find_element_by_id("addTimesheetBtn").click()
    
    time.sleep(2)  # Wait for timesheet to be added
    
    # Verify timesheet is added
    assert "Timesheet for Week" in driver.page_source
    
    driver.quit()

if __name__ == "__main__":
    test_add_timesheet()
