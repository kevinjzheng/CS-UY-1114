# WE ASSUME, IN THIS WORLD, LEAP YEARS DON'T EXIST. FEBRUARY ONLY HAS 28 DAYS

# 1. Important about lists: Passing lists around. They all point to the same thing in memory. once changed, forever changed everywhere
class Calendar:
    def __init__(self):

        today_date = input("Please enter today's date in mm/dd/yy format: ")

        self.day = int(today_date[3:5])
        self.month = int(today_date[:2])
        self.year = int(today_date[-2:])

        self.day_of_week_int = int(input("Please enter the day of the week today (1 for Monday and 7 for Sunday): "))

        # Passing in a completely new COPY of the check list
        # This way check list will not get modified
        self.to_do_list = ToDoList()

    def convert_int_to_day_of_week(self):
        if self.day_of_week_int == 1:
            return "Monday"
        elif self.day_of_week_int == 2:
            return "Tuesday"
        elif self.day_of_week_int == 3:
            return "Wednesday"
        elif self.day_of_week_int == 4:
            return "Thursday"
        elif self.day_of_week_int == 5:
            return "Friday"
        elif self.day_of_week_int == 6:
            return "Saturday"
        else:
            return "Sunday"

    def set_next_day_of_week_int(self):
        self.day_of_week_int = (self.day_of_week_int % 7) + 1

    def set_next_day_date(self):
        if self.month in [4, 6, 9, 11]:
            self.month += self.day // 30
            self.day = (self.day % 30) + 1
        elif self.month == 2:
            self.month += self.day // 28
            self.day = (self.day % 28) + 1
        else:
            self.month += self.day // 31
            self.day = (self.day % 31) + 1

        if self.month > 12:
            self.month = 1
            self.year += 1

    def start_new_day(self):
        self.set_next_day_date()
        self.set_next_day_of_week_int()
        # Again I'm sending in a copy
        self.to_do_list = ToDoList()
        print(repr(self))

    def __repr__(self):
        result = '\n'
        result += "Today's date is: "
        result += self.convert_int_to_day_of_week()
        result += " " + str(self.month) + "/" + str(self.day) + "/" + str(self.year) + "\n\n"

        result += repr(self.to_do_list)

        return result


class ToDoList:
    def __init__(self):
        self.to_do_list = []

    def create_to_do_list_item(self):
        task = input("Enter the task: ")
        to_do_list_item = [task, False]
        self.to_do_list.append(to_do_list_item)

    def check_to_do_list(self):
        for to_do_item in self.to_do_list:
            if to_do_item[1] == False:  # if done is not true
                answer = input("Did you " + to_do_item[0] + "? (y/n) ")
                if answer.upper() == "Y":
                    to_do_item[1] = True

        print("\nUpdated To-Do List:\n")
        print(repr(self))

    def __repr__(self):
        string_repr = ''

        string_repr += "Today's Accomplishment\n"
        string_repr += "=========================\n"
        for to_do_item in self.to_do_list:
            if to_do_item[1] == True:
                string_repr += to_do_item[0] + "\n"

        string_repr += "\n"
        string_repr += "Things Left To Do\n"
        string_repr += "=========================\n"

        for to_do_item in self.to_do_list:
            if to_do_item[1] == False:
                string_repr += to_do_item[0] + "\n"

        return string_repr


def main():
    calendar = Calendar()
    while True:

        print("\nMain Menu:")
        print("1. Create New Calendar")
        print("2. Add To-Do List Item")
        print("3. Check Off To-Do List")
        print("4. Show Today's Calendar")
        print("5. Start The Next Day\n")

        answer = input("What would you like to do? ")
        if answer == '1':
            calendar = Calendar()
        elif answer == '2':
            calendar.to_do_list.create_to_do_list_item()
        elif answer == '3':
            calendar.to_do_list.check_to_do_list()
        elif answer == '4':
            print(repr(calendar))
        elif answer == '5':
            calendar.start_new_day()


main()


