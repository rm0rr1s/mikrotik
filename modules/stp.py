import desiredState
from modules import counters

def check_stp(api, currentDate):
    params = {'protocol-mode': desiredState.stpMode}
    try:
        output = api(cmd='/interface/bridge/print')

        if output[0]['protocol-mode'] != desiredState.stpMode:
            api(cmd='/interface/bridge/set', numbers=0, **params)
            with open('log-{}.txt'.format(currentDate), 'a') as file:
                file.write('Set STP state to: {}\n'.format(desiredState.stpMode))
            counters.stpCorrections += 1
        else:
            with open('log-{}.txt'.format(currentDate), 'a') as file:
                file.write('No changes to STP state.\n')

    except Exception as unknown_error:
        with open('log-{}.txt'.format(currentDate), 'a') as file:
            file.write('Error has occurred: {}\n'.format(unknown_error))
