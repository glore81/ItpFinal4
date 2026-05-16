class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_user(self):
        print("User can only view tasks")

    def get_email(self):
        return self.email

    def can_view_statistics(self):
        return True

    def can_view_task(self):
        return True

    def can_add_task(self):
        return False

    def can_edit_task(self):
        return False

    def can_delete_task(self):
        return False

    def can_mark_completed(self):
        return False

class Admin(User):
    def __init__(self, name, email):
        super().__init__(name, email)

    def display_user(self):
        print("Admin can manage all tasks")

    def can_add_task(self):
        return True

    def can_edit_task(self):
        return True

    def can_delete_task(self):
        return True

    def can_mark_completed(self):
        return True