import pickle


#Loading the trained model
with open('xgboost_model.pkl', 'rb') as f:
    model = pickle.load(f,encoding='bytes')
