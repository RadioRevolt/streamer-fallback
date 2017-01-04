# coding=UTF-8
import datetime
from typing import Dict
from streamer_fallback.core.show import Show
from streamer_fallback.core.schedule_layer import ScheduleLayer

class Scheduler(object):
    """
    Provides access to the schedule.

    Both downloaded as well as not-downloaded schedules can be accessed.
    Downloading and deletion of local schedules is also handled by this class.

    This class offloads most of this work to the ScheduleLayer, but stores the
    parsed schedule in memory so it isn't parsed more than once. It also
    implements the logic for finding schedules that are no longer needed.

    Attributes:
        _schedules: Dictionary containing the schedule. Key is datetime.date,
            value is a dictionary with key being datetime.time and value being
            an instance of Show. Lazy loaded from local schedule files.
        _schedule_layer: Instance of ScheduleLayer, which provides access to
            the schedule.
    """

    def get(self, day: datetime.date) -> Dict[datetime.time, Show]:
        """
        Retrieve the schedule for the given day, if it has been downloaded
        locally.

        Arguments:
            day: Which day to retrieve the schedule for.

        Returns:
            Dictionary with the start time as key and the Show instance as
            value, representing the given day's schedule.
        """
        pass

    def download(self, day: datetime.date) -> None:
        """
        Download the schedule for the given day.

        Any existing local copies are overwritten by the upstream schedule,
        letting you update local copies using this method.

        Arguments:
            day: The day to download the schedule for.
        """
        pass

    def remove_unnecessary(self) -> None:
        """
        Remove any local schedules that are no longer needed.

        In practice, this means local copies of schedules for days in the past.
        """
        pass

    def __init__(self, schedule_layer: ScheduleLayer) -> None:
        """
        Create new Scheduler object, and initialize attributes.

        Arguments:
            schedule_layer: Instance of ScheduleLayer, which is used to query
                for schedules.
        """
        pass

    def _remove(self, day: datetime.date) -> None:
        """
        Remove the local copy of the schedule for the given day.

        Arguments:
            day: The day to remove the local copy of the schedule for.
        """
        pass



