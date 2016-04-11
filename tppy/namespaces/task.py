from api.entities import task
from repositories.story.storyHttpImpl import StoryHTTPImpl


def create(task_name, story_id):
    print task.create(task_name, story_id)


def story(story_id):
    story = StoryHTTPImpl().findWithTasks(story_id)
    tasks = story.tasks

    print "S[%d] %s" % (story.id, story.name)
    for task in tasks:
        print "\t T[%d] %s" % (task.id, task.name)
