# coding=UTF-8
import datetime
from typing import List, Dict
from streamer_fallback.core.show import Show
from streamer_fallback.core.settings import Settings

class ScheduleLayer(object):
    """
    Layer providing methods for downloading schedule files, and parsing them.
    """

    def download(self, day: datetime.date) -> None:
        """
        Make the schedule for the given day available locally.

        Arguments:
            day: Day of the schedule to make available offline.
        """
        pass

    def available_locally(self) -> List[datetime.date]:
        """
        Generate list of dates which have their schedule available offline.

        Returns:
            List of days for which there is a schedule available offline.
        """
        pass

    def remove(self, day: datetime.date) -> None:
        """
        Remove all downloaded schedule files for the given date's schedule.

        Arguments:
            day: Day to remove from the local storage.
        """
        pass

    def parse(self, day: datetime.date) -> Dict[datetime.time, Show]:
        """
        Parse the downloaded files to get the given day's schedule.

        Transform the contents of the local file(s) associated with the given
        day into a dict with starttime (datetime.time) as key and an instance
        of Show as value.

        This function will also have to take care of assigning a RecordType to
        each ShowElement in each Show.

        Arguments:
            day: The day to parse the schedule for.

        Returns:
            Dictionary with a show's start time as key and the Show instance as
            value.
        """
        pass

    def __init__(self, schedule_layer_directory: str, settings: Settings) -> None:
        """
        Initialize the ScheduleLayer.

        Arguments:
            schedule_layer_directory: Absolute path to a folder stored locally,
                which this ScheduleLayer can use to its heart's content.
            settings: Instance of Settings, used to get settings necessary for
                fetching and parsing the schedule.
        """
        pass



