# coding=UTF-8
from streamer_fallback.core.show_element import ShowElement

class Show(object):

    """
     Data class representing one broadcast of a program.

    :version:
    :author:
    """

    """ ATTRIBUTES

     When this show starts

    start  (public)

     When this show ends.

    end  (public)

     The duration of the show.

    duration  (public)

     This show's title. Usually equals the program's name.

    title  (public)

     True if this is a rerun of an earlier show, false if not (assuming live shows
     exist).
     
     The heuristic of deciding whether a show is a broadcast or not, considers
     whether the title ends with "(R)" or the existence of elements in the rerunner.

    is_rerun  (public)

     Elements that are to be played by the rerunner as a part of this show. Usually,
     this will be one recording of an earlier show.
     
     The list consists of Elements.

    elements  (public)

    """

    def __init__(self, start, end, duration, title, is_rerun, elements):
        """
         Initialize the Show, setting the provided attributes. All parameters are
         optional, and correspond to the attribute with the same name.

        @param datetime.datetime start : Start of this broadcast.
        @param datetime.datetime end : End of this broadcast. This parameter and the duration parameter are mutually exclusive; specifying both will raise an exception.
        @param datetime.timedelta duration : Duration of the broadcast. This parameter and the end parameter are mutually exclusive; specifying both will raise an exception.
        @param string title : Title of this show.
        @param bool is_rerun : True if this show is a rerun of an earlier broadcast, false if not.
        @param list elements : The ShowElements that this show consists of.
        @return  :
        @author
        """
        pass



