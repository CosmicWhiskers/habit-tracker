from classes.menu import menu
from classes.db.habit import habit
import questionary
import classes.habitsmenu

class edithabitmenu(menu):
    """ This menu allows you to edit an existing habit.

        On success the selected habit is changed based on user interaction
    """    
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

    # After selecting the habit, users can edit the habit parameter Name, Description and type
        editHabit.name = questionary.text(message = "Name: ", default = editHabit.name).ask()
        editHabit.description = questionary.text(message = "Description: ", default = editHabit.description).ask()
        editHabit.htype = questionary.select(message = "Type: ", choices = (questionary.Choice("Daily", 1), questionary.Choice("Weekly", 7)), default = int(editHabit.htype)).ask()
    
    # Updated habit will be shown in habit list
        editHabit.update()
        self.show()

    def execute(self, answer):
        return
