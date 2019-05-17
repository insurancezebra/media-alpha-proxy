## Media Alpha Proxy

A service for proxying data with FrontEnd

#### Run Locally
To run serverless locally...

1. Using invoke local:
```bash
serverless invoke local -f phone_number -p test_object.json
```

2. Using serverless offline:

The following generates an endpoint, which `POST` requests can be sent to passing along a json object in the body
```bash
npm install
serverless offline
```
It can be tested using Postman

* Note: `serverless offline` can be replaced with `sls offline`.


#### Deploy
You should deploy using Jenkins!!

However, to deploy from your local machine, where `dev` can be substituted for the proper environment (e.g. `prod`), run..
```bash
ENVIRONMENT=dev ./deploy.sh
```

#### Testing
To run tests, simply run
```bash
python -m test
```
