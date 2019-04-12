import json
import unittest
from unittest import TestCase
from unittest.mock import patch

from handler import get_phone_number, affix_secrets


class MediaAlphaTestCase(TestCase):
    def setUp(self) -> None:
        with open('test_object.json') as f:
            self.event = json.load(f)

        self.sample_response = {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': '{'
                    '"time": 0.026, '
                    '"phone_num":"+18552707248", '
                    '"expiration_time":"2019-04-11T19:40:19Z"'
                    '}'
        }

        class RequestMock(object):
            status_code = None
            text = None

            def __init__(self, status_code, return_value):
                self.status_code = status_code
                self.text = return_value

            def json(self):
                return json.loads(self.text)

        self.RequestMock = RequestMock

    def test_affix_secrets(self):
        body = self.event['body']
        self.assertNotIn('api_token', body)
        self.assertFalse(body['placement_id'])

        affix_secrets(self.event['body'])
        self.assertIn('api_token', body)
        self.assertTrue(body['placement_id'])

    @patch('handler.requests.post')
    def test_get_phone_number(self, mock_post):
        mock_post.return_value = self.RequestMock(
            200,
            '{"time": 0.026, "phone_num":"+18552707248", "expiration_time":"2019-04-11T19:40:19Z"}'
        )

        response = get_phone_number(self.event, '')
        self.assertIn('phone_num', response['body'])


if __name__ == '__main__':
    unittest.main()
