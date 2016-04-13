from api.entities import story
from repositories.story.storyHttpImpl import StoryHTTPImpl
from settings import config


def create(story_name):
    """
    Creates a story on the current project
    :param story_name: Story title
    """
    project_id = config.get_project_var('project_id')
    print story.create(story_name, project_id)


def view(story_id):
    """
    Prints information about given ticket
    :param story_id: Story Ticket ID
    """
    print StoryHTTPImpl().findWithTasks(story_id)
