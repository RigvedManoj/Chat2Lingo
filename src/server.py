from flask_ml.flask_ml_server import MLServer
from flask_ml.flask_ml_server.constants import DataTypes
from flask_ml.flask_ml_server.models import FileInput, ImageResult, ResponseModel

from text2audio import Text2AudioModel

# create an instance of the model
audio_transfer_model = Text2AudioModel()

# Create a server
server = MLServer(__name__)


# Create an endpoint
@server.route("/audiotransfer", DataTypes.IMAGE)
def audio_transfer(inputs: list[FileInput], parameters: dict):
    results = audio_transfer_model.convert(inputs)
    image_results = [
        ImageResult(file_path=res["file_path"], result=res["result"]) for res in results
    ]
    response = ResponseModel(results=image_results)
    return response.get_response()
