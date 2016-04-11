import subprocess
import re

from configuration import config
from tppy.integrations.git.exceptions.NoSuitableBranchFound import NoSuitableBranchFound


def getCurrentBranch():
    process = subprocess.Popen(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], shell=False, stdout=subprocess.PIPE)
    output = process.communicate()
    if output[1]:
        print "ERROR: " + output[1]
    return output[0]


def getTicketNumber(branch):
    match = re.match(config.get('branch_regex'), branch)
    if match is not None:
        return match.group(1)
    raise NoSuitableBranchFound(branch)


def getCurrentTicketNumber():
    return getTicketNumber(getCurrentBranch())


def getTicketType():
    raise NotImplementedError


def getCurrentTicket():
    raise NotImplementedError


