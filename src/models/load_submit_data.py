
import os, pickle
import pandas as pd
import numpy as np

def load_model_scaler():
    model_file_path = os.path.join('models', 'lr_model.pkl')
    scaler_file_path = os.path.join('models', 'lr_scaler.pkl')
    # open the files to write
    model_file_pickle = open(model_file_path, 'rb')
    scaler_file_pickle = open(scaler_file_path, 'rb')

    # persist the model and scaler
    clf_loaded = pickle.load(model_file_pickle)
    scaler_loaded = pickle.load(scaler_file_pickle)

    model_file_pickle.close()
    scaler_file_pickle.close()
    return (clf_loaded, scaler_loaded)


# Define a function to get submission file
def get_submission_file(model, filename, scaler):
    test_file_path = os.path.join('data', 'processed', 'test.csv')
    # Convert to matrix
    test_df = pd.read_csv(test_file_path, index_col='PassengerId')
    test_X = test_df.values.astype('float')
    X_test_scaled = scaler.transform(test_X)
    # get test predictions
    test_predictions = model.predict(X_test_scaled)
    submission_df = pd.DataFrame({'PassengerId': test_df.index, 'Survived': test_predictions})
    # get path and write result to csv
    submission_data_path = os.path.join('data', 'external')
    submission_file_path = os.path.join(submission_data_path, filename)

    submission_df.to_csv(submission_file_path, index=False)
