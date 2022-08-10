# Airports
import sys
import os

cost_fc = 0
cost_sc = 0
distance = 0
no_of_sc_seats = 0
max_flight_range = 0
sc_capacity = 0
min_no_of_fc_seats = 0
no_of_fc_seats = 0
flight_selection = ""
air_code_uk = ""
air_code_overseas = ""
airport_index = 0
not_overseas = True
flight_cost_per_seat = 0
planeType = [["8", "2650", "180", "8"], ["7", "5600", "220", "10"], ["5", "4050", "406", "14"]]
all_lines = []
all_lines_and_var = []

# Read in the comma separated file Airport.txt
with open("Airport.txt", "w") as file:
    file.write("JFK,John F Kennedy International,5326 5486\n")
    file.write("ORY,Paris-Orly,629 379\n")
    file.write("MAD,Adolfo Suarez Madrid-Barajas,1428 1151\n")
    file.write("AMS,Amsterdam Schiphol,526 489\n")
    file.write("CAI,Cairo International,3779 3584")
    file.close()
with open("Airport.txt", "r") as file:
    s = ""
    line_count = 0
    while (s == file.readline()) != None:
        all_lines[line_count] = s
        line_count += line_count
    for i in range(5):
        temp_array = all_lines[i].split(',')
        for j in range(temp_array.len()):
            all_lines_and_var[i, j] = temp_array[j]

# Menu


def menu():
    print("**********")
    print("Main Menu")
    print("**********")
    print("1: Enter airport details")
    print("2: Enter flight details")
    print("3: Enter price plan and calculate profit")
    print("4: Clear data")
    print("5: Quit")
    selection = input("Please select an option: ")
    if selection == "1":
        airport_details()
    elif selection == "2":
        flight_details()
    elif selection == "3":
        price_plan_and_calculate_profit()
    elif selection == "4":
        clear = lambda: os.system('cls')
        clear()
    elif selection == "5":
        print("You have quit the program")
        sys.exit()
    else:
        print("Invalid selection")
# end of menu


# Airport details


def airport_details():
    print("Airport details")
    print("***************")
    global air_code_uk
    global air_code_overseas
    global airport_index
    global not_overseas
    global distance
    air_code_uk = input("Enter 3 letter airport code for UK airport: ")
    if air_code_uk != "LPL" and air_code_uk != "BOH":
        print("Invalid airport")
        menu()
    else:
        air_code_overseas = input("Enter 3 letter code for overseas airport: ")
        for i in range(5):
            if all_lines_and_var[i][0] == air_code_overseas:
                not_overseas = False
                airport_index = i
        if not_overseas:
            print("Invalid airport")
        else:
            print(all_lines_and_var[airport_index][1])
            if air_code_uk == "LPL":
                distance = int(all_lines_and_var[airport_index][2])
            else:
                distance = int([airport_index][3])
    menu()  # Returns user to main menu


def flight_details():
    print("Flight Details")
    print("**************")
    print("1: Medium narrow body \n2: Large narrow body " + "\n3: Medium wide body")
    global min_no_of_fc_seats
    global sc_capacity
    global max_flight_range
    global flight_selection
    global flight_cost_per_seat
    flight_selection = input("Enter type of aircraft: ")
    if flight_selection == "1":
        print("\nMedium narrow body: \nRunning cost per 100km: £" + planeType[0][0] + "\nMaximum flight range: " + planeType[0][1] + "km\nCapacity if all seats are standard class: " + planeType[0][2] + "\nMinimum number of first-class seats (if there are any): " + planeType[0][3])
        min_no_of_fc_seats = int(planeType[0][3])
        sc_capacity = int(planeType[0][2])
        max_flight_range = int(planeType[0][1])
        flight_cost_per_seat = (float(planeType[0][0]) * distance) / 100
        choose_number_of_fc_seats()
    elif flight_selection == "2":
        print("\nLarge narrow body: \nRunning cost per 100km: £" + planeType[1][0] + "\nMaximum flight range: " + planeType[1][1] + "km\nCapacity if all seats are standard class: " + planeType[1][2] + "\nMinimum number of first-class seats (if there are any): " + planeType[1][3])
        min_no_of_fc_seats = int(planeType[1][3])
        sc_capacity = int(planeType[1][2])
        max_flight_range = int(planeType[1][1])
        flight_cost_per_seat = (float(planeType[1][0]) * distance) / 100
        choose_number_of_fc_seats()
    elif flight_selection == "3":
        print("\nMedium wide body: \nRunning cost per 100km: £" + planeType[2][0] + "\nMaximum flight range: " + planeType[2][1] + "km\nCapacity if all seats are standard class: " + planeType[2][2] + "\nMinimum number of first-class seats (if there are any): " + planeType[2][3])
        min_no_of_fc_seats = int(planeType[2][3])
        sc_capacity = int(planeType[2][2])
        max_flight_range = int(planeType[2][1])
        flight_cost_per_seat = (float(planeType[2][0]) * distance) / 100
        choose_number_of_fc_seats()
    else:
        print("Invalid selection")
        menu()
