# coding=UTF-8
from core.Show import *
from core.Settings import *

class ScheduleLayer(object):

    """
     Layer providing methods for downloading schedule files, and parsing them.

    :version:
    :author:
    """

    def download(self, day):
        """
         Make the schedule for the given day available locally.

        @param datetime.date day : Day of the schedule to make available offline.
        @return  :
        @author
        """
        pass

    def available_locally(self):
        """
         List of dates which have their schedule available offline.

        @return list :
        @author
        """
        pass

    def remove(self, day):
        """
         Remove the local files that were downloaded to make the schedule for the given
         day available locally.

        @param datetime.date day : Day to remove from the local storage.
        @return  :
        @author
        """
        pass

    def parse(self, day):
        """
         Transform the contents of the local file(s) associated with the given day into a
         dict with starttime (datetime.time) as key and an instance of Show as value.
         
         This function will also have to take care of assigning a RecordType to each
         ShowElement in each Show.

        @param datetime.date day : The day to parse the schedule for.
        @return dict :
        @author
        """
        pass

    def __init__(self, schedule_layer_directory, settings):
        """
         Initialize the ScheduleLayer.

        @param string schedule_layer_directory : Absolute path to a folder stored locally, which this ScheduleLayer can use to its heart's content.
        @param core.Settings settings : Instance of Settings, used to get settings necessary for fetching and parsing the schedule.
        @return  :
        @author
        """
        pass



