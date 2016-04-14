def time_add_prompt(description):
    """
    Prompts you for hours spent on the current ticket.
    :param description: Timesheet description
    """
    try:
        hours = float(raw_input("How many hours did you spent on this ticket? (ex. 2.5)  "))
        from tppy.integrations.git.time import add
        add(description, hours)
    except:
        print "Not a valid input"
        exit()


def testing_move_prompt():
    """
    Prompts you for moving the ticket to "In Testing"
    """
    try:
        answer = raw_input("Do you want to move the ticket to 'In Testing'? y/N  ")
        if answer.lower().startswith('y'):
            from tppy.namespaces.ticket import test
            from tppy.integrations.git import helpers
            ticket_id = helpers.getCurrentTicketNumber()
            test(ticket_id)
    except:
        print "Not a valid input"
        exit()


def in_progress_move_prompt():
    """
    Prompts you for moving the ticket to "In Progress"
    """
    try:
        answer = raw_input("Do you want to move the ticket to 'In Progress'? Y/n  ")
        if answer.lower().startswith('y'):
            from tppy.integrations.git import helpers
            from tppy.namespaces.ticket import start
            ticket_id = helpers.getCurrentTicketNumber()
            start(ticket_id)
    except:
        print "Not a valid input"
        exit()
