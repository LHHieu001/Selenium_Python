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

    def test_Themebtn(self):

        footer = self.driver.find_element(By.CLASS_NAME, 'footer')
        before_color = footer.value_of_css_property('background-color')

        el = self.driver.find_element(By.ID, "theme-button")
        el.click()
        self.driver.implicitly_wait(2)

        after_color = footer.value_of_css_property('background-color')

        self.assertNotEqual(before_color, after_color, "Theme didn't change")

    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
