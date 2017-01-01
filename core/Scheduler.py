# coding=UTF-8
from core.Show import *
from core.ScheduleLayer import *

class Scheduler(object):

    """
     Provides access to downloaded as well as not-downloaded schedules and handles
     downloading and deletion of local schedules. This class offloads most of this
     work to the ScheduleLayer, but stores the parsed schedule in memory so it isn't
     parsed more than once. It also implements the logic for finding schedules that
     are no longer needed.

    :version:
    :author:
    """

    """ ATTRIBUTES

     Dictionary containing the schedule. Key is datetime.date, value is a dictionary
     with key being datetime.time and value being an instance of Show. Lazy loaded
     from local schedule files.

    schedules  (protected)

     Instance of ScheduleLayer, which provides access to the schedule.

    schedule_layer  (private)

    """

    def get(self, day):
        """
         Retrieve the schedule for the given day, if it has been downloaded locally.

        @param datetime.date day : Which day to retrieve the schedule for.
        @return dict :
        @author
        """
        pass

    def download(self, day):
        """
         Download the schedule for the given day.
         
         Any existing local copies are overwritten by the upstream schedule, letting you
         update local copies using this method.

        @param datetime.date day : The day to download the schedule for.
        @return  :
        @author
        """
        pass

    def remove_unnecessary(self):
        """
         Remove any local schedules that are no longer needed.
         
         In practice, this means local copies of schedules for days in the past.

        @return  :
        @author
        """
        pass

    def __init__(self, schedule_layer):
        """
         Create new Scheduler object, and initialize attributes.

        @param core.ScheduleLayer schedule_layer : Instance of ScheduleLayer, which is used to query for schedules.
        @return  :
        @author
        """
        pass

    def _remove(self, day):
        """
         Remove the local copy of the schedule for the given day.

        @param datetime.date day : The day to remove the local copy of the schedule for.
        @return  :
        @author
        """
        pass



