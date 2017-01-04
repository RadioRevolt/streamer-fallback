# coding=UTF-8
from streamer_fallback.core.file_layer import FileLayer

class SambaFileLayer (FileLayer):
    """
    Implementation of FileLayer for systems in which the filepath is a Samba
    path.
    """

