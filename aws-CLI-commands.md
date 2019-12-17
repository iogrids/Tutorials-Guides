# AWS CLI COMMANDS

## To install AWS CLI

```
pip3 install awscli --upgrade --user```
```

## CONFIGURE KEYS

To configure private key and access key

```
aws configure
```

## All services of AWS CLI

Flow:

1. Create a user
2. Create a group
3. Attach user to the group
4. create a policy - Policy is used to define the level of access in EC2, level of access in AWS Lambda etc
5. Attach policy to the group created

You can also create a role

1. Create a role for another account. roles defines what the other account can do eg: create a ec2 instance. 
2. You can also create a policy and attach it to the role. Policy gives micro level access like "start an ec2 instance", "stop an ec2 instance" etc..

```
https://docs.aws.amazon.com/cli/latest/reference/#available-services
```

# AWS IAM

Modules in IAM: users, groups, roles, policies

## Using AWS CLI with IAM USERS

```
aws iam list-users  - Lists all users
aws iam create-user --user-name George - Creates a new user named George
aws iam delete-user --user-name George
aws iam create-access-key --user-name jeril - Creates a secret key and accesskey for the name jeril
```

## Using AWS CLI with IAM Role

```
aws iam list-roles - Lists all roles
aws iam create-role --role-name TestRole
### To create a policy and attach a particular JSON policy to a role. Here Json file has to be created 
aws iam create-role --role-name TestRole --assume-role-policy-document file://ec2-role-trust-policy.json
aws iam delete-role --role-name TestRole
```

### Using AWS CLI with IAM GROUP

```
aws iam list-groups - Lists all groups eg, Administrator group etc
aws iam create-group --group-name Developers - Creates a group called developer
aws iam delete-group --group-name Developers
aws iam add-user-to-group --user-name George --group-name Developers - adds user George to group Developers
### To attach a paricular policy to a group
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AmazonEC2FullAccess --group-name Developers
```

### Using AWS CLI with IAM Policy

```
## To list all IAM policies

aws iam list-policies --scope AWS | more - Lists all policies which comes under the scope of AWS. Apart from AWS there are also custom policies. more command displays a huge list part by part

### To find the policy ARN, list all policies and copy the ARN
aws iam attach-group-policy --policy-arn <ENTER-POLICY-ARN-HERE>

Example:

### To attach a paricular policy to a group
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AmazonEC2FullAccess --group-name Developers
```

---

## Using AWS CLI with S3 buckets

```
aws s3 ls -> lists all buckets
aws s3 mb s3://nov12-5-test -> Create a new bucket with the name nov12-5-test
aws s3 ls s3://land.giftsweep.us -> To find all the files inside the bucket land.giftsweep.us
aws s3 cp index.html s3://nov12-5-test -> copy a local file named index.html to the bucket nov12-test
aws s3 cp s3://nov12-5-test/index.html . -> copy index.html from s3 bucket to local (Note: There is a dot (.) after index.html)
aws s3 sync . s3://nov12-5-test -> sync everything in the current directory with the files inside the bucket.
```

---

## Using AWS CLI with EC2

```

```

---
