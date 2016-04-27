import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
class Expedia_search(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_Expedia(self):
        """

        :return:
        """
        driver = self.driver
        driver.get("https://www.expedia.com/")

        self.assertIn("Expedia", driver.title, "")
        search_flights = driver.find_element_by_xpath('//*[@id="tab-flight-tab"]').send_keys('\n')
        driver.implicitly_wait(2)


        search_round_trip = driver.find_element_by_id('flight-type-roundtrip-label')
        search_round_trip.send_keys('\n')
        driver.implicitly_wait(3)

        search_flying_from = driver.find_element_by_css_selector('#flight-origin').send_keys('MIA')
        search_flying_to = driver.find_element_by_id('flight-destination').send_keys('LAS')


        search_search = driver.find_element_by_id('search-button').send_keys('\n')
        assert "No results found." not in driver.page_source





    def assert_element_not_empty(element):
        """

        :return:
        """
        element_text = element.text

        if element_text == '':
            raise AssertionError('The element does not contain any text')
        else:
            print 'Element does contain some text. The text is: %s' % element_text

    def assert_element_contain_text(element, text):
        """

        :param element:
        :param text:
        :return:
        """
        element_text = element.text
        if text in element_text:
            print ('The element contain text: %s' % element_text)
        else:
            raise AssertionError('The element does not contain any text: %s' % element_text)

        return


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
