import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
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

    def do_help(self):
        """Custom help command."""
        print("This is a custom help message.")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
