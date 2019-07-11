import itertools
from sklearn.metrics import confusion_matrix
import sklearn.metrics as metrics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def evaluate_classifier(y_test, y_pred, classes = ['Not Degradable', 'Degradable'], normalize=False):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`

    Paramerters :
    -------------
    y_test : Numpy Array or Pandas DataFrame
        True Values for the target

    y_pred : Numpy Array or Pandas DataFrame
        Predicted values for the target

    classes : List of Strings
        Labels for displaying 0 and 1 in the plot , optional

    normalize : Bool
        Whether or not to schow normalized vs absolute Values in the plot

    Returns :
    ---------
    result_dict : Dictionary
        Dictionary Containing accuracy, precission, sensitivity, f1 scores as floats and a list of the confusion matrix values
        
    """
    cm = confusion_matrix(y_test,y_pred)
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion Matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('Confusion matrix')
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black", fontsize = 13)
    plt.tight_layout()
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.grid(b=None)
    plt.show()
    
    acc = metrics.accuracy_score(y_test, y_pred)
    prec = metrics.precision_score(y_test, y_pred)
    sens = metrics.recall_score(y_test, y_pred)
    f_1 = 2*(prec*sens)/(prec+sens) 
    print('Our Accuracy is:', acc)
    print('Our Precision is:', prec)
    print('Our Sensitivity is:', sens )
    print('Our F-Score is:', f_1)
    
    result_dict = {"accuracy": acc,
                  "precission": prec,
                  "sensitivity": sens,
                  "f_1" : f_1,
                  "confusion_matrix" : confusion_matrix(y_test,y_pred)}
    #results_dict_list.append(result_dict)
    return result_dict

def plot_coefs(X_train,model, return_nulls = True, legend = True):
    """Function for Plotting a Bar Chart of a Linear models Coefficients
    
    Parameters :
    ------------
    X_train : Pandas DataFrame 
        Training Features
    model : sklearn ModelObject 
        Linear or Logistic Regression model with .coef_ attribute
    return_null: bool 
        whether or not to return Features that have been pushed a coefficent value of zero
    legend: bool
        show legend for each bar
    
    Returns :
    -----------
    return_null: list
        Features with coefficient of zero
        
    plot_coef: Pandas DataFrame 
        DataFrame with Feature Name and coefficient"""

    plt.style.use("seaborn")
    fig = plt.figure(figsize = (16,15))
    plot_coef = pd.DataFrame(model.coef_[0].T, index=X_train.columns, columns = ["coeff"]).sort_values("coeff")
    plot_coef.plot(kind = "bar")
    if legend:
        plt.legend()
    plt.title("Feature Importance", fontdict = {"fontsize": 16})
    plt.show()

    if return_nulls:
        return plot_coef.loc[plot_coef.coeff ==0].index
    return plot_coef

def compare_models(results_dict_list, names_list = None):
    """Compares different models and pliots the mectrics values.

    Parameters
    ----------
    results_dict_list : list of dictionaries
        List of multiple scoring metrics of a model as key value pairs in a dictionary.

    names_list : list of strings 
        List with model Names for identification, optional.

    Returns:
    ----------
    res_df : Pandas DataFrame
        Pandas DataFrame Object containing the Scoring metrics for each model.
    """
    res_df = pd.DataFrame(columns = results_dict_list[0].keys())
    for model in results_dict_list:
        res_df.loc[len(res_df)] = list(model.values())
    if names_list:
        res_df.index = names_list
    return res_df