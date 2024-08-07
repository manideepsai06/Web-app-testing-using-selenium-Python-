import unittest
from selenium import webdriver

class TestMain(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.get("https://manideepsai.netlify.app/")

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_title(self):
        expected = "Manideepsai"
        if self.browser.title != expected:
            print("invalid title got {}, but want {}".format(self.browser.title, expected))
            return False
        return True

if __name__ == "__main__":
    unittest.main()