n = input()
instructions = []
for i in range(n):
    instructions.append(input())
screens = {}


def add_screen(instruction):
    screen_name = instruction[1]
    num_of_rows = int(instruction[2])
    num_of_seats = int(instruction[3])
    aisle_seats = map(int, instruction[4:])
    if screen_name in screens.keys():
        print("failure")
    else:
        print("success")
        screens[screen_name] = [[[0] * (num_of_seats + 1) for i in range(num_of_rows)], aisle_seats]


def reserve_seat(instruction):
    screen_name = instruction[1]
    row_number = int(instruction[2])
    seats_to_reserve = map(int, instruction[3:])
    screen, aisle_seats = screens[screen_name][0], screens[screen_name][1]
    available = True
    for seat in seats_to_reserve:
        if screen[row_number][seat] == 1:
            available = False
    if available:
        for seat in seats_to_reserve:
            screen[row_number][seat] = 1
        print("success")
    else:
        print("failure")


def get_unreserved_seats(instruction):
    screen_name = instruction[1]
    row_number = int(instruction[2])
    screen, aisle_seats = screens[screen_name][0], screens[screen_name][1]
    unreserved_seats = [i for i in range(1, len(screen[row_number])) if screen[row_number][i] == 0]
    print(" ".join(map(str, unreserved_seats)))


def suggest_contiguous_seats(instruction):
    screen_name = instruction[1]
    num_of_seats = int(instruction[2])
    row_number = int(instruction[3])
    choice_of_seat_number = int(instruction[4])


for i in instructions:
    ins = i.split()
    command = ins[0]
    if command == "add-screen":
        add_screen(ins)
    elif command == "reserve-seat":
        reserve_seat(ins)
    elif command == "get-unreserved-seats":
        get_unreserved_seats(ins)
    elif command == "suggest-contiguous-seats":
        suggest_contiguous_seats(ins)

'''
Sample Test Case
 
6
"add-screen Screen1 12 10 4 5 8 9"
"add-screen Screen2 20 25 3 4 12 13 17 18"
"reserve-seat Screen1 4 5 6 7"
"reserve-seat Screen2 13 6 7 8 9 10"
"reserve-seat Screen2 13 4 5 6"
"get-unreserved-seats Screen2 13"
"suggest-contiguous-seats Screen1 3 3 4"
"suggest-contiguous-seats Screen2 4 12 4"
"suggest-contiguous-seats Screen2 4 10 3"
'''


