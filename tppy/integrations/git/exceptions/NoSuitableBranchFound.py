class NoSuitableBranchFound(Exception):
    def __init__(self, branch):
        self.branch = branch
