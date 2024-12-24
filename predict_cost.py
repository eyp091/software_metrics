import joblib

def predict(ev):
    rf = joblib.load("rf_model.sav")
    return rf.predict(ev)