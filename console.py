#!/usr/bin/python3

"""command interpreter"""


import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand: contains the entry
    point of the command interpreter"""

    prompt = '(hbnb) '

    list_className = {
            "BaseModel": BaseModel, "User": User,
            "State": State, "City": City,
            "Amenity": Amenity, "Place": Place,
            "Review": Review}

    def do_create(self, arg):
        """Creates a new instance of BaseModel
        and print its\n"""
        if (arg):
            if arg in self.list_className:
                my_model = self.list_className[arg]()
                my_model.save()
                print(my_model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Prints the string representation of an instance
        base on the class name and id\n"""
        if arg:
            arg = arg.split()
            if arg[0] not in self.list_className:
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id missing **")
            else:
                compare = arg[0] + "." + arg[1]
                for key, obj in storage.all().items():
                    if key == compare:
                        print(obj)
                        return
                print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the
        class name and id\n"""
        if arg:
            arg = arg.split()
            if arg[0] not in self.list_className:
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id missing **")
            else:
                compare = arg[0] + "." + arg[1]
                for key in storage.all().keys():
                    if key == compare:
                        del storage.all()[key]
                        storage.save()
                        return
                print("** no instance found **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name\n"""
        if arg:
            arg = arg.split()
            if arg[0] not in self.list_className:
                print("** class doesn't exist **")
            else:
                my_list = []
                for key, obj in storage.all().items():
                    if obj.__class__.__name__ == arg[0]:
                        my_list.append(obj.__str__())
                print(my_list)
        else:
            my_list = []
            for key, obj in storage.all().items():
                my_list.append(obj.__str__())
            print(my_list)

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute\n"""
        if arg:
            arg = arg.split()
            if arg[0] not in self.list_className:
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id missing **")
            elif len(arg) == 3:
                print("** value missing **")
            else:
                compare = arg[0] + "." + arg[1]
                for key, obj in storage.all().items():
                    if key == compare:
                        new_value = arg[3].strip('"')
                        setattr(obj, arg[2], new_value)
                        storage.save()
                        return
                print("** no instance found **")
        else:
            print("** class name missing **")

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
