# coding=UTF-8
from typing import Sequence
import datetime
from streamer_fallback.core.settings import Settings
from streamer_fallback.core.scheduler import Scheduler
from streamer_fallback.core.liquid_soap import LiquidSoap
from streamer_fallback.core.liquid_soap_configuration import LiquidSoapConfiguration
from streamer_fallback.core.rerun_downloader import RerunDownloader
from streamer_fallback.core.rerun_selector import RerunSelector
from streamer_fallback.core.audio_catalog_layer import AudioCatalogLayer
from streamer_fallback.core.file_layer import FileLayer
from streamer_fallback.core.schedule_layer import ScheduleLayer

class core_main(object):
    """
    Main program for the core. Mainly handles figuring out what to do, given
    the arguments, and actually performing those actions.

    Attributes:
        settings: Settings for streamer-fallback
        scheduler: Instance of Scheduler, which grants you access to
            downloaded and not-downloaded schedules and analyzing
            them.
        liquidsoap: Instance representing the LiquidSoap service. Can be
            used primarily for restarting LiquidSoap and installing new
            configuration file.
        liquidsoap_config: Instance of LiquidSoapConfiguration, which
            represents one configuration file for LiquidSoap.
        rerun_downloader: Instance of RerunDownloader that lets you
            download reruns.
        rerun_selector: Instance of RerunSelector, that lets you figure out
            which rerun to use for a given show in the schedule.
        audio_catalog: Layer providing access to the catalog of audio elements
            available at the central audio database.
            Focused on the metadata, not the audio itself. Metadata includes
            title, duration and file path.
        file_layer: Layer providing a function for downloading a file from the
            central audio database locally.
        schedule_layer: Layer providing a way to download and parse schedule
            files.
    """

    def main(self, args: Sequence[str]) -> None:
        """
        Main program.

        Arguments:
            args: Program arguments.
        """
        pass

    def __init__(self) -> None:
        """
        Initializes attributes so they exist, but does not create objects of
        them (they are just assigned None).
        """
        pass

    def do_schedule(self, needed_days: Sequence[datetime.date]) -> None:
        """
        Does the work necessary with respect to the schedule, such as ensuring
        we have the schedule for the days we need it for, and no unecessary
        schedules laying about. It must also handle situations in which the
        schedule cannot be downloaded because systems are down.

        Arguments:
            needed_days: List of datetime.date, which are the days we need the schedule for.
        """
        pass

    def _ls_needs_restart(self) -> bool:
        """
        True if LiquidSoap needs to be restarted because of changes to its
        script, false if not.
        """
        pass

