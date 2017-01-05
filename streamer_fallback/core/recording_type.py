from enum import Enum, unique

@unique
class RecordingType(Enum):
    """Enum which tells what type of audio a recording is.

    Members:
        earlier_show: The recording is a recording of an earlier show. This is
            the most common type.
        commercial: The recording is actually a commercial.
        jingle: The recording is a jingle which is not globally used for the
            entire radio, but rather within one program.
        stinger: The recording is a jingle used by the entire radio, as a sort
            of trademark.
        music: The recording is a music track.
        other: Catch-all for all other types.
    """
    earlier_show = 1
    commercial = 2
    jingle = 3
    stinger = 4
    music = 5
    other = 6
