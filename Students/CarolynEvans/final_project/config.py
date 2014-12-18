import yaml

class config():
    """
    This class parses config.yaml into a dictionary and provides callability.
    """
    _VALUES = dict()

    def __init__(self):
        with open('config.yaml', 'r') as f:
            config = yaml.load(f)

        self.flatten(config)


    def flatten(self, config):
        """
        This method loads a dictionary using the data that was loaded from config.yaml in __init__.
        The yaml dictionary 'values' may potentially be another dictionary.
        This method is used recursively to explode all levels of the yaml into a flat dictionary.
        :param config: A dict containing configuration values.
        :return: There is no return value. This method is called during __init__.
        """
        # TODO: Rewrite for loop as comprehension

        for key, val in config.items():
            if type(val) is dict:
                self.flatten(val)
            else:
                self._VALUES[key]=val



    def get(self, key):
        """
        This method is provides a configuration value for the given 'key'.
        :param key: A string containing the 'key' of the config item in the config dict.
        :return: A string containing the value of the config item in the config dict.
        """
        val = self._VALUES[key]
        return val

