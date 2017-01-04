from enum import Enum, unique

@unique
class Status(Enum):
    """Enum which tells what the listener shall hear if the streamer goes down.

    Members:
        technical_problems_jingle: A constant loop of a jingle saying that
            there are technical problems. Depending on the current situation,
            the problem may be presented as being planned or not planned
            (not acknowledged is treated as not planned).
        nightmusic: A collection of music from a set folder is played, with
            stinger playing between each track. The current situation decides
            which jingle to play in between.
        reruns: Transparent; make an attempt to cover up the lack of a proper
            stream by playing the same reruns that were scheduled to be
            played. The current situation is ignored. Shows with a name
            matching nightmusic_show_name will play nightmusic. Shows that
            look like live shows (no (R) in title and no rerun planned on
            the rerunner) will play the technical problems-jingle if
            live_shows_present is true, reruns of that show is run if not.
    """
    technical_problems_jingle = 1
    nightmusic = 2
    reruns = 3
