<<<<<<< HEAD
import cmd

=======
#!/usr/bin/python3
"""
First Console of AirBnb project
"""
import cmd


>>>>>>> main
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
<<<<<<< HEAD
        """Quit the program."""
        print("Quitting the program.")
        return True

    def do_EOF(self, arg):
        """Handle EOF."""
        print("Exiting on EOF.")
        return True

    def emptyline(self):
        """Don't do anything for empty line."""
        pass

=======
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        pass


>>>>>>> main
if __name__ == '__main__':
    HBNBCommand().cmdloop()
