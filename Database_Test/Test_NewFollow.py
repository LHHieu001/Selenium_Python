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

    def __init__(self, *args, **kwargs):
        super(MyTest, self).__init__(*args, **kwargs)
        self.driver = webdriver.Edge(options=c_options)
        self.driver.get("http://localhost/blog_git/personalBlog/login.php")

    def test_database(self):

        email = self.driver.find_element(By.NAME, "email")
        email.send_keys("HieuHuman@gmail.com")

        password = self.driver.find_element(By.NAME, "pass")
        password.send_keys("12092003A@")

        self.driver.implicitly_wait(2)

        submit = self.driver.find_element(By.NAME, "submit")
        submit.click()

        el = self.driver.find_element(By.CLASS_NAME, "fa-plus-square")
        self.driver.execute_script("arguments[0].click();", el)
        self.driver.implicitly_wait(2)

        time.sleep(2)

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="blog_db"
        )

        self.cursor = self.db.cursor()

        email = 'HieuHuman@gmail.com'

        query = "SELECT id FROM users WHERE email = %s"
        self.cursor.execute(query, (email,))
        value = self.cursor.fetchone()

        if value:
            user_id = value[0]

            query_1 = "SELECT * FROM follows WHERE admin_id = %s AND user_id = %s"
            self.cursor.execute(query_1, ('3', user_id))
            result = self.cursor.fetchone()

            self.assertIsNotNone(result, "Test Failed: No follow found for the given post_id and user_id.")
        else:
            self.fail("Test Failed: User with the given email not found.")

        self.db.close()
        self.cursor.close()

    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
