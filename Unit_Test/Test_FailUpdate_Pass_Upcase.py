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

        curpassword = self.driver.find_element(By.NAME, "old_pass")
        curpassword.send_keys("#SN120903")

        newpassword = self.driver.find_element(By.NAME, "new_pass")
        newpassword.send_keys("#sn13052003")

        cpassword = self.driver.find_element(By.NAME, "confirm_pass")
        cpassword.send_keys("#sn13052003")

        submit = self.driver.find_element(By.NAME, "submit")
        submit.click()

        self.driver.implicitly_wait(3)

        message = self.driver.find_element(By.CLASS_NAME, "message")
        assert "Password must contain at least one uppercase letter, one number, and one special character!" in message.text
        print("Test Successful")


    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()