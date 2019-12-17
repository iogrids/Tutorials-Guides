# Serverless Computing Architecture

These are the services that we would be using from Amazon aws

![Serverless Computing](images/serverless.png "Serverless Computing")


![Architecture Diagram](images/architecture.png "Architecture Diagram")

* STEP1 1: How to create an API - Section 1 - Chapter 6

* STEP 2: How to create an API KEY - Section 3 - Chapter 19

     With the help of API KEY we can make sure that only with a valid key the API can be accessed. For each usage of API there are charges.      So always restrict the API with the help of key. You can also set usage plan for this API key. 
     
     You can also set that this API can be used only 1000 times per second. You can also set custom domains for your API. You can also set      log permissions for API usage
     
> Note: You can use various frameworks like serverless, Apex, SAM, Terraform, CF to deploy Lambda functions from command line. 

## Configuring Lambda using Apex Framework

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/u7spDymJqmc/0.jpg)](http://www.youtube.com/watch?v=u7spDymJqmc)


## Configuring Lambda using Serverless Framework

:point_right: Install aws-cli and serverless globally

```
npm install -g aws-cli serverless
```

:point_right: Then create a user in AWS and create a secret key and access key for the same user.

:point_right: There are variety of cloud platforms that serverless can connect to like Google Cloud platform, AWS etc. To make serverless know what we need to use Amazon web services use the command below.

* username: serverless-admin
* Access Key: AKIAIMKE5NA4KOZEU44A
* Secret Key: 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

```
serverless config credentials --provider aws --key AKIAIMKE5NA4KOZEU44A --secret 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 --profile serverless-admin
```

:point_right: Then setup a serverless files for nodejs using a default boilerplate. Using the command below you can create a severless boilerplate template. The below syntax will create 3 files

```
serverless create --template aws-nodejs
```

The boiler plate will create the following files

* handler.js
* serverless.yml
* .gitignore

/* ---------------------------- handler.js ---------------------------- */

```Javascript
'use strict';

//event is anything that we want to pass to LAMBDA
//context gives us information about the function like time taken for execution etc
//callback is a function itself
//callback takes 2 arguments

module.exports.hello = async (event, context, callback) => {
  const response = {
    statusCode: 200,
    body: JSON.stringify({
      message: 'Go Serverless v1.0! Your function executed successfully!',
      input: event,
    }),
  };

  callback(null, response)

  // Use this code if you don't use the http event with the LAMBDA-PROXY integration
  // return { message: 'Go Serverless v1.0! Your function executed successfully!', event };
};

```
/* ------------------------------------- Another example of a Lambda function -------------------- */

```Javascript
exports.handler = (event, context, callback) => {
    
    mqfunc1(event, callback);
    
};

var mqfunc1 = function(event, callback) {
    let a = event.a;
    let b = event.b;
    let c = a+b;
    apple(c, callback);
};

var apple = function(c, callback){
    callback(null, "Hello Jeril" + c);
};
```

/* ------------------------serverless.yml--------------------------------*/

```
service: wut-up-world
provider:
  name: aws
  runtime: nodejs8.10
  stage: dev
  region: us-east-1
  profile: serverless-admin
include:
  - utils/**
functions:
  hello:
    handler: handler.hello
```

:point_right: Now you will have to create a simple REST endpoint. To do that you will have to install a package called serverless-offline

```
npm init -y
npm install  --save-dev serverless-offline
```

then, add this plugin in serverless.yml file as shown below

```
service: wut-up-world # NOTE: update this with your service name
plugins:
  - serverless-offline
```

Next add routes or API endpoints. To add endpoints in API GATEWAY add the following code in serverless.yml file

```
events:
      - http:
          path: message
          method: get
```

To deploy the code and push it to Amazon AWS use the command below

```
serverless deploy
```

To check the logs use the below syntax. The below will tell you the time taken to execute the code, billed duration for the function etc

* hello is the function name
* dev referes to development environment
* 10 referes to code executed 10 minutes back

```
serverless logs -f hello -s dev --startTime 10
```

In order to get the realtime logs you can use

```
serverless logs -f hello -s dev -t
```

