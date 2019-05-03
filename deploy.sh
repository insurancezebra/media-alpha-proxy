#!/usr/bin/env bash

export CI_REPO_NAME=$(basename `git rev-parse --show-toplevel`)
export CI_COMMIT_ID=$(git rev-parse HEAD)
export CI_BRANCH=$(git branch | grep \* | cut -d ' ' -f2)

serverless deploy --aws-profile MyZebraUser  --stage "${ENVIRONMENT}"
