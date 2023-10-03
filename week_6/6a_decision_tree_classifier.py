'''
Write functions to split data, generate features and then train a decision tree classifier
'''

import numpy as np
from sklearn.tree import DecisionTreeClassifier


# splitdata_train_test function here
def splitdata_train_test(data, fraction_training):
  # random shuffle to prevent bias
  np.random.shuffle(data)
  split_index = int(fraction_training*len(data))
  return data[:split_index], data[split_index:]

# generate_features_targets function here
def generate_features_targets(data):
  targets = data['class']
  features = np.empty(shape=(len(data), 13))
  features[:, 0] = data['u-g']
  features[:, 1] = data['g-r']
  features[:, 2] = data['r-i']
  features[:, 3] = data['i-z']
  features[:, 4] = data['ecc']
  features[:, 5] = data['m4_u']
  features[:, 6] = data['m4_g']
  features[:, 7] = data['m4_r']
  features[:, 8] = data['m4_i']
  features[:, 9] = data['m4_z']
  features[:, 10] = data['petroR50_u']/data['petroR90_u']
  features[:, 11] = data['petroR50_r']/data['petroR90_r']
  features[:, 12] = data['petroR50_z']/data['petroR90_z']
  return features, targets

# complete this function by splitting the data set and training a decision tree classifier
def dtc_predict_actual(data):
  # split the data into training and testing sets using a training fraction of 0.7
  train, test = splitdata_train_test(data, 0.7)

  # generate the feature and targets for the training and test sets
  # i.e. train_features, train_targets, test_features, test_targets
  train_features, train_targets = generate_features_targets(train)
  test_features, test_targets = generate_features_targets(test)

  # instantiate a decision tree classifier
  dtc = DecisionTreeClassifier()

  # train the classifier with the train_features and train_targets
  dtc.fit(train_features, train_targets)

  # get predictions for the test_features
  predictions = dtc.predict(test_features)

  # return the predictions and the test_targets
  return predictions, test_targets



if __name__ == '__main__':
  data = np.load('galaxy_catalogue.npy')
    
  predicted_class, actual_class = dtc_predict_actual(data)

  # Print some of the initial results
  print("Some initial results...\n   predicted,  actual")
  for i in range(10):
    print("{}. {}, {}".format(i, predicted_class[i], actual_class[i]))
 