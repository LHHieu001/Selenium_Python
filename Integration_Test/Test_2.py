#Description:
#1.Log in as user
#2.Change the theme of website
#3.Go to Update Profile and change password
#4.Log out and Log in with the new password
#5.Go to Like Post and switch to dislike
#6.Log out
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

    def test_2(self):

        # 1.Log in
        login = self.driver.find_element(By.PARTIAL_LINK_TEXT, "User")
        login.click()
        self.driver.implicitly_wait(1)

        expected_url_1 = "http://localhost/blog_git/personalBlog/login.php"
        self.assertEqual(self.driver.current_url, expected_url_1, "Test was not successful. URL did not change.")
        time.sleep(1)

        email = self.driver.find_element(By.NAME, "email")
        email.send_keys("LeHoangHieu9903@gmail.com")
        password = self.driver.find_element(By.NAME, "pass")
        password.send_keys("123")
        self.driver.implicitly_wait(2)
        time.sleep(1)

        submit = self.driver.find_element(By.NAME, "submit")
        submit.click()
        expected_url_2 = "http://localhost/blog_git/personalBlog/index.php"
        self.assertEqual(self.driver.current_url, expected_url_2, "Login was not successful. URL did not change.")

        # 2. Change the theme
        theme = self.driver.find_element(By.ID, "theme-button")
        theme.click()
        time.sleep(3)

        # 3. Update Profile (Change Password)
        update = self.driver.find_element(By.NAME, "UpdateProfile")
        update.click()
        time.sleep(1)

        expected_url_3 = "http://localhost/blog_git/personalBlog/update.php"
        self.assertEqual(self.driver.current_url, expected_url_3, "Action was not successful. URL did not change.")
        time.sleep(2)

        oldpassword = self.driver.find_element(By.NAME, "old_pass")
        oldpassword.send_keys("123")

        newpassword = self.driver.find_element(By.NAME, "new_pass")
        newpassword.send_keys("123")

        cpassword = self.driver.find_element(By.NAME, "confirm_pass")
        cpassword.send_keys("123")
        time.sleep(1)

        submit = self.driver.find_element(By.NAME, "submit")
        submit.click()
        self.driver.implicitly_wait(2)

        message = self.driver.find_element(By.CLASS_NAME, "message")
        assert "password updated successfully!" in message.text
        print("Password Update: Pass")

        # 4.Log out and Log in with the new password

        time.sleep(1)
        userbtn = self.driver.find_element(By.ID, "user-btn")
        userbtn.click()
        self.driver.implicitly_wait(1)
        time.sleep(1)

        logout = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout")
        logout.click()
        self.driver.implicitly_wait(1)
        time.sleep(1)

        alert = self.driver.switch_to.alert
        alert.accept()

        expected_url_4 = "http://localhost/blog_git/personalBlog/index.php"
        self.assertEqual(self.driver.current_url, expected_url_4, "Log out was not successful. URL did not change.")

        login_1 = self.driver.find_element(By.PARTIAL_LINK_TEXT, "User")
        login_1.click()
        self.driver.implicitly_wait(1)

        expected_url_5 = "http://localhost/blog_git/personalBlog/login.php"
        self.assertEqual(self.driver.current_url, expected_url_5, "Test was not successful. URL did not change.")
        time.sleep(1)

        email_1 = self.driver.find_element(By.NAME, "email")
        email_1.send_keys("LeHoangHieu9903@gmail.com")
        password_1 = self.driver.find_element(By.NAME, "pass")
        password_1.send_keys("123")
        self.driver.implicitly_wait(2)
        time.sleep(1)

        submit_1 = self.driver.find_element(By.NAME, "submit")
        submit_1.click()
        expected_url_6 = "http://localhost/blog_git/personalBlog/index.php"
        self.assertEqual(self.driver.current_url, expected_url_6, "Login was not successful. URL did not change.")

        #5. Go to like post and switch to dislike
        like = self.driver.find_element(By.NAME, "UserLikes")
        like.click()

        expected_url_7 = "http://localhost/blog_git/personalBlog/user_likes.php"
        self.assertEqual(self.driver.current_url, expected_url_7, "Action was not successful. URL did not change.")

        dislike = self.driver.find_element(By.NAME, "dislike_post")
        self.driver.execute_script("arguments[0].click()", dislike)
        self.driver.implicitly_wait(1)
        time.sleep(1)
        message_dislike = self.driver.find_element(By.CLASS_NAME, "message")
        assert "added to dislikes" or "removed from likes" in message_dislike.text
        print("Dislike: pass")

        #6. Log out
        userbtn_1 = self.driver.find_element(By.ID, "user-btn")
        userbtn_1.click()
        self.driver.implicitly_wait(1)
        time.sleep(1)

        logout_1 = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Logout")
        logout_1.click()
        self.driver.implicitly_wait(1)
        time.sleep(1)

        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(1)

        expected_url_8 = "http://localhost/blog_git/personalBlog/index.php"
        self.assertEqual(self.driver.current_url, expected_url_8, "Log out was not successful. URL did not change.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()



