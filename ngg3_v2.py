from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/ngg3", methods = ["GET", "POST"])
def ngg_3():
    if request.method == "POST":
        min = int(request.form["min"])
        max = int(request.form["max"])
        feedback = request.form["feedback"]
        guess = (min + max) // 2
        if feedback == "small":
            min = guess + 1
        elif feedback == "big":
            max = guess - 1
        elif feedback == "win":
            return f"<h1>Yes! I guessed it: {guess}</h1>"
        guess = (min + max) // 2
    else:
        min = 1
        max = 1000
        guess = (min + max) // 2
    return render_template("ngg3_v2_w.html", guess=guess, min=min, max=max)

if __name__ == "__main__":
    app.run(debug=True)
