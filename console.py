import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) ' # Custom prompt

    def quit(self, arg):
        """Quit the program."""
        print("Quitting the program.")
        return True # Returning True exits the cmdloop

    def EOF(self, arg):
        """Handle EOF."""
        print("Exiting on EOF.")
        return True # Returning True exits the cmdloop

    def emptyline(self):
        """Don't do anything for empty line."""
        pass

    def help(self):
        """Custom help command."""
        print("This is a custom help message.")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
