from copyreg import pickle
import numpy as np
import json
import pickle
import config


class LoanPrediction():
    def __init__(self,Gender,Married,Education,Self_Employed,Loan_Amount_Term,Credit_History,ApplicantIncomeLog,CoapplicantIncomeLog,LoanAmountLog,Property_Area):
        self.Gender = Gender
        self.Married = Married
        self.Education = Education
        self.Self_Employed = Self_Employed
        self.Loan_Amount_Term = Loan_Amount_Term
        self.Credit_History = Credit_History
        self.ApplicantIncomeLog = ApplicantIncomeLog
        self.CoapplicantIncomeLog = CoapplicantIncomeLog
        self.LoanAmountLog = LoanAmountLog
        self.Property_Area = "Property_Area_" + Property_Area
    
    def load_model(self):
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model = pickle.load(f)
        with open(config.JSON_FILE_PATH,"r") as f:
            self.json_data = json.load(f)
     
    def get_loan_status(self):
        self.load_model()

        test_array = np.zeros(len(self.json_data["columns"]))
        test_array[0] = self.json_data["Gender"][self.Gender]
        test_array[1] = self.json_data["Married"][self.Married] 
        test_array[2] = self.json_data["Education"][self.Education]
        test_array[3] = self.json_data["Self_Employed"][self.Self_Employed]
        test_array[4] = self.Loan_Amount_Term
        test_array[5] = self.Credit_History
        test_array[6] = self.ApplicantIncomeLog
        test_array[7] = self.CoapplicantIncomeLog
        test_array[8] = self.LoanAmountLog
        region_index = self.json_data["columns"].index(self.Property_Area)
        test_array[region_index] = 1
        print("test_array",test_array)

        Loan_Stat = self.model.predict([test_array])[0]
        return Loan_Stat

