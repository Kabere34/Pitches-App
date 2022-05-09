from flask import Flask,render_template

app=Flask(__name__)

posts=[
  {
    'author': 'John',
    'title':'blog post',
    'content':'First post',
    'date_posted':'April 14, 2014',
  },
  {
    'author': 'Jane',
    'title':'video post',
    'content':'Second post',
    'date_posted':'July 14, 2015',
  }
]


@app.route("/")
def home():
    return render_template('index.html',posts=posts)

@app.route("/pickup")
def about():
    return render_template('pickup.html')

if __name__ == "__main__":
  app.run(debug=True)
