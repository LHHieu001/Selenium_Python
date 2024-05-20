#Description:
#1.Go to View All Authors and choose an author
#2.Click Follow (Should be failed)
#3.Go from login to register and make a new user account then login
#4.Find a blog on search bar and click on the searched blog's author name
#5.Follow the author
#6.Back to the homepage, go to Follow posts and unfollow the author
#7.Log out

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

    def test_3(self):

        #1.Go to View All Authors and choose an author
        authors = self.driver.find_element(By.NAME, "ViewAllAuthors")
        authors.click()
        self.driver.implicitly_wait(2)
        expected_Authors_url = "http://localhost/blog_git/personalBlog/authors.php"
        self.assertEqual(self.driver.current_url, expected_Authors_url,
                         "Test was not successful. URL did not change as expected.")
        time.sleep(2)

        author = self.driver.find_element(By.XPATH, "//a[contains(@href, 'author_posts.php?author=HieuAuthor')]")
        time.sleep(1)
        author.click()
        expected_Author_url = "http://localhost/blog_git/personalBlog/author_posts.php?author=HieuAuthor"
        self.assertEqual(self.driver.current_url, expected_Author_url,
                         "Test was not successful. URL did not change as expected.")

        #2.Click Follow (Fail)
        time.sleep(1)
        follow = self.driver.find_element(By.CLASS_NAME, "fa-plus-square")
        self.driver.execute_script("arguments[0].scrollIntoView()", follow)
        time.sleep(2)

        self.driver.execute_script("arguments[0].click();", follow)
        self.driver.implicitly_wait(3)

        followfail_message = self.driver.find_element(By.CLASS_NAME, "message")
        assert "please login first!" in followfail_message.text
        print("Fail follow: Pass")

        # 3.Go from login to register and make a new user account
        time.sleep(2)
        userbtn = self.driver.find_element(By.ID, "user-btn")
        userbtn.click()
        self.driver.implicitly_wait(1)
        time.sleep(1)

        login = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Login")
        time.sleep(1)
        login.click()

        expected_login_url = "http://localhost/blog_git/personalBlog/login.php"
        self.assertEqual(self.driver.current_url, expected_login_url,
                         "Test was not successful. URL did not change as expected.")
        time.sleep(2)

        register = self.driver.find_element(By.PARTIAL_LINK_TEXT, "register now")
        register.click()

        expected_register_url = "http://localhost/blog_git/personalBlog/register.php"
        self.assertEqual(self.driver.current_url, expected_register_url, "Test was not successful. URL did not change "
                                                                         "as expected.")

        time.sleep(2)

        name = self.driver.find_element(By.NAME, "name")
        name.send_keys("Hieu1209")

        email = self.driver.find_element(By.NAME, "email")
        email.send_keys("LeHoangHieu0236@gmail.com")

        password = self.driver.find_element(By.NAME, "pass")
        password.send_keys("SN12092003#")

        cpassword = self.driver.find_element(By.NAME, "cpass")
        cpassword.send_keys("SN12092003#")

        self.driver.implicitly_wait(3)
        time.sleep(2)

        submit = self.driver.find_element(By.NAME, "submit")
        submit.click()

        expected_url = "http://localhost/blog_git/personalBlog/index.php"
        self.assertEqual(self.driver.current_url, expected_url,
                         "Registration was not successful. URL did not change as expected.")

        # 4.Find a blog on search bar and click on the searched blog's author name
        search = self.driver.find_element(By.NAME, "search_box")
        time.sleep(2)
        search.send_keys("Test")
        time.sleep(2)
        search.submit()

        expected_search_url = "http://localhost/blog_git/personalBlog/search.php"
        self.assertEqual(self.driver.current_url, expected_search_url,"Search was not successful. URL did not change")

        author_name = self.driver.find_element(By.PARTIAL_LINK_TEXT, "HieuAuthor11")
        self.driver.execute_script("arguments[0].click();", author_name)


        # 5.Follow the author
        follow_1 = self.driver.find_element(By.CLASS_NAME, "fa-plus-square")
        self.driver.execute_script("arguments[0].scrollIntoView()", follow_1)
        time.sleep(2)

        self.driver.execute_script("arguments[0].click();", follow_1)
        self.driver.implicitly_wait(3)

        follow_message = self.driver.find_element(By.CLASS_NAME, "message")
        assert "added to follows" in follow_message.text
        print("Follow: Pass")

        #6.Back to the homepage, go to Follow posts and unfollow the author
        home = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Blcogoat.")
        self.driver.execute_script("arguments[0].scrollIntoView();", home)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", home)

        expected_index_url = "http://localhost/blog_git/personalBlog/index.php"
        self.assertEqual(self.driver.current_url, expected_index_url, "Test was not successful")
        time.sleep(3)

        el = self.driver.find_element(By.NAME, "UserFollows")
        el.click()

        self.driver.implicitly_wait(3)

        expected_follow_url = "http://localhost/blog_git/personalBlog/user_follow.php"
        self.assertEqual(self.driver.current_url, expected_follow_url,
                         "Test was not successful. URL did not change as expected.")
        self.driver.implicitly_wait(3)

        unfollow = self.driver.find_element(By.NAME, "follow_author")
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", unfollow)

        unfollow_message = self.driver.find_element(By.CLASS_NAME, "message")
        assert "removed from follows" in unfollow_message.text
        print("Unfollow: Pass")
        time.sleep(2)

        userbtn_1 = self.driver.find_element(By.ID, "user-btn")
        userbtn_1.click()
        self.driver.implicitly_wait(1)
        time.sleep(1)

        logout = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout")
        logout.click()
        self.driver.implicitly_wait(1)
        time.sleep(1)

        alert = self.driver.switch_to.alert
        time.sleep(1)
        alert.accept()

        expected_url = "http://localhost/blog_git/personalBlog/index.php"
        self.assertEqual(self.driver.current_url, expected_url, "Log out was not successful. URL did not change.")

        def tearDown(self):
            self.driver.quit()


if __name__ == '__main__':
    unittest.main()






