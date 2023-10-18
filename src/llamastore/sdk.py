"""
Creates a Llamastore class.
Generates the main SDK with all available queries as attributes.

Class:
    Llamastore
"""
from .net.environment import Environment
from .services.llama_picture import LlamaPicture
from .services.llama import Llama
from .services.token import Token
from .services.user import User


class Llamastore:
    """
    A class representing the full Llamastore SDK

    Attributes
    ----------
    llama_picture : LlamaPicture
    llama : Llama
    token : Token
    user : User

    Methods
    -------
    set_base_url(url: str)
        Sets the end URL
    set_access_token(access_token)
        Set the access token
    """

    def __init__(self, access_token="", environment=Environment.DEFAULT) -> None:
        """
        Initializes the Llamastore SDK class.
        Parameters
        ----------
        environment: str
            The environment that the SDK is accessing
        access_token : str
            The access token
        """
        self.llama_picture = LlamaPicture(access_token)
        self.llama = Llama(access_token)
        self.token = Token(access_token)
        self.user = User(access_token)

        self.set_base_url(environment.value)

    def set_base_url(self, url: str) -> None:
        """
        Sets the end URL

        Parameters
        ----------
            url:
                The end URL
        """
        self.llama_picture.set_base_url(url)
        self.llama.set_base_url(url)
        self.token.set_base_url(url)
        self.user.set_base_url(url)

    def set_access_token(self, token: str) -> None:
        """
        Sets auth token key

        Parameters
        ----------
        token: string
            Auth token value
        """
        self.llama_picture.set_access_token(token)
        self.llama.set_access_token(token)
        self.token.set_access_token(token)
        self.user.set_access_token(token)
