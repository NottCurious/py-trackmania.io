# pylint: disable=too-many-instance-attributes
from typing import List
from functools import lru_cache

__all__ = ("TMIO", "TMX")

# pylint: disable=too-few-public-methods
class TMIOTabs:
    """TMIO Endpoints"""

    def __init__(self):
        self.PLAYER: str = "player"
        self.PLAYERS: str = "players"
        self.TROPHIES: str = "trophies"
        self.MAP: str = "map"
        self.LEADERBOARD: str = "leaderboard"

        self.TOP_MATCHMAKING: str = "top/matchmaking"
        self.TOP_TROPHIES: str = "top/trophies"

        self.MATCHMAKING_ID: int = 2
        self.ROYAL_ID: int = 3

        self.TOTD: str = "totd"
        self.COTD: str = "cotd"
        self.ADS: str = "ads"


# pylint: disable=too-few-public-methods
class TMIO:
    """
    Basic TMIO Api Details

    Parameters
    ----------
    PROTOCOL : str
        The PROTOCOL to use for the api. Equal to "https"
    BASE : str
        The BASE url for the api. Equal to "trackmania.io"
    api : str
        The api endpoint for `trackmania.io`. Equal to "api".
    TABS : :class:`TMIOTabs`
        The TABS for the api.
    """

    PROTOCOL: str = "https"
    BASE: str = "trackmania.io"
    API: str = "api"

    TABS: TMIOTabs = TMIOTabs()

    @staticmethod
    @lru_cache
    def build(endpoints: List[str]) -> str:
        """Builds a TMIO endpoint url.

        Parameters
        ----------
        endpoints : List[str]
            The endpoints to build the url with.

        Returns
        -------
        str
            The built endpoint url.

        """
        url = f"{TMIO.PROTOCOL}://{TMIO.BASE}/{TMIO.API}/"

        if len(endpoints) == 0:
            return url
        if len(endpoints) > 1:
            for item in endpoints:
                url = url + item + "/"

            # Removing the Final /
            return url[:-1]
        return url + endpoints[0]


# pylint: disable=too-few-public-methods
class TMX:
    """
    Basic TMX Api Details

    Parameters
    ----------
    PROTOCOL : str
        The PROTOCOL to use for the api. Equal to "https"
    BASE : str
        The BASE url for the api. Equal to "trackmania.exchange"
    api : str
        The api endpoint for `trackmania.exchange`. Equal to "api".

    """

    PROTOCOL: str = "https"
    BASE: str = "trackmania.exchange"
    API: str = "api"

    @staticmethod
    @lru_cache
    def build(endpoints: List[str]) -> str:
        """URL Builder for TMX API

        Parameters
        ----------
        endpoints : class:`List`[str]
            The endpoints as a list.

        Returns
        -------
        str
            The URL.
        """
        url = f"{TMX.PROTOCOL}://{TMX.BASE}/{TMX.API}/"

        if len(endpoints) == 0:
            return url
        if len(endpoints) > 1:
            for item in endpoints:
                url = url + item + "/"

            # Removing the Final /
            return url[:-1]
        return url + endpoints[0]
