import boto3
import os
import sys
import glob

def client():
    return boto3.client('s3')

def resource():
    return boto3.resource('s3')

resource = resource()
client = client()

def create_bucket(name, region):
	client.create_bucket(Bucket=name, CreateBucketConfiguration={'LocationConstraint':region})

def list_buckets(resource):
	for buckets in resource.buckets.all():
	    print(bucket.name)

def list_objects(client, bucket, prefix =''):
    objects = []
    for k in client.list_objects(Bucket=bucket, Prefix=prefix)['Contents']:
        objects.append(k['Key'])
    return objects

def get_object(client, bucket, key):
	client.get_object(Bucket=bucket, Key=key)

# the key is used as both the source (local file) and the destination (s3 key within the bucket)
def upload(resource, bucket, key):
	resource.Bucket(bucket).upload_file(Filename=key, Key=key)

def upload_folders(path, bucket):
	files = list_local_files(os.path.abspath(path))
	key = path.split("/", 4)[-1]
	for file in files:
		upload(resource, bucket, key)

# Pattern match on all files within the path, so you must pass the specific parent folder of the files
def list_local_files(path):
	files = []
	for file in glob.iglob(os.path.join(path, '*'), recursive=True):
		print(file)
		files.append(file)
	return files

def download(resource, bucket, key, outpath):
	for k in list_objects(client, bucket, key):
		if k.startswith(key) and not k.endswith('.temp'):
			print("KEY: " + k)
			outfile = k.split('/')[-1]
			resp = resource.Object(bucket, k).download_file(f''.join([outpath, "/", outfile]))