# end of flight details


def choose_number_of_fc_seats():
    global no_of_fc_seats
    global no_of_sc_seats
    no_of_fc_seats = int(input("Enter number of first class seats: "))
    if no_of_fc_seats != 0:
        if no_of_fc_seats < min_no_of_fc_seats:
            print("Sorry, you must have a minimum number of " + str(min_no_of_fc_seats) + " first class seats")
            menu()
        if min_no_of_fc_seats > (sc_capacity / 2):
            print("Sorry, you have selected too many first class seats")
            menu()
    no_of_sc_seats = sc_capacity - no_of_fc_seats * 2
    menu()
# end of choose_number_of_fc_seats


def price_plan_and_calculate_profit():
    print("Price Plan and Profit")
    print("*********************")
    if air_code_uk == "" or air_code_overseas == "":
        print("Please add airports")
        menu()
    elif flight_selection == "":
        print("Please choose an aircraft")
        menu()
    elif no_of_sc_seats >= 0:
        print("Please choose number of seats")
        menu()
    elif max_flight_range < int(distance):
        print("The plane cannot fly that far")
        menu()
    else:
        price_of_fc_seat = input("Enter the cost of a First Class Seat")
        price_of_sc_seat = input("Enter the cost of a Standard Class Seat")
        flight_cost = flight_cost_per_seat * (no_of_fc_seats + no_of_sc_seats)
        flight_income = (no_of_fc_seats * price_of_fc_seat) + (no_of_sc_seats * price_of_sc_seat)
        flight_profit = float(flight_income) - flight_cost
        print("Flight cost per seat: " + str(flight_cost_per_seat))
        print("Flight cost: £" + str(flight_cost))
        print("Flight income: £" + flight_income)
        print("Flight Profit: £" + str(flight_profit))
        menu()
# end of price_plan_and_calculate_profit


menu()
# Airports
import sys
import os

cost_fc = 0
cost_sc = 0
distance = 0
no_of_sc_seats = 0
max_flight_range = 0
sc_capacity = 0
min_no_of_fc_seats = 0
no_of_fc_seats = 0
flight_selection = ""
air_code_uk = ""
air_code_overseas = ""
airport_index = 0
not_overseas = True
flight_cost_per_seat = 0
planeType = [["8", "2650", "180", "8"], ["7", "5600", "220", "10"], ["5", "4050", "406", "14"]]
all_lines = []
all_lines_and_var = []

# Read in the comma separated file Airport.txt
with open("Airport.txt", "w") as file:
    file.write("JFK,John F Kennedy International,5326 5486\n")
    file.write("ORY,Paris-Orly,629 379\n")
    file.write("MAD,Adolfo Suarez Madrid-Barajas,1428 1151\n")
    file.write("AMS,Amsterdam Schiphol,526 489\n")
    file.write("CAI,Cairo International,3779 3584")
    file.close()
with open("Airport.txt", "r") as file:
    s = ""
    line_count = 0
    while (s == file.readline()) != None:
        all_lines[line_count] = s
        line_count += line_count
    for i in range(5):
        temp_array = all_lines[i].split(',')
        for j in range(temp_array.len()):
            all_lines_and_var[i, j] = temp_array[j]

# Menu


def menu():
    print("**********")
    print("Main Menu")
    print("**********")
    print("1: Enter airport details")
    print("2: Enter flight details")
    print("3: Enter price plan and calculate profit")
    print("4: Clear data")
    print("5: Quit")
    selection = input("Please select an option: ")
    if selection == "1":
        airport_details()
    elif selection == "2":
        flight_details()
    elif selection == "3":
        price_plan_and_calculate_profit()
    elif selection == "4":
        clear = lambda: os.system('cls')
        clear()
    elif selection == "5":
        print("You have quit the program")
        sys.exit()
    else:
        print("Invalid selection")
# end of menu


# Airport details


