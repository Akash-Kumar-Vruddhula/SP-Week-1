from flask import Flask, url_for,redirect,render_template,request
import pickle

app = Flask(__name__)
@app.route("/",methods = ["POST", "GET"])
def index():
    if request.method== "POST":
        one = request.form["Sex"]
        two = request.form["Age"]
        three = request.form["Smoking"]
        four = request.form["No Of Times Smoked Per Day"]
        five = request.form["BPmedication"]
        six = request.form["Stroke"]
        seven = request.form["Hypertension"]
        eight = request.form["Diabetes"]
        nine = request.form["Cholesterol"]
        ten = request.form["SystolicBP"]
        eleven = request.form["DiastolicBP"]
        twelve = request.form["BMI"]
        thirteen = request.form["HeartRate"]
        fourteen = request.form["Glucose"]
        values = list(map(float,[one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen]))
        loaded_model = pickle.load(open("CHDPredictor.pkl", "rb"))
        estimate = loaded_model.predict([values])
        if estimate==0:
            estimated_output = "You Are Out Of Danger"
            colour = "green"
        else:
            estimated_output = "You Are In Danger, Get Yourself Checked By A Doctor ASAP!!"
            colour = "red"
        return render_template("index.html",estimated_output=estimated_output,colour=colour)
    return render_template("index.html")
app.run()

