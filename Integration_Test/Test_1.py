#Description:
#1. Log in as user
#2. Go to "Lastest Post"
#3. Like a post
#4. Add a comment
#5. Log out
#Result: Pass

import re
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

debugger_address = 'localhost:8989'

c_options = Options()
c_options.add_experimental_option("debuggerAddress", "localhost:8989")


class MyTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(MyTest, self).__init__(*args, **kwargs)
        self.driver = webdriver.Edge(options=c_options)
        self.driver.get("http://localhost/blog_git/personalBlog/")
        time.sleep(1)

    def test_1(self):

        #1.Log in
        login = self.driver.find_element(By.PARTIAL_LINK_TEXT, "User")
        login.click()
        self.driver.implicitly_wait(2)

        expected_url_1 = "http://localhost/blog_git/personalBlog/login.php"
        self.assertEqual(self.driver.current_url, expected_url_1, "Test was not successful. URL did not change.")
        time.sleep(2)

        email = self.driver.find_element(By.NAME, "email")
        email.send_keys("lehoanghieu120903@gmail.com")
        password = self.driver.find_element(By.NAME, "pass")
        password.send_keys("#SN120903")
        self.driver.implicitly_wait(2)
        time.sleep(2)

        submit = self.driver.find_element(By.NAME, "submit")
        submit.click()
        expected_url_2 = "http://localhost/blog_git/personalBlog/index.php"
        self.assertEqual(self.driver.current_url, expected_url_2,"Login was not successful. URL did not change.")

        #2.Go to "Lastest Post"
        postpage = self.driver.find_element(By.NAME, "ViewAllPosts")
        self.driver.execute_script("arguments[0].scrollIntoView();", postpage)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click()", postpage)
        self.driver.implicitly_wait(3)

        expected_url_3 = "http://localhost/blog_git/personalBlog/posts.php"
        self.assertEqual(self.driver.current_url, expected_url_3, "Login was not successful. URL did not change.")

        #3.Like a Post

        likepost = self.driver.find_element(By.NAME, "like_post")
        actions = ActionChains(self.driver)
        actions.move_to_element(likepost).perform()
        self.driver.implicitly_wait(3)
        self.driver.execute_script("arguments[0].click()", likepost)
        time.sleep(2)

        message = self.driver.find_element(By.CLASS_NAME, "message")
        assert "added to likes" in message.text
        print("Like test: pass")

        #numoflike = likepost.find_element(By.XPATH, '')
        #assert "1" in numoflike.text
        #print("Pass")


        #4.comment
        comment = self.driver.find_element(By.CLASS_NAME, "fa-comment")
        actions = ActionChains(self.driver)
        actions.move_to_element(comment).perform()
        self.driver.implicitly_wait(2)
        self.driver.execute_script("arguments[0].click()", comment)
        time.sleep(2)

        expected_url_pattern = r"http://localhost/blog_git/personalBlog/view_post.php\?post_id=\d+"
        current_url = self.driver.current_url
        self.assertTrue(re.search(expected_url_pattern, current_url),
                        "Login was not successful. URL did not match the expected pattern.")
        self.driver.implicitly_wait(2)


        writecomment = self.driver.find_element(By.CLASS_NAME, "comment-box")
        self.driver.execute_script("arguments[0].scrollIntoView();", writecomment)
        time.sleep(1)
        writecomment.send_keys("Rad")
        time.sleep(2)

        addcomment = self.driver.find_element(By.NAME, "add_comment")
        self.driver.execute_script("arguments[0].click()", addcomment)
        self.driver.implicitly_wait(4)
        time.sleep(1)

        message_comment = self.driver.find_element(By.CLASS_NAME, "message")
        assert "new comment added!" in message_comment.text
        print("comment added!")

        #5.Log out
        userbtn = self.driver.find_element(By.ID, "user-btn")
        userbtn.click()
        self.driver.implicitly_wait(1)
        time.sleep(2)

        logout = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout")
        logout.click()
        self.driver.implicitly_wait(1)
        time.sleep(2)

        alert = self.driver.switch_to.alert
        alert.accept()

        expected_url_4 = "http://localhost/blog_git/personalBlog/index.php"
        self.assertEqual(self.driver.current_url, expected_url_4, "Login was not successful. URL did not change.")

    def Teardown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()






