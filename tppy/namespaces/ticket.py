from api.entities.entityState import State
from repositories.assignable.assignableRepo import AssignableRepository
from tppy.integrations.git import helpers


def current():
    """
    Prints information about the current branch
    """
    ticket_id = helpers.getCurrentTicketNumber()
    print find(ticket_id)


def find(assignable_id):
    """
    Lists information about the ticket
    :param assignable_id: Ticket ID
    """
    try:
        print AssignableRepository().find(assignable_id)
    except:
        print "Ticket with id %s does not exist" % assignable_id


def start(entity_id):
    """
    Move the ticket to In Progress
    :param entity_id: Ticket ID
    """
    _change_state(State.IN_PROGRESS, entity_id)


def stop(entity_id):
    """
    Move the ticket to Ready
    :param entity_id: Ticket ID
    """
    _change_state(State.READY, entity_id)


def test(entity_id):
    """
    Move the ticket to In Testing
    :param entity_id: Ticket ID
    """
    _change_state(State.IN_TESTING, entity_id)


def _change_state(state, entity_id):
    from api.entities.entityState import change_state
    try:
        change_state(state, entity_id)
        print "Ticket %s changed to %s" % (entity_id, state)
    except:
        print "Could not change state for ticket %s" % entity_id
