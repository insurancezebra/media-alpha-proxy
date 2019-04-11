import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

MEDIA_ALPHA_URL = os.getenv("MEDIA_ALPHA_URL")
PAYLOAD_SECRETS = {
    "API_TOKEN": os.getenv("API_TOKEN"),
    "PLACEMENT_ID": os.getenv("PLACEMENT_ID")
}
