import numpy as np
from src.modeling.selection import multilabel_train_test_split
from sklearn.datasets import make_multilabel_classification

def test_multilabel_train_test_split():
    X, y = make_multilabel_classification(
        n_samples=1000,
        n_features=100,
        n_classes=10,
        n_labels=2,
        random_state=1)

    X_train, X_test, y_train, y_test = multilabel_train_test_split(
        X, y, test_size=0.2, random_state=1)
        
    assert type(X_train) == type(X_test) == type(y_train) == type(y_test) == np.ndarray
