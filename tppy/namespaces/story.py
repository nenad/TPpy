from api.entities import story
from repositories.story.storyHttpImpl import StoryHTTPImpl
from settings import config


def create(story_name):
    project_id = config.get_project_var('project_id')
    story.create(story_name, project_id)


