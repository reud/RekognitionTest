#coding: utf-8
import sys,boto3

#choice with commandline arguments  　arg1:S3bucket name arg2:image file name
args=sys.argv #配列数2
if __name__=="__main__":
    #get fileName and bucket
    fileName=args[2]
    fileName=args[1]
    client=boto3.client('rekognition','us-east-1')
    