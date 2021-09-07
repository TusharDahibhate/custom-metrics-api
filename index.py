from flask import Flask

app = Flask(__name__)

@app.route("/apis/custom.metrics.k8s.io/v1beta1/")
def home():
    return str(1)
    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=6440, ssl_context=('localhost.crt', 'localhost.key'))