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
        self.driver.get("http://localhost/blog_git/personalBlog/update.php")

    def test_database(self):

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
        user_id = value[0]

        query = "SELECT email FROM users WHERE id = %s"
        self.cursor.execute(query, (user_id,))
        before_email = self.cursor.fetchone()[0]
        print(before_email)

        self.db.close()
        self.cursor.close()

        email = self.driver.find_element(By.NAME, "email")
        email.clear()
        email.send_keys("HieuTheHuman@gmail.com")

        curpassword = self.driver.find_element(By.NAME, "old_pass")
        curpassword.send_keys("12092003A@")

        submit = self.driver.find_element(By.NAME, "submit")
        submit.click()

        self.driver.implicitly_wait(3)

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="blog_db"
        )

        self.cursor = self.db.cursor()

        self.cursor.execute(query, (user_id,))
        after_email = self.cursor.fetchone()[0]
        print(after_email)

        self.assertNotEqual(before_email, after_email, "Database didn't update")

        self.db.close()
        self.cursor.close()

    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
