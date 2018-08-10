import boto3
import json
import  sys
args=sys.argv
#commandline argument:collectionID
#dont use it if you had corretion
if __name__=="__main__":
    client = boto3.client('rekognition','us-east-2')

    response = client.create_collection(
        CollectionId=args[1]
    )

    response = json.dumps(response)
    print(response)