import re
import unittest
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
        self.driver.get("http://localhost/blog_git/personalBlog/user_comments.php")

    def test_UserCommentAction(self):

        el = self.driver.find_element(By.NAME, "open_edit_box")
        el.click()
        self.driver.implicitly_wait(2)

        editcomment = self.driver.find_element(By.NAME, "comment_edit_box")
        editcomment.clear()
        editcomment.send_keys("Excellent")

        confirmedit = self.driver.find_element(By.NAME, "edit_comment")
        confirmedit.click()

        #alert = self.driver.switch_to.alert
        #alert.accept()

        message = self.driver.find_element(By.CLASS_NAME, "message")
        assert "your comment edited successfully!" in message.text
        print("test pass")


    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()