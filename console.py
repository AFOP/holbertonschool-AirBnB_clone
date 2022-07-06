#!/usr/bin/python3
# console same to shell

import cmd, sys
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand: contains the entry point of the command interpreter"""
    intro = 'Welcome to the shell.   Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    # ----- basic HBNB commands -----
    def do_create(self, arg):
        """Creates a new instance of BaseModel and print its\n"""
        if not (arg):
            print("** class name missing **")
        elif arg != 'BaseModel':
            print("** class doesn't exist **")
        else:
            my_model = BaseModel()
            my_model.save()
            print(my_model.id)
            
    def do_show(self, arg):
        """Prints the string representation of an instance base on the class name and id\n"""
        if arg:
            arg = arg.split()
            if arg[0] != 'BaseModel':
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
        """Deletes an instance based on the class name and id\n"""
        if arg:
            arg = arg.split()
            if arg[0] != 'BaseModel':
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id missing **")
            else:
                compare = arg[0] + "." + arg[1] 
                for key, obj in storage.all().items():
                    if key == compare:
                        del storage.all()[key]
                        storage.save()
                        return
                print("** no instance found **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name\n"""
        if arg:
            arg = arg.split()
            if arg[0] != 'BaseModel':
                print("** class doesn't exist **")
            else:
                print("[\"{}\"]".format(str(storage.all())))
        else:
            print("[\"{}\"]".format(str(storage.all())))

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute\n"""
        if arg:
            arg = arg.split()
            if arg[0] != 'BaseModel':
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id missing **")
            else:
                compare = arg[0] + "." + arg[1]
                print(type(storage.all())) 
                for key, obj in storage.all().items():
                    if key == compare:
                        storage.all()[arg[2]] = arg[3].strip('"') 
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

    # ----- builtin HBNB commands -----
    def emptyline(self):
        pass

def parse(arg):
    """return arg parse"""
    return arg.split()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
