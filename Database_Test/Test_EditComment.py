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
        self.driver.get("http://localhost/blog_git/personalBlog/user_comments.php")

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

        query = "SELECT comment FROM comments WHERE  post_id = %s AND user_id = %s"
        self.cursor.execute(query, ('2', user_id))
        before_comment = self.cursor.fetchone()[0]
        print(before_comment)

        self.db.close()
        self.cursor.close()

        el = self.driver.find_element(By.NAME, "open_edit_box")
        el.click()
        self.driver.implicitly_wait(2)

        editcomment = self.driver.find_element(By.NAME, "comment_edit_box")
        editcomment.clear()
        editcomment.send_keys("Very Nice")

        confirmedit = self.driver.find_element(By.NAME, "edit_comment")
        confirmedit.click()
        self.driver.implicitly_wait(5)
        time.sleep(2)

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="blog_db"
        )

        self.cursor = self.db.cursor()

        self.cursor.execute(query, ('2', user_id))
        after_comment = self.cursor.fetchone()[0]
        print(after_comment)

        self.assertNotEqual(before_comment, after_comment, "Database didn't update")

        self.db.close()
        self.cursor.close()

    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
