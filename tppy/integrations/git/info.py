from repositories.assignable.assignableRepo import AssignableRepository
from repositories.story.storyHttpImpl import StoryHTTPImpl
from tp.models.entity import EntityType
from tppy.integrations.git import helpers


def current():
    try:
        ticket_id = helpers.getCurrentTicketNumber()
        assignable = AssignableRepository().find(ticket_id)
        if assignable.entityType == EntityType.USERSTORY:
            story_id = helpers.getTicketNumber(ticket_id)
            story = StoryHTTPImpl().findWithTasks(story_id)
            print story
        else:
            print assignable
    except:
        print 'bad branch'
        pass
