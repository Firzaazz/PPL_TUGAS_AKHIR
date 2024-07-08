from selenium import webdriver
import time

def test_approve_leave():
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
    
    # Click on Leave List
    driver.find_element_by_id("menu_leave_viewLeaveList").click()
    
    time.sleep(2)  # Wait for Leave List page to load
    
    # Search for leave requests
    driver.find_element_by_id("leaveList_chkSearchFilter_checkboxgroup_allcheck").click()  # Select all statuses
    driver.find_element_by_id("btnSearch").click()
    
    time.sleep(2)  # Wait for search results
    
    # Select a leave request to approve
    driver.find_element_by_id("ohrmList_chkSelectRecord_1").click()  # Selecting the first record
    
    # Click on Approve
    driver.find_element_by_id("btnApprove").click()
    
    time.sleep(2)  # Wait for approval
    
    # Verify leave is approved
    assert "Successfully" in driver.page_source
    
    driver.quit()

if __name__ == "__main__":
    test_approve_leave()
