import sys
import time
import desiredState
from modules import ntp, stp, snmp, syslog, counters

from librouteros import connect
from librouteros.query import Key

currentDate = time.strftime('%m-%d-%Y')  # get today's date; will be appended to log file name.


def login(username, password, device):  # manages connection process.
    try:
        api = connect(username=username, password=password, host=device)
        return api
    except Exception as unknown_error:
        print('Error has occurred: {}'.format(unknown_error))
        with open('log-{}.txt'.format(currentDate), 'a') as file:
            file.write('Error has occured: {}\n'.format(unknown_error))
        return None


username = 'api'
password = 'abc123'

print('----------------------------------')

startTime = time.time()

with open('log-{}.txt'.format(currentDate), 'a') as file: # timestamp new run
    file.write('-------------------------------------------\n')
    file.write('New run started at {}.\n'.format(time.strftime('%m-%d-%Y %H:%M:%S')))
    file.write('-------------------------------------------\n')

#  with open('devices_list') as file:    # this block reads the list of devices (hostnames or IPs) to be configured
#      devices_list = file.read().splitlines()

#  for device in devices_list:
device = '10.0.0.1'

print('Connecting to {}'.format(device))
api = login(username, password, device)  # establish a connection
# Librouteros does not raise an exception if the credentials are incorrect.
# It sets the connection variable to None instead.
# The below line checks if a connection really has been established, if not, tries next device.
if api == None:
    counters.connectionError += 1
    with open('log-{}.txt'.format(currentDate), 'a') as file:  # update log file
        file.write('Failed to establish a connection to {}\n'.format(device))
        file.write('--------------------------------------\n')
        print('Failed to establish a connection.')  # Moving on to next device.')
        print('----------------------------------------------------')
        #  continue
        sys.exit(2)

with open('log-{}.txt'.format(currentDate), 'a') as file: # log connection
    file.write('Connected to {}\n'.format(device))

# if you want to turn off a module, comment out the appropriate if statement and function call below.

if desiredState.ntpStatus != None:  # run NTP module if settings are present.
    ntp.check_ntp(api, currentDate)

#  if desiredState.stpMode != None:  # run STP module if settings are present.
#      stp.check_stp(api, currentDate)

#  if desiredState.snmpStatus != None:  # run SNMP modules if settings are present
#     snmp.check_snmp(api, currentDate)

#  if desiredState.syslogServerName != None:  # run the syslog module if settings are present
#      syslog.syslog(api, currentDate)

api.close()
with open('log-{}.txt'.format(currentDate), 'a') as file:
    file.write('-------------------------------------------\n')
print('----------------------------------')

#  print('End of device list')

with open('log-{}.txt'.format(currentDate), 'a') as file: # write summary
    file.write('End of run.\n')
    file.write('Changes Summary:\n')
    file.write('NTP corrections: {}\n'.format(counters.ntpCorrections))
    file.write('STP corrections: {}\n'.format(counters.stpCorrections))
    file.write('SNMP corrections: {}\n'.format(counters.snmpCorrections))
    file.write('Syslog corrections: {}\n'.format(counters.syslogCorrections))
    file.write('Connection Errors: {}\n'.format(counters.connectionError))
    file.write('-------------------------------------------\n')

totalRuntime = time.time() - startTime
print('Total runtime {}'.format(totalRuntime)) # display script runtime.




