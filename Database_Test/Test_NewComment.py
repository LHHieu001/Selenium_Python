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
        self.driver.get("http://localhost/blog_git/personalBlog/view_post.php?post_id=2")

    def test_database(self):

        writecomment = self.driver.find_element(By.CLASS_NAME, "comment-box")
        writecomment.send_keys("Good")

        addcomment = self.driver.find_element(By.NAME, "add_comment")
        self.driver.execute_script("arguments[0].click();", addcomment)
        self.driver.implicitly_wait(4)

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

            query_1 = "SELECT * FROM comments WHERE post_id = %s AND user_id = %s AND comment = %s"
            self.cursor.execute(query_1, ('2', user_id, 'Good'))
            result = self.cursor.fetchone()

            self.assertIsNotNone(result, "Test Failed: No comment found for the given post_id and user_id.")
        else:
            self.fail("Test Failed: User with the given email not found.")


        self.db.close()
        self.cursor.close()

    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
