# coding=UTF-8
import datetime
from streamer_fallback.core.recording_type import RecordingType

class Recording(object):

    """
    Data class representing one recording of an earlier show (or
    potentially a recording of something else).

    Attributes:
        title: This recording's title.
        filepath: Absolute path to where the file is stored.
        filename: The recording's file name.
        duration: Duration of the recording.
        size: The size of the audio recording, measured in bytes.
        type: The type of this recording.
    """

    def __init__(
        self,
        title: str,
        filepath: str,
        duration: datetime.timedelta,
        size: int,
        type_: RecordingType
    ) -> None:
        """
        Initialize a new Recording. You can basically set any attribute you
        want through the parameters, but they are all optional.

        title: This recording's title.
        filepath: The absolute path to this recording, in a way that is accepted by the current FileDownloader.
        duration: This recording's duration.
        size: This recording's file size (in bytes).
        type: The type of recording this is.
        """
        pass



