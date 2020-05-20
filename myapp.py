from flask import Flask, render_template
import nlp_test
import graph
import os

app = Flask(__name__)



def calculate(coef, x):
    l = len(coef) - 1
    s = 0
    for i in range(len(coef)):
        s += (x**i) * coef[l-i]
    return s

classifier = None
runOnce = True
accuracy = ""

@app.route("/")
def home():
    global runOnce
    global classifier
    global accuracy
    if runOnce:
        tup = nlp_test.train_model()
        classifier = tup[0]
        accuracy = tup[1]
        runOnce = False
    return render_template('index.html')

@app.route("/aapl")
def appl():
    global classifier
    output = nlp_test.main("apple", classifier)
    output = output.replace("\n", "<br>")
    tup = graph.graph("AAPL")
    plot_url = tup[0]
    coef = tup[1]
    x = tup[2] + 1
    predicted_value = calculate(coef, x)
    return render_template('page.html', name="Apple Prediction", output=output, 
        accuracy=accuracy, plot_url=plot_url, predicted_value=predicted_value)

@app.route("/uber", methods=["GET"])
def uber():
    global classifier
    output = nlp_test.main("uber", classifier)
    output = output.replace("\n", "<br>")
    tup = graph.graph("UBER")
    plot_url = tup[0]
    coef = tup[1]
    x = tup[2] + 1
    predicted_value = calculate(coef, x)
    return render_template('page.html', name="Uber Prediction", output=output, 
        accuracy=accuracy, plot_url=plot_url, predicted_value=predicted_value)

@app.route("/lyft")
def lyft():
    global classifier
    output = nlp_test.main("lyft", classifier)
    output = output.replace("\n", "<br>")
    tup = graph.graph("LYFT")
    plot_url = tup[0]
    coef = tup[1]
    x = tup[2] + 1
    predicted_value = calculate(coef, x)
    return render_template('page.html', name="Lyft Prediction", output=output, 
        accuracy=accuracy, plot_url=plot_url, predicted_value=predicted_value)


if __name__ == '__main__':
    app.run(debug=True)