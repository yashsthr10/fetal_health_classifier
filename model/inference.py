import pickle


#Loading the trained model
with open('D:\\Resume\\PROJECTS_1\\model\\xgboost_model.pkl', 'rb') as f:
    model = pickle.load(f,encoding='bytes')
