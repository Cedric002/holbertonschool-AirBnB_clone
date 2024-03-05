#!/usr/bin/python3
"""
First Console of AirBnb project
"""
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Do nothing if empty line
        """
        pass

    def do_create(self, arg):
        """ Create a new instance of BaseModel
        """
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print("{}".format(new_instance.id))
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string repr of an instance
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            class_name = args[0]
            class_id = args[1]
            try:
                key = "{}.{}".format(class_name, class_id)
                instance = storage._FileStorage__objects.get(key)
                if instance:
                    print(instance)
                else:
                    print("** no instance found **")
            except Exception as e:
                print(e)

    def do_all(self, arg):
        """
        Print all string representation of all instances
        """

    def do_destroy(self, arg):
        """
        Deletes instance
        """

    def do_update(self, arg):
        """
        Update instances
        """

if __name__ == '__main__':
    HBNBCommand().cmdloop()
