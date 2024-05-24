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
        self.driver.get("http://localhost/blog_git/personalBlog/update.php")

    def test_UserUpdate_Update(self):

        email = self.driver.find_element(By.NAME, "email")
        email.clear()
        email.send_keys("lehoanghieu1.com")

        curpassword = self.driver.find_element(By.NAME, "old_pass")
        curpassword.send_keys("#ID12345678")

        submit = self.driver.find_element(By.NAME, "submit")
        submit.click()

        self.driver.implicitly_wait(3)

        validation_message = self.driver.execute_script("return arguments[0].validationMessage;", email)
        self.assertIsNotNone(validation_message, "No validation message")



    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()