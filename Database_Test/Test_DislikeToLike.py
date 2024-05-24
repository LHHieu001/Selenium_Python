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
        self.driver.get("http://localhost/blog_git/personalBlog/user_dislikes.php")

    def test_login(self):

        el = self.driver.find_element(By.NAME, "like_post")
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

            query_1 = "SELECT * FROM likes WHERE post_id = %s AND user_id = %s"
            self.cursor.execute(query_1, ('1', user_id))
            result_1 = self.cursor.fetchone()

            query_2 = "SELECT * FROM dislikes WHERE post_id = %s AND user_id = %s"
            self.cursor.execute(query_2, ('1', user_id))
            result_2 = self.cursor.fetchone()

            self.assertIsNotNone(result_1, "Test Failed: Like not found for the given post_id and user_id.")
            self.assertIsNone(result_2, "Test Failed: DisLike found for the given post_id and user_id.")
        else:
            self.fail("Test Failed: User with the given email not found.")

        self.db.close()
        self.cursor.close()

    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
