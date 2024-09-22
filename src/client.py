import argparse

from flask_ml.flask_ml_client import MLClient
from flask_ml.flask_ml_server.constants import DataTypes

# Define the URL and set up client
AUDIO_STYLE_TRANSFER_MODEL_URL = "http://127.0.0.1:5000/audiotransfer"
client = MLClient(AUDIO_STYLE_TRANSFER_MODEL_URL)

# Set up command line argument parsing
parser = argparse.ArgumentParser(description="To parse text arguments")
parser.add_argument(
    "file_paths", metavar="file", type=str, nargs="+", help="Paths to input text files"
)
args = parser.parse_args()

# Prepare inputs based on command line arguments
data_type = DataTypes.AUDIO
inputs = [{"file_path": file_path} for file_path in args.file_paths]

# Send request to the model and print the response
response = client.request(inputs, data_type)
print("Audio transfer model response:")
print(response)
