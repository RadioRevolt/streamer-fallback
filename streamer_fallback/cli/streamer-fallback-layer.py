# coding=UTF-8
from overview.statuses import *
from overview.situation import *

class streamer_fallback_layer(object):

    """
     Abstraction of the communication with streamer-fallback core. It eases access to
     the current status, changes to the status and restart of LiquidSoap.

    :version:
    :author:
    """

    """ ATTRIBUTES

     Implemented using properties. Mirrors current_status in core.

    current_status  (public)

     Implemented using properties. Mirrors current_situation in core.

    current_situation  (public)

     Implemented using properties in Python, allowing data validation and such.
     Mirrors the live_shows attribute of core

    live_shows_present  (public)

     Implemented using properties. Mirrors the nightmusic_show_name attribute of core

    nightmusic_show_name  (public)

     PID of the currently (or last) running streamer-fallback-core process.

    last_pid  (protected)

     File pointer for the currently running process of streamer-fallback-core's
     stderr.

    last_stderr  (protected)

     True if all changes have been committed, False if not.

    changes_committed  (public)

     The attributes' values in streamer-fallback-core.

    committed_values  (public)

     True if LiquidSoap's config has been changed but LiquidSoap hasn't taken it into
     use yet, False otherwise.

    liquidsoap_needs_restart  (public)

    """

    def commit(self):
        """
         Apply any changes to the attributes to streamer-fallback-core, and restart
         LiquidSoap to take those changes into effect.

        @return  :
        @author
        """
        pass

    def commit_at(self, datetime):
        """
         Propogate any changes to the attributes to streamer-fallback-core, but do not
         restart LiquidSoap before the given time.

        @param datetime.datetime datetime : The time at which LiquidSoap should be restarted.
        @return  :
        @author
        """
        pass

    def get_progress(self):
        """
         Poll streamer-fallback-core for its progress.
         
         This can only be run in parallell to another call to streamer-fallback-layer.
         Running multiple operations at once is not supported.

        @return int :
        @author
        """
        pass

    def prepare(self, start_date, end_date):
        """
         Prepare for a period of downtime.

        @param datetime.date start_date : First date for which reruns and schedules shall be downloaded now.
        @param object end_date : The last date for which reruns and schedules shall be downloaded now. Can be either a datetime.date which is used as-is or a datetime.timedelta, in which case it will be added to the start_date.
        @return  :
        @author
        """
        pass

    def commit_no_restart(self):
        """
         Propogate any changes to the attributes to the streamer-fallback-core, but do
         not restart LiquidSoap. This lets you restart LiquidSoap later, in cases where
         you do not know the time right now.

        @return  :
        @author
        """
        pass

    def restart(self, time_to_restart):
        """
         Restart LiquidSoap to apply any changes that has been committed earlier using
         commit_no_restart()

        @param datetime.datetime time_to_restart : When to restart. Can be either datetime.datetime, which is used as-is, or datetime.timedelta, which is added to the current datetime. A value of 0 means restart now.
        @return  :
        @author
        """
        pass

    def _run_command(self, command):
        """
         Helper function for running a command and extracting its PID and stderr so the
         progress can be polled.

        @param string command : The command to run, given as a list of arguments.
        @return string :
        @author
        """
        pass



