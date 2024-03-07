#!/usr/bin/python3
"""
First Console of AirBnb project
"""
import cmd
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage, State, City, Amenity, Place, Review

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
        """ 
        Create a new instance of BaseModel
        """
        if not arg:
            print("** class name missing **")
        else:
            try :
                new_instance = eval(arg)()
            except NameError:
                print("** class doesn't exist **")
            else:
                new_instance.save()
                print("{}".format(new_instance.id))

    def do_show(self, arg):
        """Prints the string repr of an instance"""
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


    def do_all(self, arg):
        """
        Print all string representation of all instances
        """

    def do_update(self, line):
        """Update instance"""
        args = line.split()
        if len(args) < 4:
            print("Incorrect number of arguments.")
            return

        class_name, id, attr_name, attr_value = args[0],
        args[1], args[2], args[3]

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in self.instances:
            print("** class doesn't exist **")
            return

        if not id:
            print("** instance id missing **")
            return
        
    def create_state():
        name = input("Enter state name: ")
        state = State(name=name)
        storage.new(state)
        state.save()
    
    def show_states():
        states = storage.all().values()
        for state in states:
            if isinstance(state, State):
                print(state)

    def create_city():
        name = input("Enter city name: ")
        state_id = input("Enter state ID: ")
        city = City(name=name, state_id=state_id)
        storage.new(city)
        city.save()

    def show_cities():
        cities = storage.all(City).values()
        for city in cities:
            print(city)
    
    def create_amenity():
        description = input("Enter amenity description: ")
        amenity = Amenity(description=description)
        storage.new(amenity)
        amenity.save()

    def show_amenities():
        amenities = storage.all(Amenity).values()
        for amenity in amenities:
            print(amenity)

    def create_place():
        name = input("Enter place name: ")
        city_id = input("Enter city ID: ")
        user_id = input("Enter user ID: ")
        place = Place(name=name, city_id=city_id, user_id=user_id)
        storage.new(place)
        place.save()

    def show_places():
        places = storage.all(Place).values()
        for place in places:
            print(place)

    def create_review():
        text = input("Enter review text: ")
        user_id = input("Enter user ID: ")
        place_id = input("Enter place ID: ")
        review = Review(text=text, user_id=user_id, place_id=place_id)
        storage.new(review)
        review.save()

    def show_reviews():
        reviews = storage.all(Review).values()
        for review in reviews:
            print(review)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
