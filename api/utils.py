# import joblib
# import numpy as np
#
# # Load the trained model (e.g., a scikit-learn model)
# #MODEL_PATH = 'path/to/model.pkl'
# model = joblib.load(MODEL_PATH)
#
# def predict(features):
#     # Ensure features are in the right shape for prediction
#     features = np.array(features).reshape(1, -1)
#     prediction = model.predict(features)
#     return prediction[0]  # Return the first result