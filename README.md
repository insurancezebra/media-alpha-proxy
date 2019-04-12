## Media Alpha Proxy

A service for proxying data with FrontEnd

#### Running
To run serverless locally...

Using invoke local:
```bash
serverless invoke local -f phone_number -p test_object.json
```

Using serverless offline:

The following generates an endpoint, which `POST` requests can be sent to passing along a json object in the body
```bash
npm install
serverless offline start
```
It can be tested using Postman

* Note: `serverless` can be replaced with `sls`.


#### Testing
To run tests, simply run
```bash
python -m test
```
