
import pandas as pd
import numpy as np
import os

def read_data():
    # Define raw data path
    raw_data_path = os.path.join(os.path.pardir, 'data', 'raw')
    train_file_path = os.path.join(raw_data_path, 'train.csv')
    test_file_path = os.path.join(raw_data_path, 'test.csv')
    # read data from cvs file
    train_df = pd.read_csv(train_file_path, index_col='PassengerId')
    test_df = pd.read_csv(test_file_path, index_col='PassengerId')
    test_df['Survived'] = -1000  # set a default value for survived column on test data
    combined_df = pd.concat((train_df, test_df), axis=0, sort=True)
    return combined_df

def processed_data(df):
    # use method chaining concept
    return (df
            # Create title attribute
            .assign(Title = lambda x : x.Name.map(get_clean_title))
            # working missing values
            .pipe(fill_missing_values)
            # Create Fare bin feature
            .assign(Fare_Bin = lambda x: pd.qcut(x.Fare, 4, labels=['very_low', 'low', 'high', 'very_high']))
            # Create Age state feature
            .assign(AgeState = lambda x : np.where(x.Age >= 18, 'Adult', 'Child'))
            .assign(FamilySize = lambda x : x.Parch + x.SibSp + 1)
            .assign(IsMother = lambda x :np.where(((x.Sex == 'female') & 
                                   (x.Age >= 18) & (x.Parch > 0) &(x.Title != 'Miss')), 1, 0))
            # Create Deck feature
            .assign(Cabin = lambda x: np.where(x.Cabin == 'T', np.nan, x.Cabin))
            .assign(Deck = lambda x : x.Cabin.map(get_deck))
            # features encoding
            .assign(IsMale = lambda x : np.where(x.Sex == 'male', 1, 0))
            .pipe(pd.get_dummies, columns=['Deck', 'Pclass', 'Title', 'AgeState', 'Fare_Bin', 'Embarked'])
            # Drop unnecessary column
            .drop(['Cabin', 'Name', 'Ticket', 'Parch', 'SibSp', 'Sex'], axis=1, inplace=True)
            # Reorder column
            .pipe(reorder_columns)
           )

# Define a function to extract the title of a person from their name
def get_title(name):
    first_name_with_title =  name.split(',')[1]
    title = first_name_with_title.split('.')[0]
    title = title.strip().lower()
    return title

def get_clean_title(name):
    title_group = {
        'mr': 'Mr',
        'mrs': 'Mrs',
        'miss': 'Miss',
        'master': 'Master',
        'don': 'Sir',
        'rev': 'Sir',
        'dr': 'Officer',
        'mme': 'Mrs',
        'ms': 'Mrs',
        'major': 'Officer',
        'lady': 'Lady',
        'sir': 'Sir',
        'mlle': 'Miss',
        'col': 'Officer',
        'capt': 'Officer',
        'the countess': 'Lady',
        'jonkheer': 'Sir',
        'dona': 'Lady'
    }
    title = get_title(name)
    return title_group[title]

def fill_missing_values(df):
    # Embarked
    df.Embarked.fillna('C', inplace=True)
    # Fare
    median_fare = combined_df.loc[
        (df.Pclass == 3) & (df.Embarked == 'S'), 'Fare'].median()
    df.Fare.fillna(median_fare, inplace=True)
    # Age
    age_title_median = df.groupby('Title').Age.transform('median')
    df.Age.fillna(age_title_median, inplace=True)
    return df

def get_deck(cabin):
    return np.where(pd.notnull(cabin), str(cabin)[0].upper(), 'Z')

def reorder_columns(df):
    # Reorder columns
    columns = [column for column in df.columns if column != 'Survived']
    columns = ['Survived'] + columns
    df = df[columns]
    return df

def write_data_to_csv(df):
    processed_data_path = os.path.join(os.path.pardir, 'data', 'processed')
    write_train_file_path = os.path.join(processed_data_path, 'train.csv')
    write_test_file_path = os.path.join(processed_data_path, 'test.csv')
    # train data
    df.loc[df.Survived != -1000].to_csv(write_train_file_path)
    # test data
    columns = [column for column in df.columns if column != 'Survived'] # exclude survived column
    df.loc[df.Survived == -1000, columns].to_csv(write_test_file_path)
    
if __name__ == '__main':
    df = read_data()
    df = processed_data(df)
    write_data_to_csv(df)
