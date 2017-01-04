# coding=UTF-8
from typing import List, Union, Tuple, Dict
import datetime
from streamer_fallback.core.recording import Recording
from streamer_fallback.core.show_element import ShowElement
from streamer_fallback.core.show import Show
from streamer_fallback.core.audio_catalog_layer import AudioCatalogLayer

class RerunSelector(object):
    """
    Class for finding files to play in place of a ShowElement.

    Mirrors the AutoReplace task in BUS. Given a schedule and the database
    of reruns, it assigns a rerun for each show in the
    schedule.

    It assumes that in order to find a rerun for a program, you need to search
    for "Program name*", that is, all recordings start with their program name.

    Attributes:
        _audio_catalog: Instance of AudioCatalogLayer, used to query the
            database for recordings.
        _liveshows_present: True if there are live shows present in the
            schedule, false if not.
        _nightmusic_show_name: Show name used to identify shows which are to
            be nightmusic.
    """

    def find_recording(self, show_element: ShowElement) -> Union[Recording,
                                                                 None]:
        """
        Find a specific file to use in place of the given ShowElement.

        Arguments:
            show_element: The ShowElement to find the recording for.

        Returns:
            A Recording to replace the ShowElement with, or None if no matching
            recording could be found.
        """
        pass

    def convert_show_to_recordings(self, show: Show) -> List[Recording]:
        """
        Given a Show, finds a list of recordings to use for that show.

        If a show is empty, recordings may still be picked by taking into
        account the show's name.

        Arguments:
            show: The Show to find recordings/reruns for.

        Returns:
            A list of Recording that are to played back-to-back when the given
            show airs.
        """
        pass

    def pick_reruns_for_schedule(self, day_schedule:
            Dict[datetime.datetime, Show]) -> List[Tuple[datetime.datetime,
            datetime.datetime, Recording]]:
        """
        Find time and file path for reruns to run given a day's schedule.

        Functions as a converter between the Scheduler's output and the
        RerunDownloader's input.

        Arguments:
            day_schedule: Dict with starting time as datetime.datetime as key,
                and an instance of Show as value.

        Returns:
            A list of tuples. Each tuple has a start time, end time and
            instance of Recording.
        """
        pass

    def __init__(self, audio_catalog: AudioCatalogLayer, liveshows_present:
                 bool, nightmusic_show_name: str) -> None:
        """
        Initialize this RerunSelector.

        Arguments:
            audio_catalog: Instance of AudioCatalogLayer, which can be used to
                query for recordings.
            liveshows_present: True if there are live shows present in the
                schedule, false if not. Used to determine whether to put a
                recording in a show with no ShowElements and no signs on being
                a rerun.
            nightmusic_show_name: Name used to identify shows in which
                nightmusic is to played.
        """
        pass



