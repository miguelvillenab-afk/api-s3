import json
import boto3

def lambda_handler(event, context):
    body = event['body']
    nombre_bucket = body['bucket']
    
    s3 = boto3.client('s3')
    
    try:
        s3.create_bucket(Bucket=nombre_bucket)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'mensaje': 'Bucket creado exitosamente',
                'bucket': nombre_bucket
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
