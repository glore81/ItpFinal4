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