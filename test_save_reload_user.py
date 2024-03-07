#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = City()
my_user2.state_id = "John"
my_user2.save()
print(my_user2)

print("-- Create a new Place --")
my_place = Place()
my_place.city_id = "Toulouse"
my_place.amenity_ids = "airbnb2@mail.com"
my_place.description = "root"
my_place.save()
print(my_place)