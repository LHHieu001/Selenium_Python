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

    def test_UserFollowAction(self):


        el = self.driver.find_element(By.CLASS_NAME, "fa-comment")
        self.driver.execute_script("arguments[0].click();", el)
        self.driver.implicitly_wait(4)

    def test_UserFollowAction2_addcomment(self):
        writecomment = self.driver.find_element(By.CLASS_NAME, "comment-box")
        writecomment.send_keys("Nice")

        addcomment = self.driver.find_element(By.NAME, "add_comment")
        addcomment.click()
        self.driver.implicitly_wait(4)

    def test_UserFollowAction3_deletecomment(self):

        deletecomment = self.driver.find_element(By.NAME, "delete_comment")
        self.driver.execute_script("arguments[0].click();", deletecomment)
        self.driver.implicitly_wait(3)

        alert = self.driver.switch_to.alert
        alert.accept()





        #expected_url = "http://localhost/blog_git/personalBlog/user_follow.php"
        #self.assertEqual(self.driver.current_url, expected_url, "Test was not successful. URL did not change as expected.")

    def Teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()