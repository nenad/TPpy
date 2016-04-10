from api.entities import time


def create(description, hours, assignable_id):
    print time.create(description, hours, assignable_id)
