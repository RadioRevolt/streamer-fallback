# coding=UTF-8
from streamer_fallback.core.recording_type import RecordingType

class ShowElement(object):

    """
     Immutable data class representing one audio element (= file) in a show in BCS.

    :version:
    :author:
    """

    """ ATTRIBUTES

     Name of the element.

    title  (public)

     The type of recording that is to be used when finding rerun for this element.

    type  (public)

    """

    def __init__(self, title, type):
        """
         Initialize a new ShowElement.

        @param string title : Name of this element.
        @param core.RecordingType type : The type of recording that is going to be used when finding a recording to replace this element with.
        @return  :
        @author
        """
        pass



