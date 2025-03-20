from flask import Flask, render_template, request

app = Flask(__name__)

feedback_data = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        feedback = request.form["feedback"]
        feedback_data.append({"name": name, "email": email, "feedback": feedback})
        return render_template("thankyou.html")
    return render_template("contact.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html", feedback_data=feedback_data)

if __name__ == "__main__":
    app.run(debug=True)