from classes.db.habit import habit
from classes.menu import menu
import questionary
import classes.habitsmenu
from datetime import date, timedelta, datetime

class checkhabitsmenu(menu):
    """ This menu allows you to select and check off a habit.
        
        On success it returns to itself to enable checking off habits in rapid succession.
    """
    
    headline = "Check a habit"
    def show(self):
        self.showHabits()

    def showHabits(self):
        """ This method checks off a habit. 
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

        today = date.today()
        last_check = datetime.strptime(result.last_check, '%Y-%m-%d').date()

        # In result, we have last_check, which is the END of the current habit period.
        # Three possibilities:
        # 1) We are earlier than that period, which means we already checked this habit
        #   -> Display message that habit is already checked for this period and return
        # 2) We are later than the period, but not later than the next period
        #   -> We are in a current habit, and can update it. We update the streak by 1,
        #      and check if it's bigger than longest_streak. We also update total_checks by 1
        #      We also update the period to the end of the next one
        # 3) We are later than the period, and also later than the next period
        #   -> We check the period, but set current_streak back to 1, and also set the end
        #      of the next period

        # Case 1:
        if(today <= last_check):
            questionary.print("You already checked this habit for this period.")
        # Case 2:
        elif (today > last_check and abs((today-last_check).days) <= int(result.htype)):
            result.current_streak = result.current_streak + 1
            result.total_checks = result.total_checks + 1
            result.last_check = today
            if(result.current_streak > result.longest_streak):
                result.longest_streak = result.current_streak
            result.update()
            result.addHistory()
            self.con.commit()
            questionary.print("Successfully checked the habit for this period. Your current streak is now: " + str(result.current_streak) + ", your longest streak for this habit is " + str(result.longest_streak) + "." )
        # If the first two don't match, it is case 3 by default:
        else:
            result.current_streak = 1
            result.total_checks = result.total_checks + 1
            result.last_check = today
            result.update()
            result.addHistory()
            self.con.commit()
            questionary.print("You missed a time perion. Your streak reset!")


        # We already did a result output, so we wait for a key press and then return to the menu
        questionary.press_any_key_to_continue().ask()
        answer = self.show()
        self.execute(answer)

    def execute(self, answer):
        """
        We overwrite this to do nothing because we do all functionality above
        """
        return

