# coding=UTF-8
from typing import List
from streamer_fallback.core.recording import Recording
from streamer_fallback.core.show_element import ShowElement
from streamer_fallback.core.settings import Settings

class AudioCatalogLayer(object):
    """
    Provides access to the metadata stored in the central audio database.

    It abstracts the process of quering for recordings that have a given
    name, as well as fetching their title, duration, size and samba file path
    (in a format accepted by FileLayer).
    """

    def search_one(self, show_element: ShowElement) -> Recording:
        """
        Search for the newest audio recording with a title that satisfies
        the given query.

        Arguments:
            show_element: Search for recordings that match this ShowElement.

        Returns:
            The newest Recording whose title satisfies the given query.
        """
        pass

    def search_all(self, show_element: ShowElement) -> List[Recording]:
        """
        Returns all the recordings with a title that matches the given
        query.

        They are sorted by ascending date.

        Arguments:
            show_element: Search for all recordings that match this ShowElement.
        """
        pass

    def __init__(self, settings: Settings):
        """
        Initialize the AudioCatalogLayer.

        Arguments:
            settings: The settings. Can be used to specify options in the same
                option file as everything else.
        """
        pass



