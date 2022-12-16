from flask import Flask, jsonify, request, render_template
from Data.utils import LoanPrediction
import config

app = Flask(__name__)

@app.route("/")
def home_api():
    return render_template("login.html")

@app.route("/prediction_loan")
def prediction_loan():
    data = request.form
    Gender = data["Gender"]
    Married = data["Married"]
    Education = data["Education"]
    Self_Employed = data["Self_Employed"]
    Loan_Amount_Term = int(data["Loan_Amount_Term"])
    Credit_History = eval(data["Credit_History"])
    ApplicantIncomeLog = eval(data["ApplicantIncomeLog"])
    CoapplicantIncomeLog = eval(data["CoapplicantIncomeLog"])
    LoanAmountLog = eval(data["LoanAmountLog"])
    Property_Area= data["Property_Area"]

    loan_pred = LoanPrediction(Gender,Married,Education,Self_Employed,Loan_Amount_Term,Credit_History,ApplicantIncomeLog,CoapplicantIncomeLog,LoanAmountLog,Property_Area)
    status = loan_pred.get_loan_status()
    return jsonify({"Result":f"Status of your loan approval is: {status}"})

if __name__ == "__main__":
     app.run()

    