from selenium.webdriver.common.by import By
from test_selenium.page.base_page import BasePage

class Message(BasePage):
    def send(self,app="",group="",content=""):
        self.find((By.LINK_TEXT,'选择需要发消息的应用')).click()
        self.find((By.CSS_SELECTOR,'div[data-name*=%s]' % app)).click()
        self.find((By.LINK_TEXT,'确定')).click()
        self.find((By.LINK_TEXT, '选择发送范围')).click()
        element = self._driver.find_elements(By.CSS_SELECTOR,'.ww_searchInput_text')
        element[-1].send_keys(group)
        element=self._driver.find_elements((By.CSS_SELECTOR,'#searchResult ul>li>a'))
        element[-1].click()
        self.find((By.LINK_TEXT,'确认')).click()
        self.find((By.CSS_SELECTOR, 'textarea.js_send_msg_text')).send_keys(content)
        self.find((By.LINK_TEXT, '发送')).click()





    def get_message(self):
        pass
