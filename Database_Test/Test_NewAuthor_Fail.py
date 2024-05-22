import time
import unittest
import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

debugger_address = 'localhost:8989'

c_options = Options()
c_options.add_experimental_option("debuggerAddress", "localhost:8989")


class MyTest(unittest.TestCase):

    #Log in first
    def __init__(self, *args, **kwargs):
        super(MyTest, self).__init__(*args, **kwargs)
        self.driver = webdriver.Edge(options=c_options)
        self.driver.get("http://localhost/blog_git/personalBlog/admin/register_admin_2.php")

    def test_database(self):

        username = self.driver.find_element(By.NAME, "name")
        username.send_keys("JaneDoe")

        password = self.driver.find_element(By.NAME, "pass")
        password.send_keys("Strong123")

        cpassword = self.driver.find_element(By.NAME, "cpass")
        cpassword.send_keys("Strong123")

        self.driver.find_element(By.NAME, "submit").click()

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="blog_db"
        )

        self.cursor = self.db.cursor()

        name = 'JaneDoe'
        query = "SELECT * FROM admin WHERE name = %s"
        self.cursor.execute(query, (name,))
        value = self.cursor.fetchone()

        self.assertIsNone(value, "Test fail new author was created")

        self.db.close()
        self.cursor.close()

    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
