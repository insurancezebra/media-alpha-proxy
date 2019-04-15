## Media Alpha Proxy

A service for proxying data with FrontEnd

#### ToDo
Script to:
- Create and activate virtualenv, using python 3.6
- Install packages in requirements.txt
- Run npm install (install serverless -g, serverless python requirements and serverless offline python)

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
serverless offline
```
It can be tested using Postman

* Note: `serverless` can be replaced with `sls`.


#### Deploy
To deploy, where `dev` can be substituted for the proper environment, run..
```bash
ENVIRONMENT=dev ./deploy.sh
```
where 

#### Testing
To run tests, simply run
```bash
python -m test
```
