# coding=UTF-8

class LiquidSoap(object):
    """
    Representation of the LiquidSoap service (not a specific process). Is able
    to restart LiquidSoap, in order to make LiquidSoap use a new
    configuration.

    Attributes:
        liquidsoap_last_restart_time: Last time LiquidSoap was
            restarted.  Can be determined by running date -d "`LC_TIME=C
            systemctl show cups --property=ExecMainStartTimestamp | awk -F=
            '{print $2}'`" +%s
        liquidsoap_service_name: Name of the service to restart (using System)
            when asked to restart or find last restart of LiquidSoap.
        liquidsoap_command: Command to use when invoking LiquidSoap directly,
            for example to verify a LiquidSoap script.
    """

    def restart(self) -> None:
        """
        Restart LiquidSoap now.
        """
        pass

    def is_valid(self, path: str) -> bool:
        """
        Check whether the script at the given path has any errors.

        This does not interrupt the running LiquidSoap instance.

        Arguments:
            path: Absolute path to the script which is to be analyzed.

        Returns:
            True if the script has no errors, False if it has.
        """
        pass

    def __init__(self, liquidsoap_service_name: str, liquidsoap_command: str) -> None:
        """
        Initialize this instance of the LiquidSoap class.

        Arguments:
            liquidsoap_service_name: Corresponds to the attribute with the same name.
            liquidsoap_command: Corresponds to the attribute with the same name.
        """
        pass



