# coding=UTF-8
from streamer_fallback.core.status import Status
from streamer_fallback.core.situation import Situation

class LiquidSoapConfiguration(object):

    """
     Representation of a LiquidSoapConfiguration (that is, a LiquidSoap script),
     which also handles saving that configuration to a file.

    :version:
    :author:
    """

    """ ATTRIBUTES

     What to play for the listener.

    status  (public)

     Whether to acknowledge the outage as planned, unplanned or not at all.

    situation  (public)

     List of what to play at different times. Used only when the status is rerun.
     
     Each item is a tuple of three items. The first is when to start playing that
     recording. The second is when to stop playing that recording. The third is
     either an absolute path to the file to play, or the string "nightmusic" if
     nightmusic is to be played in that spot.
     
     Times where there are nothing playing, will play silence. After 12 seconds of
     silence, technical problems jingle will play.

    schedule  (public)

     Absolute filepath to the jingel to play when there are technical problems.

    technical_problems_jingle  (public)

     Absolute path to the jingle that plays between each track when playing
     nightmusic.

    nightmusic_jingle  (public)

     Mount to connect to on IceCast.

    icecast_mount  (public)

     Icecast host to connect to. Will usually be "localhost".

    icecast_host  (public)

     Password to use when connecting to IceCast as a source.

    icecast_password  (public)

     Port used by IceCast2.

    icecast_port  (public)

     True if the stream is to be in stereo, false if not.

    format_stereo  (public)

     Samplerate to use.

    format_samplerate  (public)

     The bitrate to use on the stream.

    format_bitrate  (public)

     Absolute path to the folder in which the nightmusic tracks are stored.

    nightmusic_folder  (public)

     How much to amplify the technical problems jingle. Each sample will be
     multiplied by this value. Experimentation or analyzing the audio file is the
     best way to determine this.

    technical_problems_amplification  (public)

    """

    def write(self, fd):
        """
         Export the resulting LiquidSoap script, writing it to the given file object.

        @param file object fd : The file object to write the script to.
        @return  :
        @author
        """
        pass

    def __init__(self):
        """
         Set this instance's attributes. They are not described here, but they can be
         provided as keyword arguments that set the corresponding attribute. All those
         parameters are optional.

        @return  :
        @author
        """
        pass



