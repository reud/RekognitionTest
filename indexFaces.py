import boto3
import  sys
import  json
#commandline argument: (arg1,arg2,arg3)=(filename,bucketname,collectionID)
if __name__=="__main__":
    args = sys.argv
    bucket=args[2]
    collectionID=args[3]
    file=open('./'+args[1])
    data1=file.read()
    file.close()
    lines=data1.split("\n")
    client = boto3.client('rekognition','us-east-2')
    for lineFileName in lines:
        response=client.index_faces(CollectionId=collectionID,
                                    Image={'S3Object':{'Bucket':bucket,'Name':lineFileName}},
                                    ExternalImageId=lineFileName,
                                    DetectionAttributes=['ALL'])
        print(f'Faces in {lineFileName}')
        for faceRecord in response['FaceRecords']:
            print(faceRecord['Face']['FaceId'])