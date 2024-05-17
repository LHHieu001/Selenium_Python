import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

debugger_address = 'localhost:8989'

c_options = Options()
c_options.add_experimental_option("debuggerAddress", "localhost:8989")


class MyTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(MyTest, self).__init__(*args, **kwargs)
        self.driver = webdriver.Edge(options=c_options)
        self.driver.get("http://localhost/blog_git/personalBlog/login.php")

    def test_UserLogin(self):

        email = self.driver.find_element(By.NAME, "email")
        email.send_keys("")

        password = self.driver.find_element(By.NAME, "pass")
        password.send_keys("12092003A@")

        self.driver.implicitly_wait(3)

        submit = self.driver.find_element(By.NAME, "submit")
        submit.click()


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()