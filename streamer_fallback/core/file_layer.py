# coding=UTF-8
from streamer_fallback.core.settings import Settings

class FileLayer(object):

    """
     Layer providing a method for downloading an audio file from the central audio
     database onto the local storage.

    :version:
    :author:
    """

    def download(self, external_path, internal_path):
        """
         Download the specified audio file from the central audio database and store it
         at the specified path.

        @param string external_path : Path specifying where the original audio file is stored.
        @param string internal_path : Absolute, local path specifying where to save the audio file.
        @return  :
        @author
        """
        pass

    def __init__(self, settings):
        """
         Initialize new instance of this class.

        @param core.Settings settings : The Settings object. Used to fetch options specific for the FileLayer implementation.
        @return  :
        @author
        """
        pass



