from classes.menu import menu
from questionary import questionary
import classes.mainmenu

class statisticsmenu(menu):
    headline = "Your statistics"
    choices = [
        "Show all daily habits",
        "Show all weekly habits",
        "Show longest streak",
        "Back to main menu"
        ]            

    def execute(self, answer):
        match answer:
            case "Show all daily habits":
                self.showByType(1)
                questionary.press_any_key_to_continue().ask()
                answer = self.show()
                self.execute(answer)

            case "Show all weekly habits":
                self.showByType(7)
                questionary.press_any_key_to_continue().ask()                
                answer = self.show()
                self.execute(answer)

            case "Show longest streak":
                result = self.getLongestStreak()
                questionary.press_any_key_to_continue().ask()
                answer = self.show()
                self.execute(answer)

            case "Back to main menu":
                mymenu=classes.mainmenu.mainmenu(self.con)
                answer=mymenu.show()
                mymenu.execute(answer)


    def showByType(self, htype):
        tuple = (htype,)
        result = self.con.cursor().execute("SELECT * FROM habit where type = ?", tuple).fetchall()

        state = "daily" if int(htype) == 1 else "weekly"
        questionary.print("Here are all " + state + " tasks:")

        for x in result:
            questionary.print("ID: " + str(x[0]) + " " + x[1])

        return

    def getLongestStreak(self):
        result = self.con.cursor().execute("SELECT * FROM habit where longest_streak = (select max(longest_streak) from habit)").fetchall()

        questionary.print("Displaying the longest streak, or longest streaks if there are multiple:")
        for x in result:
            state = "daily" if int(x[3]) == 1 else "weekly"
            questionary.print("The longest streak is called " + x[1] + ": " + x[2] + ", a " + state + " task with " + str(x[7]) + " consequitve periods.")

        return


