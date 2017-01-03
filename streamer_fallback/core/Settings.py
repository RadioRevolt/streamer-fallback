# coding=UTF-8
from overview.situation import *
from overview.statuses import *

class Settings(object):

    """
     Settings for streamer-fallback

    :version:
    :author:
    """

    """ ATTRIBUTES

     Prefix that is to be removed from the paths in order to get a local path.

    external_path_prefix  (public)

     Directory dedicated to keeping schedule files offline.

    schedule_layer_directory  (public)

     The bitrate to use on the stream.

    format_bitrate  (public)

     Samplerate to use.

    format_samplerate  (public)

     True if the stream is to be in stereo, false if not.

    format_stereo  (public)

     Icecast host to connect to. Will usually be "localhost".

    icecast_host  (public)

     Mount to connect to on IceCast.

    icecast_mount  (public)

     Password to use when connecting to IceCast as a source.

    icecast_password  (public)

     Port used by IceCast2.

    icecast_port  (public)

     Absolute path to the folder in which the nightmusic tracks are stored.

    nightmusic_folder  (public)

     Absolute path to the jingle that plays between each track when playing
     nightmusic.

    nightmusic_jingle  (public)

     Whether to acknowledge the outage as planned, unplanned or not at all.

    situation  (public)

     What to play for the listener.

    status  (public)

     How much to amplify the technical problems jingle. Each sample will be
     multiplied by this value. Experimentation or analyzing the audio file is the
     best way to determine this.

    technical_problems_amplification  (public)

     Absolute filepath to the jingel to play when there are technical problems.

    technical_problems_jingle  (public)

     Absolute path to where the LiquidSoap script is stored. By placing this path
     inside /etc/liquidsoap and using the .liq file extension, the file will be used
     by the LiquidSoap service.

    liquidsoap_script  (public)

     True if there are live shows present in the schedule, false if not. This
     determines whether to play reruns or technical problems in shows that don't look
     like reruns.

    liveshows_present  (public)

     Command to use when invoking LiquidSoap directly, for example to verify a
     LiquidSoap script.

    liquidsoap_command  (public)

     Name of the service to restart (using SystemD) when asked to restart or find
     last restart of LiquidSoap.

    liquidsoap_service_name  (public)

     Path to the directory in which recordings are to be saved.

    recording_directory  (public)

    """

    def __init__(self, fd):
        """
         Initialize settings either from default values, or from an existing settings
         file.

        @param file object fd : File to read configuration from. Optional.
        @return  :
        @author
        """
        pass

    def write(self, fd):
        """
         Write the settings to the given file.

        @param file object fd : File object to write the settings to.
        @return  :
        @author
        """
        pass



