#!/usr/bin/python3
# console same shell

import cmd, sys


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand: contains the entry point of the command interpreter"""
    intro = 'Welcome to the shell.   Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    # ----- basic HBNB commands -----
    def do_quit(self, arg):
        'Quit command to exit the program\n'
        return True

    def do_EOF(self, arg):
        'Quit command to exit the program\n'
        return True

    # ----- builtin HBNB commands -----
    def precmd(self, arg):
        arg = arg.lower()
        return arg

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
