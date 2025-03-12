import pytest
from src.train import train

#Unit tests for the training script
def test_train():
    model = train()
    assert model is not None, "Model should not be None"