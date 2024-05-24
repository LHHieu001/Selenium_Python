import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.wait import WebDriverWait

debugger_address = 'localhost:8989'

c_options = Options()
c_options.add_experimental_option("debuggerAddress", "localhost:8989")


class MyTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(MyTest, self).__init__(*args, **kwargs)
        self.driver = webdriver.Edge(options=c_options)
        self.driver.get("http://localhost/blog_git/personalBlog/")

    def test_User(self):
        el = self.driver.find_element(By.NAME, "UserLogout")
        el.click()

        alert = self.driver.switch_to.alert
        alert.accept()

        self.driver.implicitly_wait(3)

        expected_url = 'http://localhost/blog_git/personalBlog/index.php'
        self.assertEqual(self.driver.current_url, expected_url,"Test Failed")

        try:
            check = self.driver.find_element(By.NAME, 'UpdateProfile')
            self.assertIsNotNone(check, "User is logged out")
        except:
            print("Test success")


        #try:
        #    check = WebDriverWait(self.driver, 10).until(
        #        EC.presence_of_element_located((By.CLASS_NAME, "option-btn"))
        #    )
        #    self.assertTrue(check.is_displayed())
        #except:
        #    self.fail("Button did not appear within the specified time")

        #check = self.driver.find_element(By.CSS_SELECTOR, ".name p")
        #assert "Login as:" in check.text
        #print("User logged out")

    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
