import unittest
import json


response_str = '{"data": [' \
               '{"name": "John", "age": "30", "city": "New York"}, ' \
               '{"name": "Harry", "age": "40", "city": "New York"}]}'


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        print('\n')

    def test_something(self):

        response = response_str
        response_json = json.loads(response)        # converts string to dict

        data = response_json['data']
        total = 0

        for record in data:
            total += int(record['age'])

        self.assertEqual(70, total)

        print(type(response_json))
        response_string = json.dumps(response_json) # converts dict to str
        print(type(response_string))


if __name__ == '__main__':
    unittest.main()
