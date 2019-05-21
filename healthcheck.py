import json
from settings import CI_REPO_NAME, CI_COMMIT_ID, CI_BRANCH


def get_info():
    return {'repo': CI_REPO_NAME, 'version': CI_COMMIT_ID, 'branch': CI_BRANCH}


def calculate_status(info):
    return 200 if all(info.values()) else 503


def check_version(event, context):
    info = get_info()
    response = {
        'statusCode': calculate_status(info),
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        },
        'body': json.dumps(get_info())
    }
    return response


def check_component():
    return []
