# coding=UTF-8
import datetime
from typing import Sequence
from streamer_fallback.core.show_element import ShowElement

class Show(object):

    """
    Data class representing one broadcast of a program.

    Attributes:

        start: When this show starts
        end: When this show ends.
        duration: The duration of the show.
        title: This show's title. Usually equals the program's name.
        is_rerun: True if this is a rerun of an earlier show, false if not
            (assuming live shows exist).
            The heuristic of deciding whether a show is a broadcast or not,
            considers whether the title ends with "(R)" or the existence of
            elements in the rerunner.
        elements: Elements that are to be played by the rerunner as a part of
            this show. Usually, this will be one recording of an earlier
            show. The list consists of Elements.
    """

    def __init__(
            self,
            start: datetime.datetime =None,
            end: datetime.datetime =None,
            duration: datetime.timedelta =None,
            title: str =None,
            is_rerun: bool =None,
            elements: Sequence[ShowElement] =None
    ) -> None:
        """
        Initialize the Show, setting the provided attributes. All parameters are
        optional, and correspond to the attribute with the same name.

        Arguments:
            start: Start of this broadcast.
            end: End of this broadcast. This parameter and the duration
                parameter are mutually exclusive; specifying both will raise
                an exception.
            duration: Duration of the broadcast. This parameter and the end
                parameter are mutually exclusive; specifying both will raise
                an exception.
            title: Title of this show.
            is_rerun: True if this show is a rerun of an earlier broadcast,
                false if not.
            elements: The ShowElements that this show consists of.
        """
        pass



