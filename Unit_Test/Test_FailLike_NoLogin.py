import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

debugger_address = 'localhost:8989'

c_options = Options()
c_options.add_experimental_option("debuggerAddress", "localhost:8989")


class MyTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(MyTest, self).__init__(*args, **kwargs)
        self.driver = webdriver.Edge(options=c_options)
        self.driver.get("http://localhost/blog_git/personalBlog/")

    def test_UserLike(self):


        likepost = self.driver.find_element(By.NAME, "like_post")
        actions = ActionChains(self.driver)
        actions.move_to_element(likepost).perform()
        self.driver.execute_script("arguments[0].click()", likepost)
        self.driver.implicitly_wait(3)

        message = self.driver.find_element(By.CLASS_NAME, "message")
        assert "login" in message.text
        print("Test Successful")



    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()