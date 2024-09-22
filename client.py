from flask_ml.flask_ml_client import MLClient
from flask_ml.flask_ml_server.constants import DataTypes

AUDIO_STYLE_TRANSFER_MODEL_URL = "http://127.0.0.1:5000/audiotransfer"

client = MLClient(AUDIO_STYLE_TRANSFER_MODEL_URL)  # Create an instance of the MLClient object
data_type = DataTypes.AUDIO
inputs = [{"file_path": "Inputs/text1.txt"}]
response = client.request(inputs, data_type)
print("audio transfer model response:")
print(response)
