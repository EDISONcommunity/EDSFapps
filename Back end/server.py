from flask import Flask, request, jsonify, make_response # server
import json # json handling
import re # regex
from flask_cors import CORS, cross_origin # browser requests
import sys # prints
import shutil # delete previous results
from tika import parser # Pdf parser
import json # json module for API responses

# External files for functionalities
import similarity_calc as similarity
import cv_info_extractor as cv_info_extractor

# Server configuration
app = Flask(__name__)
CORS(app, supports_credentials=True)
HOST = "localhost"
PORT = 5000

@app.route('/uploadcv', methods=['POST'])
def uploadcv():
    if request.method == 'POST':
        try:
            print('Calculating graph for CV...', file=sys.stderr)
            # Get text data
            document = request.get_data()
            text = parser.from_buffer(document)
            text = text['content']
            # Remove new lines
            text = text.replace('\n', ' ')
            text = text.replace('–', '-')
            # Remove unnecessary white space
            text = ' '.join(text.split())

            # Calculate similarity
            compObj = similarity.calculateSim(text)
            print(compObj, file=sys.stderr)

            # Get cv info
            cv_info = cv_info_extractor.get_cv_info(text)
            print(cv_info, file=sys.stderr)

            return jsonify({"text": text, "competences": compObj, "cv_info": cv_info})
        except KeyError:
            return jsonify({"response": {}, "statusCode": 404, "message": "Key error"})
        except ValueError:
            return jsonify({"response": {}, "statusCode": 404, "message": "Value error"})
        except:
            return jsonify({"response": {}, "statusCode": 404, "message": "Unknown error"})

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, threaded=True) # server start