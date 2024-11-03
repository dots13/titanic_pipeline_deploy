from sklearn.model_selection import train_test_split

from classification_model.config.core import config
from classification_model.pipeline import titanic_pipe
from classification_model.processing.data_manager import load_dataset, save_pipeline


def run_training() -> None:
    """
    Train the model.
    """

    # read training data
    data = load_dataset(file_name=config.app_config.raw_data_file)

    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.classification_model_configuration.features],  # predictors
        data[config.classification_model_configuration.target],
        test_size=config.classification_model_configuration.test_size,
        random_state=config.classification_model_configuration.random_state,
    )

    # fit model
    titanic_pipe.fit(X_train, y_train)

    # persist trained model
    save_pipeline(pipeline_to_persist=titanic_pipe)


if __name__ == "__main__":
    run_training()

