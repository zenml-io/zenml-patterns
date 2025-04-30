from typing import Tuple

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from zenml import pipeline, step
from zenml.config import DockerSettings


@step
def load_data() -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Load the iris dataset and split it into train and test sets."""
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )
    return X_train, X_test, y_train, y_test

@step(enable_cache=False)
def train_model(
    X_train: np.ndarray,
    y_train: np.ndarray,
    n_estimators: int = 100,
) -> RandomForestClassifier:
    """Train a random forest classifier."""
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
    model.fit(X_train, y_train)
    return model

@pipeline(
    settings = {"docker": 
        DockerSettings(
            requirements="requirements.txt",
            python_package_installer="uv",
            prevent_build_reuse=True
        )
    }
)
def simple_ml_pipeline():
    """A simple ML pipeline that loads data, trains a model, and evaluates it."""
    # Load and split the data
    X_train, X_test, y_train, y_test = load_data()
    
    # Train the model
    model = train_model(X_train, y_train)
