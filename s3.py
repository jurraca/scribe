import boto3
import sys

def client():
    return boto3.client('s3')

def resource():
    return boto3.resource('s3')

resource = resource()
client = client()

def list_buckets(resource):
	for buckets in resource.buckets.all():
	    print(bucket.name)

def list_objects(client, prefix =''):
    for k in client.list_objects(Bucket="chaincode-btc", Prefix=prefix)['Contents']:
        print(k['Key'])

def get_object(client, bucket, key):
	client.get_object(Bucket=bucket, Key=key)

# the key is used as both the source (local file) and the destination (s3 key within the bucket)
def upload(resource, bucket, key):
	resource.Bucket(bucket).upload_file(Filename=key, Key=key)

def upload_folders(path, bucket):
	files = list_local_files(path)
	key = path.split("/", 3)[-1]
	for file in files:
		upload(resource, bucket, key)

# Pattern match on all files within the path, so you must pass the specific parent folder of the files
def list_local_files(path):
	files = []
	for file in glob.iglob(r''.join([path, '/*']), recursive=True):
		files.append(file)
	return files

def download(resource, bucket, key, outpath):
	for object in resource.Bucket(name=bucket).objects.all(): #list_objects(client(), ''.join([bucket, "/", key]))
		k = object.key
		print(k)
		if k.startswith(key):
			if k != key + '/.write_access_check_file.temp' and len(k) > 20:
				print("KEY: " + k)
				outfile = k.split('/')[-1]
				resp = resource.Object(bucket, k).download_file(f''.join([outpath, "/", outfile]))


#download(resource, 'chaincode-btc', 'segwit-output', 'segwit-output')

# create local folders per module
# add items to folder
# write objects to s3
# batch translate
# for keys in bucket, download to folders

