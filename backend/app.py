from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/generate-questions", methods=["POST"])
def generate_questions():
    return jsonify({
        "questions": [
            "Explain OOP principles.",
            "What is your strongest technical skill?"
        ]
    })

if __name__ == "__main__":
    app.run(debug=True)
