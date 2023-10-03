'''
Your task here is to complete the rf_predict_actual function.
It returns the predicted and actual classes for our galaxies using a random forest 10-fold with cross validation.

You should use the RandomForestClassifier class from the sklearn.ensemble module
It can be instantiated with: rfc = RandomForestClassifier(n_estimators=n_estimators)

rf_predict_actual takes two arguments: the data used throughout this activity and the number of estimators (n_estimators) to be used in the random forest.
The function should return two NumPy arrays containing the predicted and actual classes respectively.

You can copy and paste the functions from previous questions
However, we have provided the generate_features_targets function in the support library.
'''

import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict
from sklearn.ensemble import RandomForestClassifier
from support_functions import generate_features_targets, plot_confusion_matrix, calculate_accuracy


# complete this function to get predictions from a random forest classifier
def rf_predict_actual(data, n_estimators):
  # generate the features and targets
  features, targets = generate_features_targets(data)

  # instantiate a random forest classifier using n estimators
  rfc = RandomForestClassifier(n_estimators=n_estimators)
  
  # get predictions using 10-fold cross validation with cross_val_predict
  predicted = cross_val_predict(rfc, features, targets, cv = 10)

  # return the predictions and their actual classes
  return predicted, targets


if __name__ == "__main__":
  data = np.load('galaxy_catalogue.npy')

  # get the predicted and actual classes
  number_estimators = 50              # Number of trees
  predicted, actual = rf_predict_actual(data, number_estimators)

  # calculate the model score using your function
  accuracy = calculate_accuracy(predicted, actual)
  print("Accuracy score:", accuracy)

  # calculate the models confusion matrix using sklearns confusion_matrix function
  class_labels = list(set(actual))
  model_cm = confusion_matrix(y_true=actual, y_pred=predicted, labels=class_labels)

  # plot the confusion matrix using the provided functions.
  plt.figure()
  plot_confusion_matrix(model_cm, classes=class_labels, normalize=False)
  plt.show()
