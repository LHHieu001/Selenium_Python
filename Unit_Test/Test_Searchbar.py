from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

debugger_address = 'localhost:8989'

c_options = Options()
c_options.add_experimental_option("debuggerAddress", "localhost:8989")

driver = webdriver.Edge(options=c_options)


driver.get('http://localhost/blog_git/personalBlog/')
el = driver.find_element(By.NAME, "search_box")
el.send_keys("Hello")
el.submit()




driver.quit() 