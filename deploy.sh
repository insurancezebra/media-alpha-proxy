#!/usr/bin/env bash

python3 -m .virtualenv
source .virtualenv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

npm install serverless -g
npm install

export CI_REPO_NAME=$(basename `git rev-parse --show-toplevel`)
export CI_COMMIT_ID=$(git rev-parse HEAD)
export CI_BRANCH=$(git branch | grep \* | cut -d ' ' -f2)

serverless deploy --aws-profile MyZebraUser-staging  --stage "${ENVIRONMENT}"
