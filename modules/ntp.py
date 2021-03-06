import desiredState
from modules import counters

def check_ntp(api, currentDate):
    try:
        output = api(cmd='system/ntp/client/print')

        if output[0]['enabled'] != desiredState.ntpStatus:
            api(cmd='system/ntp/client/set', enabled=desiredState.ntpStatus)
            with open('log-{}.txt'.format(currentDate), 'a') as file:
                file.write('Set NTP enable status to {}.\n'.format(desiredState.ntpStatus))
            counters.ntpCorrections += 1
        else:
            with open('log-{}.txt'.format(currentDate), 'a') as file:
                file.write('No changes to NTP state.\n')

        params = {'primary-ntp': desiredState.ntpServer}

        if output[0]['primary-ntp'] != desiredState.ntpServer:
            api(cmd='/system/ntp/client/set', **params)
            with open('log-{}.txt'.format(currentDate), 'a') as file:
                file.write('Set the NTP server to {}.\n'.format(desiredState.ntpServer))
            counters.ntpCorrections += 1
        else:
            with open('log-{}.txt'.format(currentDate), 'a') as file:
                file.write('No changes to NTP server.\n')

    except Exception as unknown_error:
        with open('log-{}.txt'.format(currentDate), 'a') as file:
            file.write('Error has occurred: {}\n'.format(unknown_error))
