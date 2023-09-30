import os

from datetime import date as dt

from flask import Flask, render_template

web_name = os.environ["hello"]
pass_code = os.environ["lolol"]
app = Flask("__name__")

today = dt.today()
print(today)
#ok good lol well ima go add the copyrigth
#i did not, check code
the_year = today.year
the_month = today.month
today=f"{the_month}/{the_year}"
if the_year > 2039:
  today="the future"
time = 2023
@app.route("/")
def hello_world():
  lolpo=today
  year = time
  return render_template("lol.html", num=year, lol=lolpo)
#@app.route("/")
#def hello_world():
#    return render_template("login-user.php")

@app.route("/goofy")
def goofy_world():
	year = time
	return render_template("goofy.html", num=year)

@app.route("/two")
def two_world():
	year = time#so if u change this in 2024 u just change 'time' var at top im get jerkface now
	return render_template("lol1.html", num=year)

@app.route("/lol")
def lol_world():
	year = time
	return render_template("lolol.html", num=year)
@app.route(f"/{web_name}")
def youdontknowwhoiam_world():
	year = time
	return render_template("youdontknowwhoiam.html", num=year)

@app.route("/youdontknowwhoiam")
def youknow_world():
	return render_template("troll.html")

@app.route("/download-virus")
def infected_world():
	return render_template("virus.html")

@app.route("/the-spectre-by-alan-walker")
def the_spectre_world():
	return render_template("spectre.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)
