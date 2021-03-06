from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
    
    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])




    def test_can_start_a_list_and_retrive_it_later(self):
        #Edith has heard about a cool new online to-do app.
        #She goes to check out its homepage
        
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do',self.browser.title)
        header_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)
        
        #She is invited to enter a to-do item straight away
        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'   
            )
        
        #When she hits enter the page updates,and now the page lists
        #"1:Buy peacock feathers" as an item in a to-do list


        #There is still a text box inviting her to add another item.She
        #enters "Use peacock feathers to make a fly"(Edith is very methodical)     
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(10)
        
        # The page updates again ,and now show both items on her list
        self.check_for_row_in_list_table('1：Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        self.fail('Finish the test!')
        
        #She visit that URL -her to-do list is still here


if __name__ == '__main__':
   unittest.main(warnings='ignore')
    
