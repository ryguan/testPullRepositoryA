"""
This is a test Repository in order to create fake documentation
"""

import os
import yaml

class BannedYamlReader:
    """
    A class for reading and processing a YAML file containing a list of banned strings.

    Args:
        folder (str): The folder containing the YAML file.

    Attributes:
        banned_list (list): A list of banned strings read from the YAML file.
    """

    def __init__(self, folder: str) -> None:
        """
        Initialize the BannedYamlReader with the specified folder path.

        Args:
            folder (str): The folder path to search for the YAML file.
        """
        banned_yaml_location = folder + "/yaml"
        self.banned_list = []
        if os.path.exists(banned_yaml_location):
            with open(banned_yaml_location, "r") as banned:
                try:
                    self.banned_list = yaml.safe_load(banned)
                except yaml.YAMLError as exc:
                    pass

    def get_banned_list(self) -> list:
        """
        Return the list of banned strings.

        Returns:
            list: A list of banned strings.
        """
        return self.banned_list
def example_function(param1, param2):
    """Example function that demonstrates Google style documentation.

    Args:
        param1 (str): The first parameter, a string.
        param2 (int): The second parameter, an integer.

    Returns:
        tuple: A tuple containing the sum of the two input parameters and their product.

    Raises:
        ValueError: If the input parameters are not of the expected types.

    Examples:
        >>> example_function("Hello", 42)
        ('Hello42', 1764)
        >>> example_function(42, "Hello")
        ('42Hello', 1764)

    [sphinxcontrib-napoleon.readthedocs.io](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
    """
    if not isinstance(param1, str) or not isinstance(param2, int):
        raise ValueError("Both param1 and param2 must be strings and integers, respectively.")
    
    result = (param1 + param2, param1 * param2)
    return result
