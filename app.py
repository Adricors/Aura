from flask import Flask, render_template, request, jsonify
import ollama

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    
    prompt = f"""
    Eres Aura, un compañero de apoyo emocional. Escucha al usuario con empatía y comprensión.
    Sé cálido, amable, y nunca juzgues. Invita a reflexionar con preguntas suaves cuando sea adecuado.
    El usuario dice: "{user_input}"
    Tu respuesta:
    """

    response = ollama.chat(model="llama3", messages=[
        {"role": "user", "content": prompt}
    ])

    return jsonify({"response": response["message"]["content"]})

if __name__ == "__main__":
    app.run(debug=True)
