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
        name.send_keys("HoangHieuTheHuman")

        email = self.driver.find_element(By.NAME, "email")
        email.send_keys("HieuHuman@gmail.com")

        password = self.driver.find_element(By.NAME, "pass")
        password.send_keys("12092003A@")

        cpassword = self.driver.find_element(By.NAME, "cpass")
        cpassword.send_keys("12092003A@")

        self.driver.implicitly_wait(3)

        submit = self.driver.find_element(By.NAME, "submit")
        submit.click()

        expected_url = "http://localhost/blog_git/personalBlog/index.php"
        self.assertEqual(self.driver.current_url, expected_url,
                         "Registration was not successful. URL did not change as expected.")

    def test_database(self):

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="blog_db"
        )

        self.cursor = self.db.cursor()

        self.cursor.execute("SELECT * FROM users WHERE name ='HoangHieuTheHuman'")
        result = self.cursor.fetchone()

        self.assertIsNotNone(result, "Login failed or database entry does not exist.")

        expected_username = "HoangHieuTheHuman"
        self.assertEqual(result[1], expected_username, f"Expected username {expected_username} but got {result[1]}")

    def Teardown(self):
        self.db.close()
        self.cursor.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
