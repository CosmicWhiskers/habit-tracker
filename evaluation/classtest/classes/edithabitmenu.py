from classes.menu import menu


class edithabitmenu(menu):
    headline = "Edit an existing habit"
    choices = [
        "Edit habits",
        "Check off habits",
        "Statistics",
        "Quit"
    ]            

    def editHabit(self):
        return  