from selenium import webdriver
import time

def test_dashboard_widgets():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    # Login first
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()
    
    time.sleep(2)  # Wait for page to load
    
    # Navigate to Dashboard
    driver.find_element_by_id("menu_dashboard_index").click()
    
    time.sleep(2)  # Wait for Dashboard page to load
    
    # Verify the Dashboard widgets are displayed
    widgets = ["dashboard__employeeDistribution", "panel_wrapper_1", "panel_wrapper_2", "panel_wrapper_3"]
    for widget in widgets:
        assert driver.find_element_by_id(widget).is_displayed()
    
    driver.quit()

if __name__ == "__main__":
    test_dashboard_widgets()
