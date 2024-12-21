from google.cloud import storage

# Ruta a tu archivo de credenciales JSON
credentials_path = "./credential.json"

# Nombre del bucket y configuración de CORS
bucket_name = "test-app-video-3"
origin = "https://wpbot.midominio.com" 
response_header = "Content-Type"
max_age_seconds = 3600
method = "GET"

def configure_bucket_cors():
    try:
        # Inicializa el cliente de almacenamiento con el archivo de credenciales
        storage_client = storage.Client.from_service_account_json(credentials_path)
        
        # Obtén el bucket
        bucket = storage_client.get_bucket(bucket_name)
        
        # Configura CORS
        cors_configuration = [{
            "origin": [origin],
            "responseHeader": [response_header],
            "method": [method],
            "maxAgeSeconds": max_age_seconds
        }]
        bucket.cors = cors_configuration
        bucket.patch()  # Actualiza el bucket con la nueva configuración
        
        print(f"Se actualizó el bucket {bucket_name} con la configuración de CORS.")
        print(f"Permitiendo solicitudes {method} desde {origin} compartiendo {response_header}.")
    except Exception as e:
        print(f"Error al configurar CORS para el bucket: {e}")

# Llama a la función
configure_bucket_cors()
