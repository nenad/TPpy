from repositories.project.projectHttpImpl import ProjectHTTPImpl


def view(project_id):
    print ProjectHTTPImpl().find(project_id)
