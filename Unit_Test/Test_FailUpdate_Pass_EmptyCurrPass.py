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


        newpassword = self.driver.find_element(By.NAME, "new_pass")
        newpassword.send_keys("#SN15092005")

        cpassword = self.driver.find_element(By.NAME, "confirm_pass")
        cpassword.send_keys("#SN15092005")

        submit = self.driver.find_element(By.NAME, "submit")
        submit.click()

        self.driver.implicitly_wait(3)

        message = self.driver.find_element(By.CLASS_NAME, "message")
        assert "Please enter your current password!" in message.text
        print("Test Successful")


    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()