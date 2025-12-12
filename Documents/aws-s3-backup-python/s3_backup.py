import boto3
import os

# Connect to S3 in Sydney
s3 = boto3.resource("s3", region_name="ap-southeast-2")


def show_buckets(s3_resource):
    """Print all S3 buckets in this account."""
    print("Your S3 buckets:")
    for bucket in s3_resource.buckets.all():
        print(bucket.name)


def upload_backup(s3_resource, file_name, bucket_name, key_name):
    """Upload the backup file to the given bucket/key."""
    if not os.path.exists(file_name):
        print("File not found:", file_name)
        return

    with open(file_name, "rb") as data:
        s3_resource.Bucket(bucket_name).put_object(Key=key_name, Body=data)

    print("Backup uploaded successfully.")


if __name__ == "__main__":
    bucket_name = "python-for-devops-badal"
    file_name = "/Users/badalsenchury/documents/python-workshop-practice/backup/backup_2025-12-10.tar.gz"
    key_name = "my-backup.tar.gz"

    show_buckets(s3)
    upload_backup(s3, file_name, bucket_name, key_name)
    

        

