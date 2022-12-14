# Import Standard Modules
import os
import pytest

# Set root path
os.chdir(os.environ['YOLO_OBJECT_DETECTION_PATH'])

# Import Package Modules
from packages.pytest_test.test_utils_fixtures import test_object_detector
from packages.object_detection.object_detection import ObjectDetector
from packages.utils.utils import read_configuration


def test_environment_variable(test_object_detector: ObjectDetector):
    """
    Test the correct set of the environment variables YOLO_OBJECT_DETECTION

    Args:
        test_object_detector: ObjectDetector instance

    Returns:
    """

    assert os.getcwd() == os.environ['YOLO_OBJECT_DETECTION_PATH']


@pytest.mark.parametrize('test_config_file, test_config, expected_value', [
    ('config.yaml', 'classes_file_path', './classes/yolov3_classes.txt'),
    ('config.yaml', 'model_structure_file_path', './models/yolov3.cfg'),
    ('config.yaml', 'model_weights_file_path', './models/yolov3.weights'),
    ('config.yaml', 'test_data_path', './data/test_images/')
])
def test_read_configuration(test_config_file: str,
                            test_config: str,
                            expected_value: str):
    """
    Test the function packages.utils.utils.read_configuration

    Args:
        test_config_file: String configuration file name
        test_config: String configuration entry key
        expected_value: String configuration expected value

    Returns:
    """

    # Read configuration file
    config = read_configuration(test_config_file)

    assert config[test_config] == expected_value


@pytest.mark.parametrize('test_config_file, expected_error', [
    ('wrong_config.config', FileNotFoundError)
])
def test_read_configuration_exception(test_config_file: str,
                                      expected_error: FileNotFoundError):
    """
    Test the exceptions to the function packages.utils.utils.read_configuration

    Args:
        test_config_file: String configuration file name
        expected_error: Exception instance

    Returns:
    """

    with pytest.raises(expected_error):

        read_configuration(test_config_file)