# Serverless Threat Detection & Automated Incident Response System

## Project Overview
This project is a serverless cloud security monitoring system built using AWS services such as AWS Lambda, Amazon S3, Amazon SNS, and IAM.

The system automatically detects suspicious activity, sends real-time email alerts, and stores security incident logs inside an Amazon S3 bucket.

This project demonstrates event-driven cloud automation and serverless architecture using AWS.

---

# Architecture Used

AWS Lambda → Amazon SNS → Email Alert  
AWS Lambda → Amazon S3 → Incident Logs

---

# AWS Services Used

## 1. AWS Lambda
Used to run serverless Python code for:
- Detecting suspicious activity
- Sending email notifications
- Generating incident logs

## 2. Amazon SNS
Used for:
- Real-time email alerts
- Notification delivery system

## 3. Amazon S3
Used for:
- Storing security incident logs
- Maintaining monitoring records

## 4. IAM (Identity and Access Management)
Used for:
- Secure permissions management
- Role-based access control

---

# Features

- Real-time security alert emails
- Automated incident logging
- Serverless architecture
- Event-driven automation
- AWS cloud integration
- Secure IAM permission handling
- Automatic S3 log generation

---

# Project Workflow

## Step 1
AWS Lambda function gets triggered.

## Step 2
Lambda detects suspicious activity.

## Step 3
Amazon SNS sends a security alert email.

## Step 4
Incident log file is automatically stored in Amazon S3 bucket.

# Outcome

This project successfully demonstrates:
- AWS serverless computing
- Cloud security monitoring
- Automated incident response
- Real-time alert generation
- Event-driven architecture
---

# Project Structure

```text
serverless-threat-detection-system/
│
├── screenshots/
│   ├── 01_IAM_User_Creation.png
│   ├── 02_S3_Bucket_Created.png
│   ├── 03_Lambda_Function_Created.png
│   ├── 04_Lambda_Code_Screen.png
│   ├── 05_IAM_Role_Permissions.png
│   ├── 06_SNS_Email_Subscription.png
│   ├── 07_Lambda_Test_Success.png
│   ├── 08_S3_Logs_Generated.png
│   ├── 09_Trigger_Connected.png
│   └── 10_Security_Alert_Email.png
│
├── lambda_function.py
└── README.md


# Author

Afra Anees
