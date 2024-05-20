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
        self.driver.get("http://localhost/blog_git/personalBlog/user_follow.php")

    def test_UserFollowtn(self):

        el = self.driver.find_element(By.NAME, "follow_author")
        el.click()

        self.driver.implicitly_wait(3)

        message = self.driver.find_element(By.CLASS_NAME, "message")
        assert "removed from follows" in message.text
        print("Test Pass")


    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()