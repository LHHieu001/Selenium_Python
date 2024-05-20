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

    def test_Authorbtn(self):
        el = self.driver.find_element(By.CLASS_NAME, "fa-moon")
        el.click()

        change = self.driver.find_element(By.TAG_NAME, "body")
        getclass = change.get_attribute("class")
        assert "dark-theme" or "" in getclass
        print("Test successful")

    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
