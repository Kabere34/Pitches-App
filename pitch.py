from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/pickup")
def about():
    return render_template('pickup.html')

if __name__ == "__main__":
  app.run(debug=True)
