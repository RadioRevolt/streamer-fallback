# coding=UTF-8
from streamer_fallback.core.recording import Recording
from streamer_fallback.core.show_element import ShowElement
from streamer_fallback.core.settings import Settings

class AudioCatalogLayer(object):

    """
     Layer that provides access to the metadata stored in the central audio database.
     
     It abstracts the process of quering for recordings that have a given name, as
     well as fetching their title, duration, size and samba file path (in a format
     accepted by FileLayer).

    :version:
    :author:
    """

    def search_one(self, show_element):
        """
         Search for the newest audio recording with a title that satisfies the given
         query.

        @param core.ShowElement show_element : Search for recordings that match this ShowElement.
        @return core.Recording :
        @author
        """
        pass

    def search_all(self, show_element):
        """
         Returns all the recordings with a title that matches the given query.
         
         They are sorted by ascending date.

        @param core.ShowElement show_element : Search for all recordings that match this ShowElement.
        @return list :
        @author
        """
        pass

    def __init__(self, settings):
        """
         Initialize the AudioCatalogLayer.

        @param core.Settings settings : The settings. Can be used to specify options in the same option file as everything else.
        @return  :
        @author
        """
        pass



