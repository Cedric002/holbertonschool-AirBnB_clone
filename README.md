# Holberton School AirBnB clone project

## Description

This is an implementation of a command line interpreter coded in `Python` in order to interact with differents classes and saves them. The idea is to create instances and manage them for futures usage on the AirBnb clone website. We store every datas, update them and, if needed, delete them. It's a back-end tool to work on users. The storage is handled with a JSON interpreter. To start it, you only need to open a terminal and write `./console.py`.

## :file_folder: Files

- `console.py`: Command line interpreter to interact with storage.
- `base_model.py`: The parent class to initialize instances.
- `__init__.py`: Create global variable "storage", an instance of FileStorage.
- `file_storage.py`: Serialize instances to a JSON file and deserialize this file.
- `user.py`: New class for futur user.
- `amenity.py`: Subclass for futur user.
- `city.py`: Subclass for futur user.
- `place.py`: Subclass for futur user.
- `review.py`: Subclass for futur user.

- `test_*.py`: All files are tested with unittests.

## Functions and modules used

### Modules imported

- cmd
- uuid
- datetime
- unittest

### Functions (not exhaustive)

`do_help`, `do_EOF`, `do_create`, `do_show`, `do_destroy`, `do_all`, `do_update`, `save`, `__str__`, `to_dict`...

Environment
:--------------------------------------------------: |
Language: Python3
OS: Ubuntu 20.04 LTS
Style guidelines: Pycodestyle

## Usage

To use the custom command line interpreter, just run the `./console.py` executable. It directly open the "cmd". When can use the `help` command to look at all availables commands. Then, you can create instances, save them, update them or destroy them. One detail, you need to use the ID associated to the instance to work on them. Every created instance is saved in a JSON file `file.json`The command line interpreter also work in non-interactive mode.

```python
./console.py
(hbnb)
```

### :floppy_disk: Examples

Display the list of available commands:
```
./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```
----------
Create a new instance `BaseModel` and display the id associated :
```
./console.py 
(hbnb) create BaseModel
58bb80cd-f543-4211-9dad-88937aeea3f0
(hbnb) 
```
----------
Display the new `BaseModel` instance attributes :
```
./console.py 
(hbnb) create BaseModel
58bb80cd-f543-4211-9dad-88937aeea3f0
(hbnb) show BaseModel 58bb80cd-f543-4211-9dad-88937aeea3f0
[BaseModel] (58bb80cd-f543-4211-9dad-88937aeea3f0) {'id': '58bb80cd-f543-4211-9dad-88937aeea3f0', 'created_at': datetime.datetime(2024, 3, 7, 14, 47, 6, 148370), 'updated_at': datetime.datetime(2024, 3, 7, 14, 47, 6, 148480)}
(hbnb) 
```
----------
Delete the `BaseModel`instance:
```
./console.py 
(hbnb) create BaseModel
58bb80cd-f543-4211-9dad-88937aeea3f0
(hbnb) show BaseModel 58bb80cd-f543-4211-9dad-88937aeea3f0
[BaseModel] (58bb80cd-f543-4211-9dad-88937aeea3f0) {'id': '58bb80cd-f543-4211-9dad-88937aeea3f0', 'created_at': datetime.datetime(2024, 3, 7, 14, 47, 6, 148370), 'updated_at': datetime.datetime(2024, 3, 7, 14, 47, 6, 148480)}
(hbnb) destroy BaseModel 58bb80cd-f543-4211-9dad-88937aeea3f0
(hbnb) show BaseModel 58bb80cd-f543-4211-9dad-88937aeea3f0
** no instance found **
(hbnb) 
```
----------

## Authors

- Cédric Guerin
- Nathan Raynal
