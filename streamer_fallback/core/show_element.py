# coding=UTF-8
from streamer_fallback.core.recording_type import RecordingType

class ShowElement(object):

    """
    Immutable data class representing one audio element (= file) in a show in BCS.

    Attributes:
        title: Name of the element.
        type: The type of recording that is to be used when finding rerun for this element.
    """

    def __init__(self, title: str, type_: RecordingType) -> None:
        """
        Initialize a new ShowElement.

        Arguments:
            title: Name of this element.
            type: The type of recording that is going to be used when finding a recording to replace this element with.
        """
        pass



