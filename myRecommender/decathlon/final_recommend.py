import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def cycle_recommend(form_data):
    le = LabelEncoder()
  #  df = pd.read_csv('decathlon/cycle.csv')

    data = pd.read_csv('decathlon/cycle.csv')

    data.Gender = le.fit_transform(data.Gender)
    data.Cycle_Type = le.fit_transform(data.Cycle_Type)
    data.Cycling_Reason = le.fit_transform(data.Cycling_Reason)

    c = DecisionTreeClassifier(criterion='entropy', min_samples_split=2)

    features = ['Gender',
                'Age',
                'Cycle_Type',
                'Cycle_id',
                'Cycling_Reason',
                'MRP']

    X_train, X_test, y_train, y_test = train_test_split(data[features], data.Cycle, test_size=0.20, random_state=0)

    dt = c.fit(X_train, y_train)

    print("Accuracy on training set: {:.3f}".format(c.score(X_train, y_train)))
    print("Accuracy on test set: {:.3f}".format(c.score(X_test, y_test)))

   # result = c.predict([[1, 22, 0, 2534222, 2, 10999]])

    actual_data = [form_data['Gender'],
                   form_data['Age'],
                   form_data['Cycle_Type'],
                   form_data['Cycle_id'],
                   form_data['Cycling_Reason'],
                   form_data['MRP']
                   ]

    result = c.predict([actual_data])


    return result[0]

    