from api.entities import task


def create(task_name, story_id):
    print task.create(task_name, story_id)
