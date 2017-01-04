# coding=UTF-8
from streamer_fallback.core.settings import Settings

class FileLayer(object):
    """
    Layer providing a method for downloading an audio file from the central
    audio database onto the local storage.
    """

    def download(self, external_path: str, internal_path: str) -> None:
        """
        Download the specified audio file from the central audio database and
        store it at the specified path.

        Arguments:
            external_path: Path specifying where the original audio file is stored.
            internal_path: Absolute, local path specifying where to save the audio file.
        """
        pass

    def __init__(self, settings: Settings) -> None:
        """
        Initialize new instance of this class.

        Arguments:
            settings: The Settings object. Used to fetch options specific for the FileLayer implementation.
        """
        pass



