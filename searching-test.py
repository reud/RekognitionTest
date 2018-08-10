import boto3
import sys
args=sys.argv
#(arg1,arg2,arg3)=(bucket,file,collectionID)

BUCKET = args[1]
KEY = args[2]
COLLECTION = args[3]

def search_faces_by_image(bucket, key, collection_id, threshold=80, region="us-east-2"):
	rekognition = boto3.client("rekognition", region)
	response = rekognition.search_faces_by_image(
		Image={
			"S3Object": {
				"Bucket": bucket,
				"Name": key,
			}
		},
		CollectionId=collection_id,
		FaceMatchThreshold=threshold,
	)
	return response['FaceMatches']

for record in search_faces_by_image(BUCKET, KEY, COLLECTION):
	face = record['Face']
	print("Matched Face ({}%)".format(record['Similarity']))
	print("  FaceId : {}".format(face['FaceId']))
	print("  ImageId : {}".format(face['ExternalImageId']))