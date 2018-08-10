import boto3
import  json
#see Collection List
if __name__=="__main__":
    client = boto3.client('rekognition','us-east-1')
    response=client.list_collections()
    response=json.dumps(response)
    print(response)