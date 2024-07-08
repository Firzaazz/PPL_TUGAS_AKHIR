from selenium import webdriver
import time

def test_schedule_interview():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    # Login first
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    
    time.sleep(2)  # Wait for page to load
    
    # Navigate to Recruitment module
    driver.find_element_by_id("menu_recruitment_viewRecruitmentModule").click()
    
    time.sleep(2)  # Wait for Recruitment page to load
    
    # Click on a candidate to schedule an interview
    driver.find_element_by_link_text("Jane Smith").click()
    
    time.sleep(2)  # Wait for candidate details page to load
    
    # Click on Schedule Interview
    driver.find_element_by_id("btnSave").click()
    
    # Fill in interview details
    driver.find_element_by_id("interview_date").clear()
    driver.find_element_by_id("interview_date").send_keys("2024-07-20")
    driver.find_element_by_id("saveBtn").click()
    
    time.sleep(2)  # Wait for saving
    
    # Verify interview is scheduled
    assert "Interview Scheduled" in driver.page_source
    
    driver.quit()

if __name__ == "__main__":
    test_schedule_interview()
