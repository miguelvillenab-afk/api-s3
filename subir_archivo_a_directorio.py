import json
import boto3

def lambda_handler(event, context):
    body = json.loads(event['body'])
    nombre_bucket = body['bucket']
    nombre_directorio = body['directorio']
    nombre_archivo = body['archivo']
    contenido = body['contenido']
    
    ruta_completa = f"{nombre_directorio}/{nombre_archivo}"
    
    s3 = boto3.client('s3')
    
    try:
        s3.put_object(
            Bucket=nombre_bucket,
            Key=ruta_completa,
            Body=contenido
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'mensaje': 'Archivo subido exitosamente',
                'ruta': ruta_completa
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }