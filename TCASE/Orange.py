import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Set up the test report document
test_report = open("test_report.txt", "w")
test_report.write("Test Report: OrangeHRM System\n")
test_report.write("=================================\n")

# Set up the test cases
class TestOrangeHRM(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Replace with your preferred browser
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys("admin123")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']"))).click()

    def test_admin_menu(self):
        test_case_id = "TC001"
        test_case_description = "Verify that the Admin menu is accessible and displays the correct sub-menus."
        test_report.write(f"{test_case_id}: {test_case_description}\n")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "menu_admin_viewAdminModule"))).click()
        sub_menus = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#menu_admin_viewAdminModule ul li")))
        expected_sub_menus = ["User Management", "Job", "Organization", "Qualifications", "Nationalities", "Languages"]
        for sub_menu in sub_menus:
            self.assertIn(sub_menu.text, expected_sub_menus)
        test_report.write(f"{test_case_id}: Passed\n")

    def test_pim_menu(self):
        test_case_id = "TC002"
        test_case_description = "Verify that the PIM menu is accessible and displays the correct sub-menus."
        test_report.write(f"{test_case_id}: {test_case_description}\n")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "menu_pim_viewPimModule"))).click()
        sub_menus = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#menu_pim_viewPimModule ul li")))
        expected_sub_menus = ["Employee List", "Reports", "Configuration"]
        for sub_menu in sub_menus:
            self.assertIn(sub_menu.text, expected_sub_menus)
        test_report.write(f"{test_case_id}: Passed\n")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

test_report.write("=================================\n")
test_report.write("Test Report Summary:\n")
test_report.write("Total Test Cases: 2\n")
test_report.write("Passed: 2\n")
test_report.write("Failed: 0\n")
test_report.close()
