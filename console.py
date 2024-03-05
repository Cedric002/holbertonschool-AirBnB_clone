#!/usr/bin/python3
"""
First Console of AirBnb project
"""
import cmd
from storage import Storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    storage = Storage()

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it and print the id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]
            """Assuming you have a way to check if the class exists"""
            if not self.storage.class_exists(class_name):
                print("** class doesn't exist **")
            else:
                """Create a new instance and save it"""
                instance = self.storage.create(class_name)
                print(f"{instance.id}")

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Don't do anything for empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()