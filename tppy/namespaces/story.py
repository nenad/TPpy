from api.entities import story
from settings import config


def create(task_name):
    project_id = config.get_project_var('project_id')
    story.create(task_name, project_id)
