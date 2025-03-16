import joblib

try:
    model = joblib.load('model.pkl')
    print(type(model))
    print(model.get_params())
except Exception as e:
    print(f"Joblib error: {e}")