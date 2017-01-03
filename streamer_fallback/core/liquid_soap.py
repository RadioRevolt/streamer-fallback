# coding=UTF-8

class LiquidSoap(object):

    """
     Representation of the LiquidSoap service (not a specific process). Is able to
     restart LiquidSoap, in order to make LiquidSoap use a new configuration.

    :version:
    :author:
    """

    """ ATTRIBUTES

     Last time LiquidSoap was restarted.
     
     Can be determined by running date -d "`LC_TIME=C systemctl show cups
     --property=ExecMainStartTimestamp | awk -F= '{print $2}'`" +%s

    liquidsoap_last_restart_time  (public)

     Name of the service to restart (using SystemD) when asked to restart or find
     last restart of LiquidSoap.

    liquidsoap_service_name  (private)

     Command to use when invoking LiquidSoap directly, for example to verify a
     LiquidSoap script.

    liquidsoap_command  (private)

    """

    def restart(self):
        """
         Restart LiquidSoap now.

        @return  :
        @author
        """
        pass

    def is_valid(self, path):
        """
         Analyze the script located at the given path to determine whether it is a valid
         script.
         
         This does not interrupt the running LiquidSoap instance.

        @param string path : Absolute path to the script which is to be analyzed.
        @return bool :
        @author
        """
        pass

    def __init__(self, liquidsoap_service_name, liquidsoap_command):
        """
         Initialize this instance of the LiquidSoap class.

        @param string liquidsoap_service_name : Corresponds to the attribute with the same name.
        @param string liquidsoap_command : Corresponds to the attribute with the same name.
        @return  :
        @author
        """
        pass



