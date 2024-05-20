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
        self.driver.get("http://localhost/blog_git/personalBlog/")

    def test_UserCommentAction(self):


        el = self.driver.find_element(By.CLASS_NAME, "fa-comment")
        self.driver.execute_script("arguments[0].click();", el)
        self.driver.implicitly_wait(4)

        expected_url_pattern = r"http://localhost/blog_git/personalBlog/view_post.php\?post_id=\d+"
        current_url = self.driver.current_url
        self.assertTrue(re.search(expected_url_pattern, current_url),
                        "Test was not successful. URL did not match the expected pattern.")

    def test_UserCommentAction_2_write(self):
        writecomment = self.driver.find_element(By.CLASS_NAME, "comment-box")
        writecomment.send_keys("Nice")

        addcomment = self.driver.find_element(By.NAME, "add_comment")
        self.driver.execute_script("arguments[0].click();", addcomment)
        self.driver.implicitly_wait(4)

        message = self.driver.find_element(By.CLASS_NAME, "message")
        assert "comment already added!" in message.text
        print("Test pass")


    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()