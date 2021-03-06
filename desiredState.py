# Warning: If you would like to turn off a module, set all the variables for that module to None,
# or, turn off the module entirely by commenting out the function call in the "run.py" file.

ntpStatus = True  # "True" for NTP enabled, "False" for NTP disabled.
ntpServer = '91.209.0.17'  # set the desired NTP server IP address.

stpMode = 'rstp'  # turn on RSTP

snmpStatus = True  # enable SNMP, True or False
snmpCommunity = 'm0rr1sSnmpDoma1n'  # set the community string.

syslogServerName = 'SyslogServer'  # name for syslog server settings
syslogTarget = 'remote'  # syslog message target. ie, memory, remote, etc. Check documentation.
syslogIPaddress = '10.0.0.5'  # IP address of the remote syslog server
syslogBSDformat = True  # Enable BSD syslog format
