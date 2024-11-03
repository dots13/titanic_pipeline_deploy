#import logging

import pytest
from sklearn.model_selection import train_test_split

from classification_model.config.core import config
from classification_model.processing.data_manager import load_raw_dataset


#logger = logging.getLogger(__name__)
#logging.basicConfig(level=logging.INFO)  # Set logging level to INFO


@pytest.fixture
def sample_input_data():
    # Load raw dataset
    data = load_raw_dataset(file_name=config.app_config.raw_data_file)
    #logger.info("Raw dataset loaded successfully. Dataset shape: %s", data.shape)
    #logger.info("Model configuration: %s", config.classification_model_configuration)

    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data,  # predictors
        data[config.classification_model_configuration.target],
        test_size=config.classification_model_configuration.test_size,
        # we are setting the random seed here
        # for reproducibility
        random_state=config.classification_model_configuration.random_state,
    )

    #logger.info("Data split into train and test sets.")
    #logger.info("X_test shape: %s", X_test.shape)

    return X_test

