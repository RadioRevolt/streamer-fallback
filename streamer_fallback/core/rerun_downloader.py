# coding=UTF-8
from typing import Sequence, Set
from streamer_fallback.core.file_layer import FileLayer

class RerunDownloader(object):
    """
    Ensures only needed reruns are present locally.

    Attributes:
        local_files: List of external paths for the files that are available
            locally. Loaded lazily.
        file_layer: Instance of FileLayer, used to download recordings.
        recording_directory: Path to the directory in which recordings are to
            be saved.
        external_path_prefix: Prefix that is to be removed from the paths in
            order to get a local path.
    """

    def synchronize(self, files: Set[str]) -> None:
        """
        Download and remove reruns so that only those in files are present.

        This may potentially download large files, and will therefore take its
        time. You can query for the progress simultanously using the progress
        method.

        If there is not enough disk space for all the necessary files, an
        appropriate exception is raised.

        Arguments:
            files: Set of strings, which are the paths to the different media
                files that are needed locally.
        """
        pass

    def files_to_download(self, needed_files: Set[str]) -> Set[str]:
        """
        Given a set of necessary files, a set of files that are necessary
        but not available locally is generated.

        Arguments:
            needed_files: The complete set of files that are needed.

        Returns:
            Set of external file paths for files that are necessary but not
            available offline.
        """
        pass

    def files_to_remove(self, needed_files: Set[str]) -> Set[str]:
        """
        Given a complete set of files that are needed, a set of files that
        are available locally but not needed is generated.

        Arguments:
            needed_files: Complete set of external file paths for files that
                are needed.

        Returns:
            Set of local file paths for files that are not needed offline.
        """
        pass

    def size_needed(self, needed_files: Set[str]) -> int:
        """
        Extra space required to ensure that the files in the given set are
        available locally.

        This can be negative, in the event that the files removed are greater
        in size than those needing to be downloaded.

        This doesn't actually download anything, it just gathers size data.

        Arguments:
            needed_files: List of files that must be available locally.

        Returns:
            Number of additional bytes that must be used to store all
            needed files offline.
        """
        pass

    def __init__(self, file_layer: FileLayer, recording_directory: str,
                 external_path_prefix: str) -> None:
        """
        Initiliaze the RerunDownloader.

        Arguments:
            file_layer: Instance of FileLayer, used for downloading files.
            recording_directory: The directory in which recordings are
                stored.
            external_path_prefix: Prefix for the external path, which can be
                stripped away and be prefixed by recording_directory to obtain
                a recording's local path.
        """
        pass

    def _available_locally(self, media_file: str) -> bool:
        """
        Returns true if the given media file is available locally, false if not.

        Arguments:
            media_file: External path of the media file to query.

        Returns:
            True if the given file is available locally, False if not.
        """
        pass

    def _ext_to_local(self, external_file_path: str) -> str:
        """
        Convert an external file path into an absolute local one.

        Arguments:
            external_file_path: Path to the file, as accepted by the current
                FileLayer.

        Returns:
            The absolute local file path.
        """
        pass

    def _local_to_ext(self, local_file_path: str) -> str:
        """
        Convert an absolute local file path into an external one.

        Arguments:
            local_file_path: The absolute local path to the file, as accepted
                by LiquidSoap, the OS and so on.

        Returns:
            The external file path, as accepted by FileLayer.
        """
        pass

