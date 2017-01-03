# coding=UTF-8
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
     Main program for the core. Mainly handles figuring out what to do, given the
     arguments, and actually performing those actions.

    :version:
    :author:
    """

    """ ATTRIBUTES

     Settings for streamer-fallback

    settings  (public)

     Instance of Scheduler, which grants you access to downloaded and not-downloaded
     schedules and analyzing them.

    scheduler  (public)

     Instance representing the LiquidSoap service. Can be used primarily for
     restarting LiquidSoap and installing new configuration file.

    liquidsoap  (public)

     Instance of LiquidSoapConfiguration, which represents one configuration file for
     LiquidSoap.

    liquidsoap_config  (public)

     Instance of RerunDownloader that lets you download reruns.

    rerun_downloader  (public)

     Instance of RerunSelector, that lets you figure out which rerun to use for a
     given show in the schedule.

    rerun_selector  (public)

     Layer providing access to the catalog of audio elements available at the central
     audio database.
     
     Focused on the metadata, not the audio itself. Metadata includes title, duration
     and file path.

    audio_catalog  (public)

     Layer providing a function for downloading a file from the central audio
     database locally.

    file_layer  (public)

     Layer providing a way to download and parse schedule files.

    schedule_layer  (public)

    """

    def main(self, args):
        """
         Main program.

        @param list args : Program arguments.
        @return int :
        @author
        """
        pass

    def __init__(self):
        """
         Initializes attributes so they exist, but does not create objects of them (they
         are just assigned None).

        @return  :
        @author
        """
        pass

    def do_schedule(self, needed_days):
        """
         Does the work necessary with respect to the schedule, such as ensuring we have
         the schedule for the days we need it for, and no unecessary schedules laying
         about. It must also handle situations in which the schedule cannot be downloaded
         because systems are down.

        @param list needed_days : List of datetime.date, which are the days we need the schedule for.
        @return  :
        @author
        """
        pass

    def _ls_needs_restart(self):
        """
         True if LiquidSoap needs to be restarted because of changes to its script, false
         if not.

        @return bool :
        @author
        """
        pass



