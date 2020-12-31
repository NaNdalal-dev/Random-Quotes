from flask import *
from quotes import Quote
from random import randint,choice

app = Flask(__name__)
bgs=["#4DCCFF","#FF9156","#5F67EC","#F67162"]

@app.route("/")
def home():
	num=randint(1,2706)
	color=choice(bgs)
	q=Quote(num)
	author=str(q['AUTHOR'])
	quote=q['QUOTE']
	nan="nan"
	return render_template("index.html", quote=quote, author=author, nan=nan, color=color)

@app.route("/",methods=["POST"])
def home2():
	return redirect(url_for("home"))
	
if __name__ == "__main__":
	app.run(debug=True,port=8080)
