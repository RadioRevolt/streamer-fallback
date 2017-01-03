# coding=UTF-8
from streamer_fallback.core.recording_type import RecordingType

class Recording(object):

    """
     Data class representing one recording of an earlier show (or potentially a
     recording of something else).

    :version:
    :author:
    """

    """ ATTRIBUTES

     This recording's title.

    title  (public)

     Absolute path to where the file is stored.

    filepath  (public)

     The recording's file name.

    filename  (public)

     Duration of the recording.

    duration  (public)

     The size of the audio recording, measured in bytes.

    size  (public)

     The type of this recording.

    type  (public)

    """

    def __init__(self, title, filepath, duration, size, type):
        """
         Initialize a new Recording. You can basically set any attribute you want through
         the parameters, but they are all optional.

        @param string title : This recording's title.
        @param string filepath : The absolute path to this recording, in a way that is accepted by the current FileDownloader.
        @param datetime.timedelta duration : This recording's duration.
        @param int size : This recording's file size (in bytes).
        @param core.RecordingType type : The type of recording this is.
        @return  :
        @author
        """
        pass



