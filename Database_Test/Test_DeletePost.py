import time
import unittest
import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.edge.options import Options

debugger_address = 'localhost:8989'

c_options = Options()
c_options.add_experimental_option("debuggerAddress", "localhost:8989")


class MyTest(unittest.TestCase):

    #Log in first
    def __init__(self, *args, **kwargs):
        super(MyTest, self).__init__(*args, **kwargs)
        self.driver = webdriver.Edge(options=c_options)
        self.driver.get("http://localhost/blog_git/personalBlog/admin/edit_post.php?id=3")

    def test_database(self):

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="blog_db"
        )

        self.cursor = self.db.cursor()

        query_likes = "SELECT COUNT(*) FROM likes WHERE post_id = 3;"
        self.cursor.execute(query_likes)
        before_likes_count = self.cursor.fetchone()[0]

        query_dislikes = "SELECT COUNT(*) FROM dislikes WHERE post_id = 3;"
        self.cursor.execute(query_dislikes)
        before_dislikes_count = self.cursor.fetchone()[0]

        query_comments = "SELECT COUNT(*) FROM comments WHERE post_id = 3;"
        self.cursor.execute(query_comments)
        before_comments_count = self.cursor.fetchone()[0]

        self.cursor.close()
        self.db.close()


        delete = self.driver.find_element(By.NAME, "delete_post")
        delete.click()
        self.driver.implicitly_wait(2)
        time.sleep(1)


        self.driver.implicitly_wait(3)

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="blog_db"
        )

        self.cursor = self.db.cursor()

        self.cursor.execute(query_likes)
        after_likes_count = self.cursor.fetchone()[0]

        self.cursor.execute(query_dislikes)
        after_dislikes_count = self.cursor.fetchone()[0]

        self.cursor.execute(query_comments)
        after_comments_count = self.cursor.fetchone()[0]

        print("likes: ", before_likes_count,after_likes_count)
        print("dislikes: ",before_dislikes_count,after_dislikes_count)
        print("comments: ",before_comments_count,after_comments_count)

        self.assertNotEqual(before_likes_count,after_likes_count,"Test Failed")
        self.assertNotEqual(before_dislikes_count,after_dislikes_count,"Test Failed")
        self.assertNotEqual(before_comments_count,after_comments_count,"Test Failed")

        self.db.close()
        self.cursor.close()

    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
