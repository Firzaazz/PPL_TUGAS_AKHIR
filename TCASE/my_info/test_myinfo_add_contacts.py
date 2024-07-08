from selenium import webdriver
import time

def test_add_contact_details():
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
    
    # Click on Contact Details
    driver.find_element_by_link_text("Contact Details").click()
    
    time.sleep(2)  # Wait for Contact Details page to load
    
    # Click on Edit button
    driver.find_element_by_id("btnSave").click()
    
    # Add contact details
    driver.find_element_by_id("contact_street1").send_keys("123 Main St")
    driver.find_element_by_id("contact_city").send_keys("New York")
    driver.find_element_by_id("contact_province").send_keys("NY")
    driver.find_element_by_id("contact_emp_mobile").send_keys("1234567890")
    driver.find_element_by_id("btnSave").click()
    
    time.sleep(2)  # Wait for saving
    
    # Verify contact details are updated
    assert "123 Main St" in driver.find_element_by_id("contact_street1").get_attribute("value")
    
    driver.quit()

if __name__ == "__main__":
    test_add_contact_details()
