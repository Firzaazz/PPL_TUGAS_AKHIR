import unittest
from admin.test_admin_login import TestAdminLogin
from admin.test_admin_navigation import TestAdminNavigation
from pim.test_add_employee import TestAddEmployee
from pim.test_edit_employee import TestEditEmployee
# Import other test classes similarly

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestAdminLogin))
    test_suite.addTest(unittest.makeSuite(TestAdminNavigation))
    test_suite.addTest(unittest.makeSuite(TestAddEmployee))
    test_suite.addTest(unittest.makeSuite(TestEditEmployee))
    # Add other tests to the suite
    
    return test_suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
