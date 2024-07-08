from selenium import webdriver
import time

def test_add_candidate():
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
    
    # Click on Add Candidate
    driver.find_element_by_id("btnAdd").click()
    
    time.sleep(2)  # Wait for Add Candidate page to load
    
    # Fill in candidate details
    driver.find_element_by_id("addCandidate_firstName").send_keys("Jane")
    driver.find_element_by_id("addCandidate_lastName").send_keys("Smith")
    driver.find_element_by_id("addCandidate_email").send_keys("jane.smith@example.com")
    driver.find_element_by_id("btnSave").click()
    
    time.sleep(2)  # Wait for saving
    
    # Verify candidate is added
    assert "Candidate" in driver.page_source
    
    driver.quit()

if __name__ == "__main__":
    test_add_candidate()
