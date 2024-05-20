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
    
    def test_SearchBar(self):
        el = self.driver.find_element(By.NAME, "search_box")
        el.send_keys("Test")
        el.submit()

        title = self.driver.find_element(By.CLASS_NAME, "post-title")
        assert "Test" in title.text
        print("Test Successful")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()