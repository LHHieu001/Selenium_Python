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

    def test_UserUpdateProfilebtn(self):

        el = self.driver.find_element(By.NAME, "UpdateProfile")
        el.click()

        self.driver.implicitly_wait(3)


        expected_url = "http://localhost/blog_git/personalBlog/update.php"
        self.assertEqual(self.driver.current_url, expected_url, "Action was not successful. URL did not change as expected.")


    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()