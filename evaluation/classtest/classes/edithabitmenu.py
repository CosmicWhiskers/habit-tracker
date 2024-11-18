from classes.menu import menu
from classes.db.habit import habit
import questionary
import classes.habitsmenu

class edithabitmenu(menu):
    headline = "Edit a habit"
    def show(self):
        self.editHabit()
    def editHabit(self):
        choices = self.getAllHabitsAsChoices()

        self.clearScreen()
        answer = questionary.select(self.headline, choices).ask()
   
        if(answer == -1):
            mymenu=classes.habitsmenu.habitsmenu(self.con)
            answer=mymenu.show()
            mymenu.execute(answer)
            return
        
        editHabit=habit(self.con)
        editHabit.getByHabitId(answer)

        editHabit.name = questionary.text(message = "Name:", default = editHabit.name).ask()
        editHabit.description = questionary.text(message = "Description:", default = editHabit.description).ask()

        editHabit.update()
        self.show()

    def execute(self, answer):
        return
