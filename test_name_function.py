import unittest
from name_function import get_formatted_name

class MyTestCase(unittest.TestCase):
    def test_something(self):
        formmatted_name = get_formatted_name("janis", "joplin", 'ads')
        self.assertEqual(formmatted_name, "Janis Ads Joplin")


if __name__ == '__main__':
    unittest.main()
