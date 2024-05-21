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
        self.driver.get("http://localhost/blog_git/personalBlog")

    def test_database(self):

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="blog_db"
        )

        self.cursor = self.db.cursor()

        initial_query = "SELECT COUNT(*) FROM dislikes"
        self.cursor.execute(initial_query)
        initial_count = self.cursor.fetchone()[0]

        #Like
        el = self.driver.find_element(By.NAME, "dislike_post")
        self.driver.execute_script("arguments[0].click();", el)
        self.driver.implicitly_wait(2)
        time.sleep(1)

        self.cursor.execute(initial_query)
        updated_count = self.cursor.fetchone()[0]

        self.assertNotEqual(updated_count, initial_count + 1, "disLike count updated even not login.")

    def Teardown(self):
        self.db.close()
        self.cursor.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
