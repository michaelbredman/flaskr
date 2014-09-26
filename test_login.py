
# from selenium.webdriver.firefox.webdriver import WebDriver
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time, unittest, sys, copy
import wd.parallel
import os


class TestLogin(unittest.TestCase):

    def setUp(self):
        # self.wd = WebDriver()
        # self.wd.implicitly_wait(60)

        desired_capabilities = []

        browser = copy.copy(webdriver.DesiredCapabilities.CHROME)
        browser['platform'] = 'Windows 8.1'
        browser['name'] = 'Windows 8.1 Chrome 35'
        browser['version'] = '35'
        desired_capabilities += [browser]

        browser = copy.copy(webdriver.DesiredCapabilities.FIREFOX)
        browser['platform'] = 'Windows 8.1'
        browser['name'] = 'Windows 8.1 Firefox 29'
        browser['version'] = '29'
        browser['screen-resolution'] = '1280x1024'
        desired_capabilities += [browser]

        browser = copy.copy(webdriver.DesiredCapabilities.INTERNETEXPLORER)
        browser['platform'] = 'Windows 7'
        browser['name'] = 'Windows 7 IE 9'
        browser['version'] = '9'
        desired_capabilities += [browser]

        browser = copy.copy(webdriver.DesiredCapabilities.INTERNETEXPLORER)
        browser['platform'] = 'Windows 8'
        browser['name'] = 'Windows 8 IE 10'
        browser['version'] = '10'
        desired_capabilities += [browser]

        browser = copy.copy(webdriver.DesiredCapabilities.SAFARI)
        browser['platform'] = 'OS X 10.9'
        browser['name'] = 'OS X 10.9 Safari 7'
        browser['version'] = '7'
        desired_capabilities += [browser]


        self.drivers = wd.parallel.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://" + os.environ['SAUCE_USERNAME'] + ":" + os.environ['SAUCE_ACCESS_KEY'] + "@ondemand.saucelabs.com:80/wd/hub"
        )

    #@saucehelper.timeit
    @wd.parallel.multiply
    def test_parallel(self):
        print "Setting up tests...."

        # print "Native Events Supported: " + str(self.driver.desired_capabilities)

        print "Working on : " + self.driver.desired_capabilities['platform'] \
        + " " + self.driver.desired_capabilities['browserName'] \
        + " " + self.driver.desired_capabilities['version']
        print "Working on session : " + self.driver.session_id

        #saucehelper.report_test_name(self.driver.session_id, self.driver.session_id, os.environ['SAUCE_USERNAME'], os.environ['SAUCE_ACCESS_KEY'])
        #saucehelper.report_build_number("Sauce", self.driver.session_id, os.environ['SAUCE_USERNAME'], os.environ['SAUCE_ACCESS_KEY'])

        self.driver.get("http://localhost:5000")
        self.driver.find_element_by_link_text("log in").click()
        self.driver.find_element_by_name("username").click()
        self.driver.find_element_by_name("username").clear()
        self.driver.find_element_by_name("username").send_keys("admin")
        self.driver.find_element_by_name("password").click()
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("default")
        self.driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        self.driver.find_element_by_link_text("log out").click()
        #title = self.driver.title
        #self.assertEquals("American Greetings", title)

        # wait = (self.driver, 30)
        # print "Wait" + str(wait)
        # condition = EC.text_to_be_present_in_element((By.TAG_NAME, "html"), "Private Banking")
        # print "********CONDIITON***********" + str(condition)
        # This is currently saving the image locally how do I do it on Sauce?
            # self.driver.save_screenshot(self.driver.desired_capabilities['platform'] \
        # + "-" + self.driver.desired_capabilities['version'] + "-" + self.driver.session_id + ".png")
        # wait.until(condition)

    @wd.parallel.multiply
    def tearDown(self):
        print "Tearing down test...."
        status = sys.exc_info() == (None, None, None)
        print "Status: " + str(status)
        if status == True:
            print "Test passed...."
        else:
            print "Test failed.... https://saucelabs.com/tests/" + self.driver.session_id

        #saucehelper.report_status(status, self.driver.session_id, os.environ['SAUCE_USERNAME'], os.environ['SAUCE_ACCESS_KEY'])
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
