import json
import requests

MEDIA_ALPHA_URL = 'http://insurance-test.mediaalpha.com/ivr.json'


def validate_input(payload):
    """
    Validate payload
    :param payload: A dict
    :return: The body of the payload
    """
    try:
        body = payload['body']
    except KeyError:
        body = payload
    else:
        body = json.loads(body)

    if 'version' not in body:
        raise Exception('Invalid json object')

    return body


def get_phone_number(event, context):
    """

    :param event:
    :param context:
    :return:
    """
    valid_body = validate_input(event)

    r = requests.post(MEDIA_ALPHA_URL, json=valid_body)
    response = {
        "statusCode": r.status_code,
        "body": r.json(),
    }

    return response
