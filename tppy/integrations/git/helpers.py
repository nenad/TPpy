import subprocess
import re

from configuration import config
from repositories.assignable.assignableRepo import AssignableRepository
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
    id = getCurrentTicketNumber()
    assignable = AssignableRepository().find(id)


def getCurrentTicket():
    return config.get('hostname') + "/entity/" + getCurrentTicketNumber()
