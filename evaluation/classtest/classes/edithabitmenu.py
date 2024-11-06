from classes.menu import menu
import questionary
import classes.habitsmenu

class edithabitmenu(menu):
    headline = "Edit a habit"
    def show(self):
        self.editHabit()
    def editHabit(self):
        result = self.con.cursor().execute("SELECT * FROM habit")

        choices = []
        for x in result:
        #    print(x)
            choices.append(questionary.Choice(x[1],x[0]))

        choices.append(questionary.Choice("Back to habit menu", -1))
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