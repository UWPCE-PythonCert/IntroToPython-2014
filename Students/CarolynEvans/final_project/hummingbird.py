import urllib2
import json

from config import config

class hummingbird(object):
    """
    This class is used to call the DizzyNinja Hummingbird Domain Recommendation API.
    The complete hummingbird API documentation can be found at
        https://wiki.rightside.net/display/tnt/API+Documentation
    """

    def __init__(self):
        """
        This method sets the hummingbird url from the config.
        """
        cnf = config()
        self.url = cnf.get('hummingbird_url')


    def __call__(self, command, **kwargs):
        """
        This method calls the hummingbird API.
        The complete hummingbird API documentation can be found at
        https://wiki.rightside.net/display/tnt/API+Documentation
        :param command: A string containing a valid hummingbird command.
        :param kwargs: Depends on 'command'. See hummingbird documentation for complete list.
        :return: Returns JSON with results for the 'command'.
        """

        # build the query string parameter for the hummingbird API http request.
        query_string = "".join(['{}={},'.format(key,val) for key, val in kwargs.items()])

        #add the 'command' and the query string to the url.
        url = '{}{}?{}'.format(self.url, command, query_string)

        response = urllib2.urlopen(url).read()
        return json.loads(response)


