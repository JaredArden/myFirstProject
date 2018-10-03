import unittest
import pacman_simulator
from pacman_simulator import Pacman

class TestPacmanSimulator(unittest.TestCase):
    def test_validate_position(self):
        # Test case 1: valid x position
        command = "PLACE 0,0,NORTH"
        result = pacman_simulator.validate_position(command, 'x')
        self.assertEqual(result, 0)

        # Test case 2: invalid x position > 4
        command = "PLACE 5,0,NORTH"
        result = pacman_simulator.validate_position(command, 'x')
        self.assertEqual(result, -1)

        # Test case 3: invalid x position < 0
        command = "PLACE -2,0,NORTH"
        result = pacman_simulator.validate_position(command, 'x')
        self.assertEqual(result, -1)

        # Test case 4: valid y position
        command = "PLACE 0,0,NORTH"
        result = pacman_simulator.validate_position(command, 'y')
        self.assertEqual(result, 0)

        # Test case 5: invalid y position > 4
        command = "PLACE 0,5,NORTH"
        result = pacman_simulator.validate_position(command, 'y')
        self.assertEqual(result, -1)

        # Test case 6: invalid y position < 0
        command = "PLACE 0,-2,NORTH"
        result = pacman_simulator.validate_position(command, 'y')
        self.assertEqual(result, -1)

        # Test case 7: empty string as a command
        command = ""
        result = pacman_simulator.validate_position(command, 'y')
        self.assertEqual(result, -1)

        # Test case 8: invalid command
        command = "INVALID COMMAND"
        result = pacman_simulator.validate_position(command, 'y')
        self.assertEqual(result, -1)

    def test_validate_direction(self):
        # Test case 1: valid direction
        command = "PLACE 0,0,NORTH"
        result = pacman_simulator.validate_direction(command)
        self.assertEqual(result, "NORTH")

        # Test case 2: invalid direction
        command = "PLACE 0,0,NORTHEAST"
        result = pacman_simulator.validate_direction(command)
        self.assertEqual(result, "")

        # Test case 3: empty command
        command = ""
        result = pacman_simulator.validate_direction(command)
        self.assertEqual(result, "")

        # Test case 4: invalid command
        command = "INVALID COMMAND"
        result = pacman_simulator.validate_direction(command)
        self.assertEqual(result, "")
        
    def test_validate_place_command(self):
        # Test case 1: valid place command
        command = "PLACE 0,0,NORTH"
        result = pacman_simulator.validate_place_command(command)
        self.assertEqual(result, [0, 0, "NORTH"])

        # Test case 2: invalid x position
        command = "PLACE 5,0,NORTH"
        result = pacman_simulator.validate_place_command(command)
        self.assertEqual(result, [])

        # Test case 3: invalid x position
        command = "PLACE 5,0,NORTH"
        result = pacman_simulator.validate_place_command(command)
        self.assertEqual(result, [])

        # Test case 4: invalid y position
        command = "PLACE 0,5,NORTH"
        result = pacman_simulator.validate_place_command(command)
        self.assertEqual(result, [])

        # Test case 5: invalid direction
        command = "PLACE 0,0,NORTHEAST"
        result = pacman_simulator.validate_place_command(command)
        self.assertEqual(result, [])

        # Test case 6: empty command
        command = ""
        result = pacman_simulator.validate_place_command(command)
        self.assertEqual(result, [])

        # Test case 7: invalid command
        command = "INVALID COMMAND"
        result = pacman_simulator.validate_place_command(command)
        self.assertEqual(result, [])

        # Test case 8: negative x position
        command = "PLACE -2,0,NORTH"
        result = pacman_simulator.validate_place_command(command)
        self.assertEqual(result, [])

        # Test case 9: negative y position
        command = "PLACE 0,-3,NORTH"
        result = pacman_simulator.validate_place_command(command)
        self.assertEqual(result, [])

    def test_move(self):
        # Test case 1: valid east movement
        pacman = Pacman(0,0,"EAST")
        pacman.move()
        x = pacman.x
        y = pacman.y
        direction = pacman.direction
        self.assertEqual([x, y, direction], [1, 0, "EAST"])

        # Test case 2: invalid east movement
        pacman = Pacman(4,0,"EAST")
        pacman.move()
        x = pacman.x
        y = pacman.y
        direction = pacman.direction
        self.assertEqual([x, y, direction], [4, 0, "EAST"])

        # Test case 3: valid west movement
        pacman = Pacman(4,0,"WEST")
        pacman.move()
        x = pacman.x
        y = pacman.y
        direction = pacman.direction
        self.assertEqual([x, y, direction], [3, 0, "WEST"])

        # Test case 4: invalid west movement
        pacman = Pacman(0,0,"WEST")
        pacman.move()
        x = pacman.x
        y = pacman.y
        direction = pacman.direction
        self.assertEqual([x, y, direction], [0, 0, "WEST"])

        # Test case 5: valid north movement
        pacman = Pacman(0,0,"NORTH")
        pacman.move()
        x = pacman.x
        y = pacman.y
        direction = pacman.direction
        self.assertEqual([x, y, direction], [0, 1, "NORTH"])

        # Test case 6: invalid north movement
        pacman = Pacman(0,4,"NORTH")
        pacman.move()
        x = pacman.x
        y = pacman.y
        direction = pacman.direction
        self.assertEqual([x, y, direction], [0, 4, "NORTH"])

        # Test case 7: valid south movement
        pacman = Pacman(0,4,"SOUTH")
        pacman.move()
        x = pacman.x
        y = pacman.y
        direction = pacman.direction
        self.assertEqual([x, y, direction], [0, 3, "SOUTH"])

        # Test case 8: invalid south movement
        pacman = Pacman(0,0,"SOUTH")
        pacman.move()
        x = pacman.x
        y = pacman.y
        direction = pacman.direction
        self.assertEqual([x, y, direction], [0, 0, "SOUTH"])

    def test_rotate_left(self):
        pacman = Pacman(0,0,"NORTH")

        pacman.rotate_left()
        direction = pacman.direction
        self.assertEqual(direction, "WEST")

        pacman.rotate_left()
        direction = pacman.direction
        self.assertEqual(direction, "SOUTH")

        pacman.rotate_left()
        direction = pacman.direction
        self.assertEqual(direction, "EAST")

        pacman.rotate_left()
        direction = pacman.direction
        self.assertEqual(direction, "NORTH")

    def test_rotate_right(self):
        pacman = Pacman(0,0,"NORTH")

        pacman.rotate_right()
        direction = pacman.direction
        self.assertEqual(direction, "EAST")

        pacman.rotate_right()
        direction = pacman.direction
        self.assertEqual(direction, "SOUTH")

        pacman.rotate_right()
        direction = pacman.direction
        self.assertEqual(direction, "WEST")

        pacman.rotate_right()
        direction = pacman.direction
        self.assertEqual(direction, "NORTH")

         
if __name__ == "__main__":
    unittest.main()
