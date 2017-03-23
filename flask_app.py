from flask import Flask, render_template, request

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["use_reloader"]=False


@app.route("/",methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template("main_page.html")

    elif request.method == 'POST':
        expression = request.form.get('expression')
        result = eval(expression)
        return render_template("resultado.html", result=result)
