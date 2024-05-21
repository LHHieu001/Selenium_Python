import unittest
import mysql.connector
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

    def test_CreateUser(self):

        name = self.driver.find_element(By.NAME, "name")
        name.send_keys("")

        email = self.driver.find_element(By.NAME, "email")
        email.send_keys("HieuHuman@gmail.com")

        password = self.driver.find_element(By.NAME, "pass")
        password.send_keys("12092003A@")

        cpassword = self.driver.find_element(By.NAME, "cpass")
        cpassword.send_keys("12092003A@")

        self.driver.implicitly_wait(3)

        submit = self.driver.find_element(By.NAME, "submit")
        submit.click()

    def test_database(self):

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="blog_db"
        )

        self.cursor = self.db.cursor()

        self.cursor.execute("SELECT * FROM users WHERE email ='HieuHuman@gmail.com'")
        result = self.cursor.fetchone()

        self.assertIsNone(result, "Test Failed, The user account got created.")

    def Teardown(self):
        self.db.close()
        self.cursor.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
