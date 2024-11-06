from classes.menu import menu

class deletehabitmenu(menu):
    headline = "Delete a habit"
    choices = [
        "Edit habits",
        "Check off habits",
        "Statistics",
        "Quit"
    ]            

    def deleteHabit(self):
        return  