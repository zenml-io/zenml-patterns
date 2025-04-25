__all__ = ['train']

import site
site.main()

from zenml import step
from demo.training import train_model

@step
def train():
    train_model()
