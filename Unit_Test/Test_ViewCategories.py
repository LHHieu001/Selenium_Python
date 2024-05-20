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

    def test_ViewCategories(self):
        el = self.driver.find_element(By.NAME, "ViewAllCates")
        el.click()

        expected_url = "http://localhost/blog_git/personalBlog/all_category.php"
        self.assertEqual(self.driver.current_url, expected_url,
                         "Test was not successful. URL did not change as expected.")

    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
