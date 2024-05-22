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
        self.driver.get("http://localhost/blog_git/personalBlog/admin/add_posts.php")

    def test_database(self):
        title = self.driver.find_element(By.NAME, "title")
        title.send_keys("My Post Title")

        content = self.driver.find_element(By.NAME, "content")
        content.send_keys("This is my post content")

        category = self.driver.find_element(By.NAME, "category")
        select_category = Select(category).select_by_value("lifestyle")

        file_input = self.driver.find_element(By.NAME, "image")
        image_path = r"C:\Users\lehoa\Downloads\download.jpg"
        file_input.send_keys(image_path)

        self.driver.find_element(By.NAME, "publish").click()

        self.driver.implicitly_wait(3)

        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="blog_db"
        )

        self.cursor = self.db.cursor()

        query = "SELECT * FROM posts WHERE title = 'My Post Title'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()

        self.assertIsNotNone(result, "Failed, No post found")

        self.db.close()
        self.cursor.close()

    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
