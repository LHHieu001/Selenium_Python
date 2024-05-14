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

    def test_UserCommentsBtn(self):

        el = self.driver.find_element(By.NAME, "UserComments")
        el.click()

        self.driver.implicitly_wait(3)

        expected_url = "http://localhost/blog_git/personalBlog/user_comments.php"
        self.assertEqual(self.driver.current_url, expected_url, "Test was not successful. URL did not change as expected.")

    #def test_UserCommentsBtn2_Delete(self):



    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()