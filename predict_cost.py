import joblib

def predict(ev):
    rf = joblib.load("rfc_model.sav")
    return rf.predict(ev)