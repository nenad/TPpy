from repositories.assignable.assignableRepo import AssignableRepository
from tppy.integrations.git import helpers


def current():
    ticket_id = helpers.getCurrentTicketNumber()
    print find(ticket_id)


def find(assignable_id):
    try:
        print AssignableRepository().find(assignable_id)
    except:
        print "Ticket with id %s does not exist" % assignable_id
