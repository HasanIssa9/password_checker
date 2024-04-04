import dill
import numpy as np

model = dill.load(open("xgb_classifier.pkl", "rb"))
vectorizer = dill.load(open("vectorizer.pkl", "rb"))

while 1:
    password = input("Enter your password : ")
    if len(password) > 6:
        pred = np.array([password])
        x_pred = vectorizer.transform(pred)
        predicted = model.predict(x_pred)
        if predicted == 1:
            print("Password is Medium")
        elif predicted == 0:
            print("Password is Weak")
        elif predicted == 2:
            print("Password is Strong")
    else:
        print("Your password must be at least 6 characters long. Please choose a stronger password for better security.")
