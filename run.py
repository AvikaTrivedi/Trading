from flask import Flask, jsonify
import gdown
app = Flask(__name__)

@app.route('/run-colab')
def run_colab():
    gdown.download('https://colab.research.google.com/drive/1fzg2BPpA-lrA0AkbH-69-2_46Mk_MA3V', 'Another copy of tradingBot.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')
