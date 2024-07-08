from selenium import webdriver
import time

def test_post_buzz():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    # Login first
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    
    time.sleep(2)  # Wait for page to load
    
    # Navigate to Buzz
    driver.find_element_by_id("menu_buzz_viewBuzz").click()
    
    time.sleep(2)  # Wait for Buzz page to load
    
    # Post a buzz
    driver.find_element_by_id("createPost_content").send_keys("This is a test buzz post.")
    driver.find_element_by_id("postSubmitBtn").click()
    
    time.sleep(2)  # Wait for post to be submitted
    
    # Verify the post is submitted
    assert "This is a test buzz post." in driver.page_source
    
    driver.quit()

if __name__ == "__main__":
    test_post_buzz()
