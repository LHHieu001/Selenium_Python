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
        email.send_keys("LeHoangHieu9903@gmail.com")

        password = self.driver.find_element(By.NAME, "pass")
        password.send_keys("12092003")

        self.driver.implicitly_wait(3)

        submit = self.driver.find_element(By.NAME, "submit")
        submit.click()

        expected_url = "http://localhost/blog_git/personalBlog/index.php"
        self.assertEqual(self.driver.current_url, expected_url, "Login was not successful. URL did not change as expected.")

    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()