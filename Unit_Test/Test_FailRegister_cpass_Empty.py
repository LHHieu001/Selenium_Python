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
        self.driver.get("http://localhost/blog_git/personalBlog/register.php")

    def test_UserReg(self):

        name = self.driver.find_element(By.NAME, "name")
        name.send_keys("HieuDFG")

        email = self.driver.find_element(By.NAME, "email")
        email.send_keys("LeHoangHieu0234@gmail.com")

        password = self.driver.find_element(By.NAME, "pass")
        password.send_keys("12092003A@")

        cpassword = self.driver.find_element(By.NAME, "cpass")
        cpassword.send_keys("")

        self.driver.implicitly_wait(3)

        submit = self.driver.find_element(By.NAME, "submit")
        submit.click()

        validation_message = self.driver.execute_script("return arguments[0].validationMessage;", cpassword)
        assert "Please fill out this field." in validation_message
        print("Test Successful")

    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()