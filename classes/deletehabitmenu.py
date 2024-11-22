from classes.menu import menu
from classes.db.habit import habit
import questionary
import classes.habitsmenu

class deletehabitmenu(menu):
    """ This menu allows you to select and delete a habit.
        
        On success the selected habit will be removed from the habits list.
    """
    headline = "Delete a habit"
    def show(self):
        self.deleteHabit()
        return
    def deleteHabit(self):
        """ This method deletes a habit. 
        """
        choices = self.getAllHabitsAsChoices()

        self.clearScreen()
        answer = questionary.select(self.headline, choices).ask()
   
        if(answer == -1):
            mymenu=classes.habitsmenu.habitsmenu(self.con)
            answer=mymenu.show()
            mymenu.execute(answer)
            return

        result = habit(self.con)
        result.getByHabitId(answer)
        result.delete()

        answer = self.show()
        self.execute(answer)

    def execute(self, answer):
        return
        