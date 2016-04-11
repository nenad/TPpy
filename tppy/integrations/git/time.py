from api.entities import time
from repositories.assignable.assignableRepo import AssignableRepository
from repositories.story.storyHttpImpl import StoryHTTPImpl
from tppy.integrations.git.exceptions.NoSuitableBranchFound import NoSuitableBranchFound
import api.entities.task as taskEntity
from tppy.integrations.git.helpers import getCurrentBranch
from tppy.integrations.git.helpers import getTicketNumber
from colorama import init
from colorama import Fore


def add(description, hours):
    init()
    assignable_id = getTicketNumber(getCurrentBranch())
    assignable = None
    try:
        assignable = AssignableRepository().find(assignable_id)
    except:
        print "Can't find ticket with ID: %s" % assignable_id
        exit()

    if assignable.entityType == 'UserStory':
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
    else:
        time.create(description, hours, assignable_id)

    # Add time to task
    print Fore.GREEN + "Added time"
    total_time = today()
    print "Total time for today: %s" % total_time


def today():
    times = time.today()
    total = 0
    for t in times:
        total += float(t.spent)
        print "[%s] - %s (%s - %s)" % (t.spent, t.description, t.assignable.name, t.assignable.id)
    print "Total [%s]" % total

