from google.cloud import storage
from google.oauth2 import service_account
from datetime import timedelta

def generate_signed_url(bucket_name, file_name, credentials_path):
    # Carga las credenciales desde el archivo JSON
    credentials = service_account.Credentials.from_service_account_file(credentials_path)

    # Crea el cliente de almacenamiento con las credenciales
    client = storage.Client(credentials=credentials)

    # Obtén el bucket y el archivo
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    # Configura las opciones para la URL firmada
    url = blob.generate_signed_url(
        version="v4",
        expiration=timedelta(minutes=15),  # Expiración: 15 minutos
        method="GET"
    )

    return url

# Ejemplo de uso
if __name__ == "__main__":
    bucket_name = "example-video-test"
    file_name = "naturaleza.mp4"
    credentials_path = "./credentials.json"
    
    signed_url = generate_signed_url(bucket_name, file_name, credentials_path)
    print(f"Signed URL: {signed_url}")
