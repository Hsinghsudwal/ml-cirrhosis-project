#importing libraries and packages
import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from imblearn.combine import SMOTETomek

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.ensemble import GradientBoostingClassifier
import joblib
from utils import create_folder

create_folder('output') 

def read_data(path_name):
    data = pd.read_csv(path_name)
    return data

def process_data(data):
    cat = data.select_dtypes(include='object')
    num = data.select_dtypes(include='number')

    data['Age']= (data['Age']/365.25).round()
    data['Status'] = data['Status'].map({'C': 1, 'D': 0, 'CL': 2})

    for feature in cat:
        data[feature]=data[feature].fillna(data[feature].mode()[0])

    for i in num:
        data[i]=data[i].fillna(data[i].mean())
    
    le = LabelEncoder()
    for i in cat:
        data[i]=le.fit_transform(data[i])

    return data


### Modeling
def model_trainer(data):

    x = data.drop(['Status','ID'], axis=1)
    y = data['Status']

    smote = SMOTETomek()
    x_smote, y_smote = smote.fit_resample(x,y)

    X_train, X_test, y_train, y_test = train_test_split(x_smote,y_smote,test_size=0.2,random_state=42)

    # 2. GridSearchCV Gradient boosting
    param_grid = {
        "learning_rate": [0.1],
        "max_depth":[5],
        "n_estimators":[200]
    }

    # Initialize the Gradient Boosting model
    gbc = GradientBoostingClassifier(n_estimators=300,
                                 learning_rate=0.05,
                                 # random_state=42,
                                 max_features=5 )

    # Initialize GridSearchCV
    # grid_search = GridSearchCV(estimator=gbc, param_grid=param_grid, cv=3, n_jobs=-1)

    # Fit the model to the training data using GridSearchCV
    gbc.fit(X_train, y_train)

    # Model Training score
    print('Training Score: ', gbc.score(X_train, y_train))

    # Make predictions on the test set using the best model
    y_pred = gbc.predict(X_test)

    # Evaluate the model
    accuracy_best = round(accuracy_score(y_test, y_pred),2)

    
    with open('output/best_model.pkl','wb') as file:
            joblib.dump((gbc),file)
    # with open('deployment/best_model.pkl','wb') as file:
    #         joblib.dump((gbc),file)

    return accuracy_best


if __name__=='__main__':
    path='data/cirrhosis.csv'
    df=read_data(path)
    # print(df)
    data=process_data(df)
    # print(data)
    score =model_trainer(data)
    print('Models Score: ', score)
   
    
    