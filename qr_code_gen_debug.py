

from flask import Flask, request, jsonify, send_file
import qrcode
from qrcode.exceptions import DataOverflowError
from io import BytesIO
from PIL import Image

app = Flask(__name__)

@app.route("/qr", methods=["GET"])
def generate_qr():
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400
    try:
        qr = url
        img = qrcode.make(qr)
        img_io = BytesIO()
        img.save(img_io, "PNG") # to display the imge back as repsonse of the API.
        #img.save("qr_code.jpg", "JPEG") - to save the image into working directory
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png')
    except DataOverflowError as e:
        return jsonify({"error": "Data Overflow Error: Provided data is too large"}), 400

if __name__ == "__main__":
    app.run(debug=True)
    
# After uploading to pythonwhere, use this to generate QR: https://mak7bit.pythonanywhere.com/qr?url=