from flask import Flask, redirect, url_for, render_template, request, session
import integrate
#for permamnent sessions we need to define how long it lasts, eqv of stay logged in option
app=Flask(__name__)
#session data is encrpyted/decrypted using a session key without which we get an error
app.secret_key="hello"
@app.route("/", methods=["POST","GET"])
def login():
	if request.method == "POST":
		user=request.form["uname"]
		pword=request.form["pword"]
		if((user=="kanak" and pword=="potdar") or (user=="anant" and pword=="gadodia") or (user=="harshitha" and pword=="koppisetty") or (user=="anmolika" and pword=="goyal") or (user=="arpit" and pword=="kupadia") or (user=="ruchi" and pword=="gadodia")):
			session["user"]=user
			return redirect(url_for("user"))
		else:
			return render_template("loginpage.html")	
	elif "user" in session: #then the method is get
		#check if person is already logged in
		return redirect(url_for("user"))
	else:
		return render_template("loginpage.html")

@app.route("/user", methods=["POST","GET"])
def user():
	if "user" in session:
		user=session["user"]
		if user=="kanak":
			return render_template("prof1.html")
		elif user=="anant":
			return render_template("prof2.html")
		elif user=="harshitha":
			return render_template("prof3.html")
		elif user=="anmolika":
			return render_template("prof4.html")
		elif user=="arpit":
			return render_template("prof5.html")
		elif user=="ruchi":
			return render_template("profdoc1.html")
	else:
		return redirect(url_for("/"))


@app.route("/exer", methods=["POST", "GET"])
def exer():
	return render_template("perfEx.html")

@app.route("/fc", methods=["POST", "GET"])
def fc():
	print("1")
	a=integrate.controller("anant",10)
	a=int(a*100)
	print("\n\nout of controller\n\n")
	return render_template("resultdisptemplate.html", similaritypercentage=a)

@app.route("/pat1", methods=["POST", "GET"])
def pat1():
	return render_template("prof1.html")
@app.route("/pat2", methods=["POST", "GET"])
def pat2():
	return render_template("prof2.html")
@app.route("/pat3", methods=["POST", "GET"])
def pat3():
	return render_template("prof3.html")
#	return render_template("codetest2.html", val1=e, val2=f, val3=g, val4=h)


@app.route("/res1", methods=["POST", "GET"])
def res1():
	return render_template("resultdisp1.html",)
@app.route("/res2", methods=["POST", "GET"])
def res2():
	return render_template("resultdisp2.html")
@app.route("/res3", methods=["POST", "GET"])
def res3():
	return render_template("resultdisp3.html")


@app.route("/logout")
def logout():
	session.pop("user", None)
	return redirect(url_for("login"))
#removing session data to logout

if __name__ == "__main__":
	app.run(debug=True)

#if you close the browser session data is deleted