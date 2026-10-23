import json
import boto3

def lambda_handler(event, context):
    body = event['body']
    nombre_bucket = body['bucket']
    nombre_directorio = body['directorio']
    if not nombre_directorio.endswith('/'):
        nombre_directorio += '/'
        
    s3 = boto3.client('s3')
    
    try:
        s3.put_object(
            Bucket=nombre_bucket,
            Key=nombre_directorio
        )
        
        return {
            'statusCode': 200,
            'body': {
                'mensaje': 'Directorio creado exitosamente',
                'directorio': nombre_directorio
            }
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': {'error': str(e)}
        }
