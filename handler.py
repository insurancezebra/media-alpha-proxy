import json
import requests
import logging

MEDIA_ALPHA_URL = 'http://insurance-test.mediaalpha.com/ivr.json'
log = logging.getLogger(__name__)


def validate_input(payload):
    """
    Validate payload
    :param payload: A dict
    :return: The body of the payload
    """
    try:
        body = payload['body']
    except KeyError:
        log.warning(' Key \'body\' not found. Continuing...')
        body = payload
    else:
        body = json.loads(body)

    return body


def get_phone_number(event, context):
    """
    Get the users phone number
    :param event: Contains payload
    :param context:
    :return: Object containing phone number
    """
    body = validate_input(event)

    r = requests.post(MEDIA_ALPHA_URL, json=body)
    response = {
        "statusCode": r.status_code,
        "body": r.json(),
    }

    return response
