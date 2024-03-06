#!/usr/bin/python3
"""
First Console of AirBnb project
"""
import cmd
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
<<<<<<< HEAD
=======
from models.user import User

>>>>>>> main

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
        """
        Do nothing if empty line
        """
        pass

    def do_create(self, arg):
<<<<<<< HEAD
        """ 
=======
        """
>>>>>>> main
        Create a new instance of BaseModel
        """
        if not arg:
            print("** class name missing **")
        else:
<<<<<<< HEAD
            try :
=======
            try:
>>>>>>> main
                new_instance = eval(arg)()
            except NameError:
                print("** class doesn't exist **")
            else:
                new_instance.save()
                print("{}".format(new_instance.id))

    def do_show(self, arg):
        """
        Prints the string repr of an instance
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            try:
                class_instance = eval(class_name)
            except NameError:
                print("** class doesn't exist **")
                return
            if len(args) == 1:
                print("** instance id missing **")
            else:
                class_id = args[1]
                key = "{}.{}".format(class_name, class_id)
                instance = storage._FileStorage__objects.get(key)
                if instance:
                    print(instance)
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes instance
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
<<<<<<< HEAD
        if NameError:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            class_name = args[0]
            class_id = args[1]
            class_instances = storage.all().get(class_name)
            if class_instances is not None:
                key = "{}.{}".format(class_name, class_id)
                instance = class_instances.get(key)
                if instance:
                    del class_instances[key]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

=======
        else:
            class_name = args[0]
            try:
                class_instance = eval(class_name)
            except NameError:
                print("** class doesn't exist **")
                return
            if len(args) == 1:
                print("** instance id missing **")
            else:
                class_id = args[1]
                key = "{}.{}".format(class_name, class_id)
                class_instances = storage._FileStorage__objects.get(key)
                if class_instances:
                    del storage._FileStorage__objects[key]
                    storage.save()
                else:
                    print("** no instance found **")
>>>>>>> main

    def do_all(self, arg):
        """
        Print all string representation of all instances
        """
<<<<<<< HEAD
=======
        args = arg.split()
        if len(args) == 1:
            class_name = args[0]
            try:
                class_instance = eval(class_name)
            except NameError:
                print("** class doesn't exist **")
                return
            instances = storage.all().values()
            filtered_instances = [str(instance) for instance in instances
                                  if isinstance(instance, class_instance)]
            if filtered_instances:
                print(filtered_instances)
            else:
                print("** no instance found **")
        else:
            instances = storage.all().values()
            print([str(instance) for instance in instances])
>>>>>>> main

    def do_update(self, arg):
        """
        Update instances
        """
<<<<<<< HEAD
=======
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        try:
            class_instance = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        else:
            class_id = args[1]
            key = "{}.{}".format(class_name, class_id)
            instance = storage._FileStorage__objects.get(key)
            if instance is None:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attr_name = args[2]
            attr_value = args[3]
            if attr_name in ["id", "created_at", "updated_at"]:
                return
            try:
                attr_value = eval(attr_value)
            except (NameError,  SyntaxError):
                pass
            setattr(instance, attr_name, attr_value)
            instance.save()

>>>>>>> main

if __name__ == '__main__':
    HBNBCommand().cmdloop()
