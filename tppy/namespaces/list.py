from repositories.project.projectHttpImpl import ProjectHTTPImpl


def projects():
    all_projects = ProjectHTTPImpl().getAll()
    for project in all_projects:
        print project
