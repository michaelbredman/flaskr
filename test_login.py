from selenium import webdriver
import unittest
import sys
import copy
import wd.parallel
import os


class TestLogin(unittest.TestCase):

    def setUp(self):

        desired_capabilities = []

        browser = copy.copy(webdriver.DesiredCapabilities.CHROME)
        browser['platform'] = 'Windows 8.1'
        browser['name'] = 'Windows 8.1 Chrome 35'
        browser['version'] = '35'
        browser['tunnel-identifier'] = os.environ['TRAVIS_JOB_NUMBER']
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

    @wd.parallel.multiply
    def test_parallel(self):
        self.driver.get("http://www.yahoo.com")

        '''
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
        '''

    @wd.parallel.multiply
    def tearDown(self):
        print "Tearing down test...."
        status = sys.exc_info() == (None, None, None)
        print "Status: " + str(status)
        if status == True:
            print "Test passed...."
        else:
            print "Test failed.... https://saucelabs.com/tests/" + self.driver.session_id

        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
