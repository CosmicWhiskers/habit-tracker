from classes.menu import menu

class deletehabitmenu(menu):
    headline = "Choose and delete a habit"
    choices = [
        "Edit habits",
        "Check off habits",
        "Statistics",
        "Quit"
    ]            

    def deleteHabit(self):
        return  