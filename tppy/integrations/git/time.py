import subprocess

import re
import types

from repositories.story.storyHttpImpl import StoryHTTPImpl


def add(description, time):
    story_id = _getTicketNumber(_getCurrentBranch())
    # Get tasks
    tasks = StoryHTTPImpl().findWithTasks(story_id)
    # If not exist, create task
    # Decide task
    # Add time to task
    print "Added time"


def _getCurrentBranch():
    process = subprocess.Popen(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], shell=False, stdout=subprocess.PIPE)
    output = process.communicate()
    if output[1]:
        print "ERROR: " + output[1]
    return output[0]


def _getTicketNumber(branch):
    from tppy.integrations.git.exceptions.NoSuitableBranchFound import NoSuitableBranchFound
    match = re.match('.*/(\d+).*', branch)
    if match is not None:
        return match.group(1)
    raise NoSuitableBranchFound(branch)
