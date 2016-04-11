from repositories.story.storyHttpImpl import StoryHTTPImpl
from tppy.integrations.git import helpers


def current():
    try:
        story_id = helpers.getTicketNumber(helpers.getCurrentBranch())
        story = StoryHTTPImpl().findWithTasks(story_id)
        print story
    except:
        print 'bad branch'
        pass
