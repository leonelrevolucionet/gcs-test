from flask import Flask, jsonify, request
from google.cloud import storage
from google.oauth2 import service_account
from datetime import timedelta

app = Flask(__name__)

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

@app.route('/get-signed-url', methods=['GET'])
def get_signed_url():
    # bucket_name = request.args.get('bucket_example-video-testname')
    # file_name = request.args.get('file_name')
    bucket_name = 'example-video-test'
    file_name = 'naturaleza.mp4'

    credentials_path = "./credentials.json"
    
    if not bucket_name or not file_name:
        return jsonify({"error": "Missing bucket_name or file_name"}), 400
    
    signed_url = generate_signed_url(bucket_name, file_name, credentials_path)
    
    return jsonify({"signed_url": signed_url})

if __name__ == "__main__":
    app.run(debug=True)
