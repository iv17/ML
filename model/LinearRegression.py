from model.SpeedDate import SpeedDate
import statsmodels.formula.api as sm
import numpy as np
from sklearn.model_selection import train_test_split
import sklearn.linear_model as linear_model
from sklearn.preprocessing import StandardScaler
from  sklearn.metrics import accuracy_score

"""
Scaling all features to same range.
"""


def feature_scaling(data):
    sc_data = StandardScaler()
    return sc_data.fit_transform(data)


"""
Building the optimal model using Backward Elimination.
"""


def backward_elimination(data, dependent):
    # Adding column of ones at matrix of features
    data = np.append(arr=np.ones((len(data), 1)).astype(int), values=data, axis=1)
    # Create new optimal matrix of features. At the end it will contain only features
    # that are statistically significant and has strongest impact to dependent variable. P-val < 0.05
    data_opt = data[:, [1, 2, 4, 7, 8, 10]]
    # Ordinary Least Squares
    regressor_OLS = sm.OLS(endog=dependent, exog=data_opt).fit()
    # print(regressor_OLS.summary())
    return data_opt


def process_data():
    # load data from database
    db_dates = SpeedDate.select()
    dates = []

    # put every row into list and add it to dates
    for d in db_dates:
        dates.append(SpeedDate.to_list(d))

    # scale features
    # dates = feature_scaling(dates)

    dates = np.array(dates)

    # independent variables
    x_dates = dates[:, 1:]
    # scale features
    x_dates = feature_scaling(x_dates)

    # dependent variable
    y_dates = dates[:, 0]

    # optimized dependent variables(removed redundant)
    dates_opt = backward_elimination(x_dates, y_dates)

    return dates_opt, y_dates


def regression(dates_opt, y_dates):
    # split set to train/test
    x_train, x_test, y_train, y_test = train_test_split(dates_opt, y_dates, test_size=.25, random_state=0)

    # regression
    regressor = linear_model.LogisticRegression()
    # fit linear model
    regressor.fit(x_train, y_train)

    # make prediction
    y_pred = regressor.predict(x_test)

    # test accuracy
    predictions = np.array(y_pred, dtype=int)
    print("Regression Accuracy: ", accuracy_score(y_test, predictions))


if __name__ == "__main__":
    dates_opt, y_dates = process_data()
    regression(dates_opt, y_dates)
