from selenium import webdriver
import time

def test_update_personal_details():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    # Login first
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    
    time.sleep(2)  # Wait for page to load
    
    # Navigate to My Info module
    driver.find_element_by_id("menu_pim_viewMyDetails").click()
    
    time.sleep(2)  # Wait for My Info page to load
    
    # Click on Edit button
    driver.find_element_by_id("btnSave").click()
    
    # Update personal details
    driver.find_element_by_id("personal_txtEmpNickName").send_keys("Nick")
    driver.find_element_by_id("btnSave").click()
    
    time.sleep(2)  # Wait for saving
    
    # Verify details are updated
    assert "Nick" in driver.find_element_by_id("personal_txtEmpNickName").get_attribute("value")
    
    driver.quit()

if __name__ == "__main__":
    test_update_personal_details()
