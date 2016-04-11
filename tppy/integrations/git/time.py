from repositories.story.storyHttpImpl import StoryHTTPImpl
from tppy.integrations.git.exceptions.NoSuitableBranchFound import NoSuitableBranchFound
from tppy.namespaces import time
import api.entities.task as taskEntity
from tppy.integrations.git.helpers import getCurrentBranch
from tppy.integrations.git.helpers import getTicketNumber
from colorama import init
from colorama import Fore


def add(description, hours):
    init()
    try:
        assignable_id = getTicketNumber(getCurrentBranch())
        story = StoryHTTPImpl().findWithTasks(assignable_id)
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
        print Fore.GREEN + "Added time"
    except NoSuitableBranchFound:
        print Fore.RED + "Cannot add time to this branch. Try checking out to a suitable branch first."

def today():
    pass
