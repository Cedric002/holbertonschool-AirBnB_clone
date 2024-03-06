#!/usr/bin/python3
"""
First Console of AirBnb project
"""
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_create(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[args[0]]()
            print(new_instance.id)

    def do_show(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            print("** no instance found **")

    def do_all(self, arg):
        args = arg.split()
        if len(args) > 0 and args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            print("[]")

    def do_update(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            print("** no instance found **")

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