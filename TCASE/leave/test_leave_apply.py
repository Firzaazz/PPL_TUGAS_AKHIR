from selenium import webdriver
import time

def test_apply_leave():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    # Login first
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    
    time.sleep(2)  # Wait for page to load
    
    # Navigate to Leave module
    driver.find_element_by_id("menu_leave_viewLeaveModule").click()
    
    time.sleep(2)  # Wait for Leave page to load
    
    # Click on Apply
    driver.find_element_by_id("menu_leave_applyLeave").click()
    
    time.sleep(2)  # Wait for Apply Leave page to load
    
    # Fill in leave application
    driver.find_element_by_id("applyleave_txtLeaveType").send_keys("Annual Leave")
    driver.find_element_by_id("applyleave_txtFromDate").clear()
    driver.find_element_by_id("applyleave_txtFromDate").send_keys("2024-07-10")
    driver.find_element_by_id("applyleave_txtToDate").clear()
    driver.find_element_by_id("applyleave_txtToDate").send_keys("2024-07-15")
    driver.find_element_by_id("applyBtn").click()
    
    time.sleep(2)  # Wait for application to be submitted
    
    # Verify leave is applied
    assert "My Leave" in driver.current_url
    
    driver.quit()

if __name__ == "__main__":
    test_apply_leave()
