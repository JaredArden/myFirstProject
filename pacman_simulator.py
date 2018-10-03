class Pacman:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction


    # Move Pacman in the corresponding direction if possible
    def move(self):
        if self.direction == "EAST":
            if self.x < 4:
                self.x += 1
        elif self.direction == "WEST":
            if self.x > 0:
                self.x -= 1
        elif self.direction == "NORTH":
            if self.y < 4:
                self.y += 1
        elif self.direction == "SOUTH":
            if self.y > 0:
                self.y -= 1
        else: # This line should never be reached
            print("Error: invalid direction")


    # Rotate Pacman 90 degrees counter-clockwise
    def rotate_left(self):
        if self.direction == "EAST":
            self.direction = "NORTH"
        elif self.direction == "NORTH":
            self.direction = "WEST"
        elif self.direction == "WEST":
            self.direction = "SOUTH"
        elif self.direction == "SOUTH":
            self.direction = "EAST"
        else: # This line should never be reached
            print("Error: invalid direction")


    # Rotate Pacman 90 degrees clockwise
    def rotate_right(self):
        if self.direction == "EAST":
            self.direction = "SOUTH"
        elif self.direction == "SOUTH":
            self.direction = "WEST"
        elif self.direction == "WEST":
            self.direction = "NORTH"
        elif self.direction == "NORTH":
            self.direction = "EAST"
        else: # This line should never be reached
            print("Error: invalid direction")

    # Announce Pacman's x and y coordiantes along with direction
    # Output format example: 0,1,NORTH
    def report(self):
        print(str(self.x) + "," + str(self.y) + "," + str(self.direction))


# Returns x or y position if valid, returns -1 otherwise
# Precondition: coordinate is either 'x' or 'y'
def validate_position(command, coordinate):
    try:
        if coordinate == 'x':
            position = int(command[len("PLACE 0")-1]) # get x position from the command
        elif coordinate == 'y':
            position = int(command[len("PLACE 0,0")-1]) # get y position from the command
        else:
            print("Error invalid coordinate") # This line should never be reached
        
        if position < 0 or position > 4:
            print(str(coordinate) + " position out of range")
            return -1
        return position

    except IndexError:
        print("Index error invalid " + str(coordinate) + " position")
        return -1

    except ValueError:
        print("Value error invalid " + str(coordinate) + " position")
        return -1
        

# Returns direction if valid, returns empty string otherwise
def validate_direction(command):
    direction = command[len("PLACE X,Y,"):len(command)]
    if direction == "NORTH" or direction == "SOUTH" or direction == "EAST" or direction == "WEST":
        return direction
    else:
        print("Invalid direction")
        return ""

# Returns position and direction if PLACE command is valid, returns empty list otherwise
def validate_place_command(command):
    direction = validate_direction(command)
    if direction != "":
        x_position = validate_position(command, "x")
        if x_position != -1: # validate y position if x position is valid
            y_position = validate_position(command, "y")
            if y_position != -1: # if both x and y positions are valid
                return [x_position, y_position, direction]
            else:
                return []
        else:
            return []
    else:
        return []

if __name__ == "__main__":
    # initlialisations
    command = None
    first_command = True

    # main iteration
    while command != "QUIT":
        command = input("\nEnter a command: ")

        if first_command:
            if command[:len("PLACE")] == "PLACE":
                position_direction_list = validate_place_command(command)
                if len(position_direction_list) == 3: # if PLACE command is valid
                    x_position = position_direction_list[0]
                    y_position = position_direction_list[1]
                    direction = position_direction_list[2]
                    pacman = Pacman(x_position, y_position, direction)
                    first_command = False
                else:
                    print("Invalid PLACE command")
            elif command == "QUIT": # quit is still valid even if it's the first command
                break
            else:
                print("Invalid command. First command must be PLACE or QUIT")

        else: # if it's not the first command
            if command[:len("PLACE")] == "PLACE":
                position_direction_list = validate_place_command(command)
                if len(position_direction_list) == 3: # if PLACE command is valid
                    x_position = position_direction_list[0]
                    y_position = position_direction_list[1]
                    direction = position_direction_list[2]
                    pacman = Pacman(x_position, y_position, direction)
                else:
                    print("Invalid PLACE command")
            elif command == "MOVE":
                pacman.move()
            elif command == "LEFT":
                pacman.rotate_left()
            elif command == "RIGHT":
                pacman.rotate_right()
            elif command == "REPORT":
                pacman.report()
            elif command != "QUIT":
                print("Invalid command")
