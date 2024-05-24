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

    def test_Userbtn(self):
        el = self.driver.find_element(By.PARTIAL_LINK_TEXT, "User")
        el.click()

        expected_url = "http://localhost/blog_git/personalBlog/login.php"
        self.assertEqual(self.driver.current_url, expected_url, "Test Failed")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()