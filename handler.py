import json
import logging

import requests

from settings import MEDIA_ALPHA_URL, PAYLOAD_SECRETS

log = logging.getLogger(__name__)


def affix_secrets(payload):
    """
    Affixes secrets to payload
    :param payload: Incoming data
    :return: Data with
    """
    try:
        payload = json.loads(payload)
    except TypeError as e:
        log.info(f'{e}\nBody parameter is of type \'dict\'\nContinuing...')
    finally:
        payload['api_token'] = PAYLOAD_SECRETS['API_TOKEN']
        payload['placement_id'] = payload.get('placement_id') or PAYLOAD_SECRETS['PLACEMENT_ID']

    return payload


def get_phone_number(event, context):
    """
    Get the users phone number
    :param event: Contains payload
    :param context:
    :return: Object containing phone number
    """
    payload = event.get('body', event)

    # Append secrets to payload
    data = affix_secrets(payload)

    r = requests.post(MEDIA_ALPHA_URL, json=data)
    response = {
        'statusCode': r.status_code,
        'body': r.text,
    }

    return response
