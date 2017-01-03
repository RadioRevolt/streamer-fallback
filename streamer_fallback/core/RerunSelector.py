# coding=UTF-8
from core.Recording import *
from core.ShowElement import *
from core.Show import *
from core.AudioCatalogLayer import *

class RerunSelector(object):

    """
     Mirrors the AutoReplace task in BUS. Given a schedule and the database of
     reruns, it assigns a rerun for each show in the schedule.
     
     It assumes that in order to find a rerun for a program, you need to search for
     "Program name*", that is, all recordings start with their program name.

    :version:
    :author:
    """

    """ ATTRIBUTES

     Instance of AudioCatalogLayer, used to query the database for recordings.

    audio_catalog  (protected)

     True if there are live shows present in the schedule, false if not.

    liveshows_present  (private)

     Show name used to identify shows which are to be nightmusic.

    nightmusic_show_name  (private)

    """

    def find_recording(self, show_element):
        """
         Returns a Recording that matches the given ShowElement, or None if nothing
         matches.

        @param core.ShowElement show_element : The ShowElement to find the recording for.
        @return core.Recording :
        @author
        """
        pass

    def convert_show_to_recordings(self, show):
        """
         Given a Show, finds a list of recordings to use for that show.
         
         If a show is empty, recordings may still be picked by taking into account the
         show's name.

        @param core.Show show : The Show to find recordings/reruns for.
        @return list :
        @author
        """
        pass

    def pick_reruns_for_schedule(self, day_schedule):
        """
         Given the schedule for one day, a list of tuples is returned.
         
         Each tuple has a start time, end time and recording.
         
         Functions as a converter between the Scheduler's output and the
         RerunDownloader's input.

        @param dict day_schedule : Dict with starting time as datetime.datetime as key, and an instance of Show as value.
        @return list :
        @author
        """
        pass

    def __init__(self, audio_catalog, liveshows_present, nightmusic_show_name):
        """
         Initialize this RerunSelector.

        @param core.AudioCatalogLayer audio_catalog : Instance of AudioCatalogLayer, which can be used to query for recordings.
        @param bool liveshows_present : True if there are live shows present in the schedule, false if not. Used to determine whether to put a recording in a show with no ShowElements and no signs on being a rerun.
        @param string nightmusic_show_name : Corresponds to the attribute with the same name.
        @return  :
        @author
        """
        pass



