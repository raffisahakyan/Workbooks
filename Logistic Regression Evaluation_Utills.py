import numpy as np

def accuracy(y_true, y_pred):
    """
    Computes accuracy
    :param truth_values: true values
    :param predicted_values: predictions

    :return: accuracy
    """
    ### YOUR CODE HERE ###
    #accuracy=accuracy_score(truth_values, predicted_values)
    tp = sum((y_true==1) & (y_pred==1))
    tn = sum((y_true==0) & (y_pred==0))
    fn = sum((y_true==1) & (y_pred==0))
    fp = sum((y_true==0) & (y_pred==1))
    
    accuracy=(tp+tn)/(tp+tn+fp+fn) 
    ######################
    return accuracy

def precision(y_true, y_pred):
    """
    Computes precision
    :param truth_values: true values
    :param predicted_values: predictions

    :return: precision
    """
    ### YOUR CODE HERE ###    


    tp = sum((y_true==1) & (y_pred==1))
    fp = sum((y_true==0) & (y_pred==1))
    
    precision=tp/(tp+fp)  
    ######################
    return precision


def recall(y_true, y_pred):
    """
    Computes recall
    :param truth_values: true values
    :param predicted_values: predictions

    :return: recall
    """
    ### YOUR CODE HERE ###


    tp = sum((y_true==1) & (y_pred==1))
    fn = sum((y_true==1) & (y_pred==0))
    recall = tp/(tp+fn) 
    ######################
    return recall

