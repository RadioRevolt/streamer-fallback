# coding=UTF-8
from typing import TextIO
from streamer_fallback.core.situation import Situation
from streamer_fallback.core.status import Status

class Settings(object):
    """
    Settings for streamer-fallback

    Attributes:
        external_path_prefix: Prefix that is to be removed from the paths in
            order to get a local path.
        schedule_layer_directory: Directory dedicated to keeping schedule
            files offline.
        format_bitrate: The bitrate to use on the stream.
        format_samplerate: Samplerate to use.
        format_stereo: True if the stream is to be in stereo, false if not.
        icecast_host: Icecast host to connect to. Will usually be "localhost".
        icecast_mount: Mount to connect to on IceCast.
        icecast_password: Password to use when connecting to IceCast as a
            source.
        icecast_port: Port used by IceCast2.
        nightmusic_folder: Absolute path to the folder in which the nightmusic
            tracks are stored.
        nightmusic_jingle: Absolute path to the jingle that plays between each
            track when playing nightmusic.
        situation: Whether to acknowledge the outage as planned, unplanned or
            not at all.
        status: What to play for the listener.
        technical_problems_amplification: How much to amplify the technical
            problems jingle. Each sample will be multiplied by this value.
            Experimentation or analyzing the audio file is the best way to
            determine this.
        technical_problems_jingle: Absolute filepath to the jingel to play
            when there are technical problems.
        liquidsoap_script: Absolute path to where the LiquidSoap script is
            stored. By placing this path inside /etc/liquidsoap and using the
            liq file extension, the file will be used by the LiquidSoap service.
        liveshows_present: True if there are live shows present in the
            schedule, false if not. This determines whether to play reruns or
            technical problems in shows that don't look like reruns.
        liquidsoap_command: Command to use when invoking LiquidSoap directly,
            for example to verify a LiquidSoap script.
        liquidsoap_service_name: Name of the service to restart (using SystemD)
            when asked to restart or find last restart of LiquidSoap.
        recording_directory: Path to the directory in which recordings are to
            be saved.
    """

    def __init__(self, fd: TextIO=None) -> None:
        """
        Initialize settings either from default values, or from an existing
        settings file.

        Arguments:
            fd: File to read configuration from. Optional.
        """
        pass

    def write(self, fd: TextIO) -> None:
        """
        Write the settings to the given file.

        Arguments:
            fd: File object to write the settings to.
        """
        pass