def airport_details():
    print("Airport details")
    print("***************")
    global air_code_uk
    global air_code_overseas
    global airport_index
    global not_overseas
    global distance
    air_code_uk = input("Enter 3 letter airport code for UK airport: ")
    if air_code_uk != "LPL" and air_code_uk != "BOH":
        print("Invalid airport")
        menu()
    else:
        air_code_overseas = input("Enter 3 letter code for overseas airport: ")
        for i in range(5):
            if all_lines_and_var[i][0] == air_code_overseas:
                not_overseas = False
                airport_index = i
        if not_overseas:
            print("Invalid airport")
        else:
            print(all_lines_and_var[airport_index][1])
            if air_code_uk == "LPL":
                distance = int(all_lines_and_var[airport_index][2])
            else:
                distance = int([airport_index][3])
    menu()  # Returns user to main menu


def flight_details():
    print("Flight Details")
    print("**************")
    print("1: Medium narrow body \n2: Large narrow body " + "\n3: Medium wide body")
    global min_no_of_fc_seats
    global sc_capacity
    global max_flight_range
    global flight_selection
    global flight_cost_per_seat
    flight_selection = input("Enter type of aircraft: ")
    if flight_selection == "1":
        print("\nMedium narrow body: \nRunning cost per 100km: £" + planeType[0][0] + "\nMaximum flight range: " + planeType[0][1] + "km\nCapacity if all seats are standard class: " + planeType[0][2] + "\nMinimum number of first-class seats (if there are any): " + planeType[0][3])
        min_no_of_fc_seats = int(planeType[0][3])
        sc_capacity = int(planeType[0][2])
        max_flight_range = int(planeType[0][1])
        flight_cost_per_seat = (float(planeType[0][0]) * distance) / 100
        choose_number_of_fc_seats()
    elif flight_selection == "2":
        print("\nLarge narrow body: \nRunning cost per 100km: £" + planeType[1][0] + "\nMaximum flight range: " + planeType[1][1] + "km\nCapacity if all seats are standard class: " + planeType[1][2] + "\nMinimum number of first-class seats (if there are any): " + planeType[1][3])
        min_no_of_fc_seats = int(planeType[1][3])
        sc_capacity = int(planeType[1][2])
        max_flight_range = int(planeType[1][1])
        flight_cost_per_seat = (float(planeType[1][0]) * distance) / 100
        choose_number_of_fc_seats()
    elif flight_selection == "3":
        print("\nMedium wide body: \nRunning cost per 100km: £" + planeType[2][0] + "\nMaximum flight range: " + planeType[2][1] + "km\nCapacity if all seats are standard class: " + planeType[2][2] + "\nMinimum number of first-class seats (if there are any): " + planeType[2][3])
        min_no_of_fc_seats = int(planeType[2][3])
        sc_capacity = int(planeType[2][2])
        max_flight_range = int(planeType[2][1])
        flight_cost_per_seat = (float(planeType[2][0]) * distance) / 100
        choose_number_of_fc_seats()
    else:
        print("Invalid selection")
        menu()
# end of flight details


def choose_number_of_fc_seats():
    global no_of_fc_seats
    global no_of_sc_seats
    no_of_fc_seats = int(input("Enter number of first class seats: "))
    if no_of_fc_seats != 0:
        if no_of_fc_seats < min_no_of_fc_seats:
            print("Sorry, you must have a minimum number of " + str(min_no_of_fc_seats) + " first class seats")
            menu()
        if min_no_of_fc_seats > (sc_capacity / 2):
            print("Sorry, you have selected too many first class seats")
            menu()
    no_of_sc_seats = sc_capacity - no_of_fc_seats * 2
    menu()
# end of choose_number_of_fc_seats


def price_plan_and_calculate_profit():
    print("Price Plan and Profit")
    print("*********************")
    if air_code_uk == "" or air_code_overseas == "":
        print("Please add airports")
        menu()
    elif flight_selection == "":
        print("Please choose an aircraft")
        menu()
    elif no_of_sc_seats >= 0:
        print("Please choose number of seats")
        menu()
    elif max_flight_range < int(distance):
        print("The plane cannot fly that far")
        menu()
    else:
        price_of_fc_seat = input("Enter the cost of a First Class Seat")
        price_of_sc_seat = input("Enter the cost of a Standard Class Seat")
        flight_cost = flight_cost_per_seat * (no_of_fc_seats + no_of_sc_seats)
        flight_income = (no_of_fc_seats * price_of_fc_seat) + (no_of_sc_seats * price_of_sc_seat)
        flight_profit = float(flight_income) - flight_cost
        print("Flight cost per seat: " + str(flight_cost_per_seat))
        print("Flight cost: £" + str(flight_cost))
        print("Flight income: £" + flight_income)
        print("Flight Profit: £" + str(flight_profit))
        menu()
# end of price_plan_and_calculate_profit


menu()
