from enum import Enum, unique

class Situation(Enum):
    """Enum which tells what we tell the listener about the downtime.

    Members:
        planned: Downtime is planned.
        unplanned: Downtime is not planned.
        hidden: Downtime is to be hidden or not acknowledged.
    """
    planned = 1
    unplanned = 2
    hidden = 3
