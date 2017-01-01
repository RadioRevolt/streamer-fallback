# coding=UTF-8
from core.FileLayer import *

class RerunDownloader(object):

    """
     Class that ensures that the necessary reruns are available locally, and
     downloads the reruns that are needed but not present, and deletes the reruns
     that are not needed but present locally.

    :version:
    :author:
    """

    """ ATTRIBUTES

     List of Samba paths for the files that are available locally.
     Loaded lazily.

    local_files  (public)

     Instance of FileLayer, used to download recordings.

    file_layer  (private)

     Path to the directory in which recordings are to be saved.

    recording_directory  (private)

     Prefix that is to be removed from the paths in order to get a local path.

    external_path_prefix  (private)

    """

    def synchronize(self, files):
        """
         Ensures that all media files in the given list, but none other, are available
         locally.
         
         This may potentially download large files, and will therefore take its time. You
         can query for the progress simultanously using the progress method.
         
         If there is not enough disk space for all the necessary files, an appropriate
         exception is raised.

        @param list files : List of strings, which are the paths to the different media files that are needed locally.
        @return  :
        @author
        """
        pass

    def files_to_download(self, needed_files):
        """
         Given a list of necessary files, a list of files that are necessary but not
         available locally is generated.

        @param list needed_files : The complete list of files that are needed.
        @return list :
        @author
        """
        pass

    def files_to_remove(self, needed_files):
        """
         Given a complete list of files that are needed, a list of files that are
         available locally but not needed is generated.

        @param list needed_files : Complete list of files that are needed.
        @return list :
        @author
        """
        pass

    def size_needed(self, needed_files):
        """
         Extra space required to ensure that the files in the given list are available
         locally.
         
         This can be negative, in the event that the files removed are greater in size
         than those needing to be downloaded.
         
         This doesn't actually download anything, it just gathers size data.

        @param list needed_files : List of files that must be available locally.
        @return list :
        @author
        """
        pass

    def __init__(self, file_layer, recording_directory, external_path_prefix):
        """
         Initiliaze the RerunDownloader.

        @param core.FileLayer file_layer : Instance of FileLayer, used for downloading files.
        @param string recording_directory : The directory in which recordings are stored.
        @param string external_path_prefix : Prefix for the external path, which can be stripped away and be prefixed by recording_directory to obtain a recording's local path.
        @return  :
        @author
        """
        pass

    def _available_locally(self, media_file):
        """
         Returns true if the given media file is available locally, false if not.

        @param string media_file : Samba path to the media file to query.
        @return bool :
        @author
        """
        pass



