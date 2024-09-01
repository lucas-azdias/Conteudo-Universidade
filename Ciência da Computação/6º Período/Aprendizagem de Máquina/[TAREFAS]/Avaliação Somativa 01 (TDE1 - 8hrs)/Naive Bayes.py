# ENVIRONMENT
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt

import numpy as np

import sklearn.datasets
import sklearn.metrics
import sklearn.model_selection
import sklearn.naive_bayes


from typing import Iterable


# LOADING MODEL
# Class for holding each model dataset
class model_dataset:

    def __init__(self, data:Iterable, labels:Iterable, random_seed:int) -> None:
        self.data = data
        self.labels = labels

        # Defining the random seed
        self.random_seed = random_seed
        
        # Splitting the model dataset into train/test groups
        self.train_data, self.test_data, self.train_labels, self.test_labels = sklearn.model_selection.train_test_split(
            data,
            labels,
            train_size=0.7,
            test_size=0.3,
            random_state=random_seed
        )


    def plot(self) -> None:
        # Ploting model dataset function
        _, ax = plt.subplots()
        for n_class in range(0, len(np.unique(self.labels))):
            ax.scatter(
                self.data[self.labels==n_class, 0],
                self.data[self.labels==n_class, 1],
                c=tuple(mcolors.BASE_COLORS.keys())[n_class],
                label=str(n_class)
            )
        ax.legend()
        plt.show()
    

    def analysis(self, predicted_labels:Iterable) -> None:
        # Model analysis function
        print("Accuracy Score:", sklearn.metrics.accuracy_score(self.test_labels, predicted_labels), end="\n\n")
        print(sklearn.metrics.classification_report(self.test_labels, predicted_labels))

        cm = sklearn.metrics.confusion_matrix(self.test_labels, predicted_labels, labels=np.unique(self.train_labels))
        sklearn.metrics.ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=np.unique(self.train_labels)).plot()


# Loading the models datasets
breast_cancer_model = model_dataset(*sklearn.datasets.load_breast_cancer(return_X_y=True), p=2, k_neighbors=5, random_seed=9999)
wine_model = model_dataset(*sklearn.datasets.load_wine(return_X_y=True), p=2, k_neighbors=5, random_seed=9999)

# Ploting models datasets
breast_cancer_model.plot()
wine_model.plot()


# SCIKIT-LEARN MODEL IMPLEMENTATION
sk_nb = sklearn.naive_bayes.GaussianNB()

# Train the model
sk_nb.fit(breast_cancer_model.train_data, breast_cancer_model.train_labels)

# Test the model
predicted_labels = sk_nb.predict(breast_cancer_model.test_data)

# Model analysis
breast_cancer_model.analysis(predicted_labels)


# OWN MODEL IMPLEMENTATION
class naive_bayes():

    def __minkowski(self, u:Iterable, v:Iterable) -> float:
        if len(u) != len(v):
            raise ValueError("Vectors of different sizes passed as arguments")
        
        # distance = 0
        # for i in range(0, len(u)):
        #     distance += np.power(np.abs(u[i] - v[i]), self.p)
        
        distance = np.sum(np.power(np.abs(np.subtract(u, v)), self.p))

        distance = np.power(distance, np.divide(1, p))

        return distance


    def fit(self, data, labels) -> None:
        self.data = data
        self.labels = labels
    

    def predict(self, data) -> tuple:
        labels = list()
        for instance in data:
            distances = list()
            for i in range(0, len(self.data)):
                distances.append((self.__minkowski(instance, self.data[i]), self.labels[i]))
            
            distances.sort(key=lambda x: x[0])

            votes = {k: 0 for k in np.unique(self.labels)}
            for i in range(0, self.k_neighbors):
                votes[distances[i][1]] += 1
            
            # print(votes, max(*votes.items(), key=lambda x: x[1])[0])

            labels.append(max(*votes.items(), key=lambda x: x[1])[0])
        
        return tuple(labels)


own_nb = naive_bayes()

# Train the model
own_nb.fit(breast_cancer_model.train_data, breast_cancer_model.train_labels)

# Test the model
predicted_labels = own_nb.predict(breast_cancer_model.test_data)

# Model analysis
breast_cancer_model.analysis(predicted_labels)
