from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def

if __name__ == '__main__':
    app.run(debug=True)
    
