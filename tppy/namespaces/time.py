from api.entities import time


def create(description, hours, assignable_id):
    time.create(description, hours, assignable_id)
