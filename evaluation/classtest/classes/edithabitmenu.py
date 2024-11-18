from classes.menu import menu
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
        
        editHabit=habit()



        #self.con.cursor().execute("DELETE FROM habit where habit_id = " + str(answer))
        self.con.commit()

        self.show()

    def execute(self, answer):
        return
