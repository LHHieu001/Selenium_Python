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
        self.driver.get("http://localhost/blog_git/personalBlog/admin/update_profile.php")

    def test_database(self):
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="blog_db"
        )

        self.cursor = self.db.cursor()

        before_name = 'JaneDoe'
        query = "SELECT id FROM admin WHERE name = %s"
        self.cursor.execute(query, (before_name,))
        author_id = self.cursor.fetchone()[0]

        query_pass = "SELECT password FROM admin WHERE id = %s"
        self.cursor.execute(query_pass, (author_id,))
        before_pass = self.cursor.fetchone()[0]

        self.db.close()
        self.cursor.close()


        name = self.driver.find_element(By.NAME, "name")
        name.send_keys("HoangTheAuthor")

        old_password = self.driver.find_element(By.NAME, "old_pass")
        old_password.send_keys("StrongPassword!456")

        new_password = self.driver.find_element(By.NAME, "new_pass")
        new_password.send_keys("WeakPassword!123")

        con_password = self.driver.find_element(By.NAME, "confirm_pass")
        con_password.send_keys("WeakPassword!123")

        self.driver.find_element(By.NAME, "submit").click()


        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="blog_db"
        )

        self.cursor = self.db.cursor()

        query_name = "SELECT name FROM admin WHERE id = %s"
        self.cursor.execute(query_name, (author_id,))
        after_name = self.cursor.fetchone()[0]

        self.cursor.execute(query_pass, (author_id,))
        after_pass = self.cursor.fetchone()[0]

        print('Pass:', before_pass, after_pass)
        print('Name:', before_name, after_name)

        self.assertEqual(before_name,after_name, "Test fail new author was updated")
        self.assertEqual(before_pass,after_pass,"Test fail new author was updated")

        self.db.close()
        self.cursor.close()

    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
