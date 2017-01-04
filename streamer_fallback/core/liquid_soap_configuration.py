# coding=UTF-8
from typing import TextIO
from streamer_fallback.core.status import Status
from streamer_fallback.core.situation import Situation

class LiquidSoapConfiguration(object):
    """
    Representation of a LiquidSoapConfiguration (that is, a LiquidSoap script),
    which also handles saving that configuration to a file.

    Attributes:
        status: What to play for the listener.
        situation: Whether to acknowledge the outage as planned, unplanned or
            not at all.
        schedule: List of what to play at different times. Used only when the
            status is rerun.  Each item is a tuple of three items. The first
            is when to start playing that recording. The second is when to
            stop playing that recording. The third is either an absolute path
            to the file to play, or the string "nightmusic" if nightmusic is
            to be played in that spot.

            Times where there are nothing playing, will play silence. After 12
            seconds of silence, technical problems jingle will play.
        technical_problems_jingle: Absolute filepath to the jingel to play
            when there are technical problems.
        nightmusic_jingle: Absolute path to the jingle that plays between each
            track when playing nightmusic.
        icecast_mount: Mount to connect to on IceCast.
        icecast_host: Icecast host to connect to. Will usually be "localhost".
        icecast_password: Password to use when connecting to IceCast as a
            source.
        icecast_port: Port used by IceCast2.
        format_stereo: True if the stream is to be in stereo, false if not.
        format_samplerate: Samplerate to use.
        format_bitrate: The bitrate to use on the stream.
        nightmusic_folder: Absolute path to the folder in which the nightmusic
            tracks are stored.
        technical_problems_amplification: How much to amplify the technical
            problems jingle. Each sample will be multiplied by this value.
            Experimentation or analyzing the audio file is the best way to
            determine this.
    """

    def write(self, fd: TextIO) -> None:
        """
        Export the resulting LiquidSoap script.

        Arguments:
            fd: The file object to write the script to.
        """
        pass

    def __init__(self) -> None:
        """
        Set this instance's attributes.

        The arguments are not described here, but they
        can be provided as keyword arguments that set the attribute with the
        corresponding name. All those arguments are optional.
        """
        pass



