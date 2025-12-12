# AWS S3 Backup Script (Python)

This project is a simple Python script that uploads a backup file to an AWS S3 bucket using `boto3`.

## Features
- Lists available S3 buckets
- Uploads a local backup file to S3
- Uses AWS SDK for Python (boto3)

## File
- `s3_backup.py` – main script for uploading backups to S3

## Requirements
- Python 3
- AWS credentials configured (`aws configure`)
- boto3 library

## Install dependencies
```bash
pip install boto3
