from datetime import datetime

def validate_priority(priority):
    priorities = ['low', 'medium', 'high']
    if priority in priorities:
        return True
    return False


def validate_status(status):
    statuses = ['pending', 'in_progress', 'completed']
    if status in statuses:
        return True
    return False


def validate_deadline(deadline):
    try:
        datetime.strptime(deadline, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def validate_task(task):
    if task.title == "":
        return False

    if task.description == "":
        return False

    if not validate_priority(task.priority):
        return False

    if not validate_status(task.status):
        return False

    if not validate_deadline(task.deadline):
        return False

    return True