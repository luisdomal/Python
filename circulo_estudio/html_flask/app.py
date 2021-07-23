from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/index", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "POST":
    resultado = request.form["primer_cadena"] + request.form["segunda_cadena"]
    print("Ejecutando POST")
    return render_template('index.html', resultado = resultado)

  print("Ejecutando GET")
  return render_template('index.html')