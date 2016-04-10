import subprocess
import re

from repositories.story.storyHttpImpl import StoryHTTPImpl
from tppy.namespaces import time
import api.entities.task as taskEntity


def add(description, hours):
    story_id = _getTicketNumber(_getCurrentBranch())
    story = StoryHTTPImpl().findWithTasks(story_id)
    tasks = story.tasks if story.tasks is not None else []

    while True:
        if len(tasks) > 0:
            print "[0] CREATE NEW TASK"
            for index, task in enumerate(tasks, 1):
                print "[%d] %s" % (index, task.name)
        try:
            selected = int(raw_input("\nEnter selection [0 - %d]: " % len(tasks)))
            if selected == 0:
                taskName = raw_input('\nEnter new task name: ')
                newTask = taskEntity.create(taskName, story.id)
                time.create(description, hours, newTask.id)
                break
            elif 0 < selected <= len(tasks):
                time.create(description, hours, tasks[selected - 1].id)
                break
            else:
                print "\nInput not valid!"
        except ValueError:
            print "\nInput not valid!"

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
