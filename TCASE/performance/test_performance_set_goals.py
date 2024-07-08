from selenium import webdriver
import time

def test_set_performance_goals():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    # Login first
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    
    time.sleep(2)  # Wait for page to load
    
    # Navigate to Performance module
    driver.find_element_by_id("menu__Performance").click()
    
    time.sleep(2)  # Wait for Performance page to load
    
    # Click on Manage Reviews
    driver.find_element_by_id("menu_performance_viewManageReviews").click()
    
    time.sleep(2)  # Wait for Manage Reviews page to load
    
    # Click on Add
    driver.find_element_by_id("btnAdd").click()
    
    time.sleep(2)  # Wait for Add Review page to load
    
    # Fill in review details
    driver.find_element_by_id("performanceReview360SearchForm_employeeName").send_keys("John Doe")
    driver.find_element_by_id("saveReviewBtn").click()
    
    time.sleep(2)  # Wait for saving
    
    # Verify review is added
    assert "Performance Review" in driver.page_source
    
    driver.quit()

if __name__ == "__main__":
    test_set_performance_goals()
