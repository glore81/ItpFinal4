class User:

    def display_role(self):
        return "User can only view tasks"

    def can_view_statistics(self):
        return True

    def can_view_tasks(self):
        return True

    def can_add_task(self):
        return False

    def can_edit_task(self):
        return False

    def can_delete_task(self):
        return False

    def can_mark_completed(self):
        return False

    def __str__(self):
        return "User"

class Admin(User):

    def display_role(self):
        return "Admin can manage all tasks"

    def can_add_task(self):
        return True

    def can_edit_task(self):
        return True

    def can_delete_task(self):
        return True

    def can_mark_completed(self):
        return True

    def __str__(self):
        return "Admin"