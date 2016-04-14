import datetime

from api.entities import time
from repositories.assignable.assignableRepo import AssignableRepository
from repositories.story.storyHttpImpl import StoryHTTPImpl
import api.entities.task as taskEntity
from colorama import Fore, Style


def add(description, hours, ticket_id='current'):
    """
    Creates a timesheet entry in TP for a given ticket
    :param description: Timesheet description
    :param hours: Hours worked on the ticket
    :param ticket_id: Ticket ID, default is current branch
    """
    from tppy.integrations.git.helpers import getCurrentBranch
    from tppy.integrations.git.helpers import getTicketNumber
    from colorama import init

    init()
    assignable = None
    if ticket_id == 'current':
        assignable_id = getTicketNumber(getCurrentBranch())
    else:
        assignable_id = ticket_id

    try:
        assignable = AssignableRepository().find(assignable_id)
    except:
        print "Can't find ticket with ID: %s" % assignable_id
        exit()

    if assignable.entityType == 'UserStory':
        story = StoryHTTPImpl().findWithTasks(assignable_id)
        tasks = story.tasks if story.tasks is not None else []
        while True:
            print "[0] CREATE NEW TASK"
            if len(tasks) > 0:
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
    today()


def date(date_str):
    """
    Prints timesheet for given date
    :param date_str: Date in format YYYY-MM-DD
    """
    times = time.atDate(date_str)
    total = 0
    for t in times:
        total += float(t.spent)
        print "[%s] - %s (%s - %s)" % (t.spent, t.description, t.assignable.name, t.assignable.id)
    print Fore.YELLOW + "Total [%s]" % total + Style.RESET_ALL


def today():
    """
    Prints today's timesheet
    """
    date_today = datetime.datetime.today().strftime('%Y-%m-%d')
    date(date_today)


def yesterday():
    """
    Prints yesterday's timesheet
    """
    date_yesterday = datetime.datetime.today() - datetime.timedelta(1)
    date(date_yesterday.strftime('%Y-%m-%d'))


