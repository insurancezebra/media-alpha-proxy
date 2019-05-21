import os


MEDIA_ALPHA_URL = os.getenv("MEDIA_ALPHA_URL")

PAYLOAD_SECRETS = {
    "API_TOKEN": os.getenv("API_TOKEN"),
    "PLACEMENT_ID": os.getenv("PLACEMENT_ID")
}

CI_REPO_NAME = os.getenv("CI_REPO_NAME")
CI_COMMIT_ID = os.getenv("CI_COMMIT_ID")
CI_BRANCH = os.getenv("CI_BRANCH")
