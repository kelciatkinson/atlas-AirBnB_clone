#!/usr/bin/python3
"""This module defines a simple command-line interface using the cmd module.
Commands available:
 - help: Provides help information for commands.
 - exit: Exits the program
 - EOF: Exits the program"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_hbnh(self, line):
        print("hello")

    def do_help(self, arg):
        if arg:
            try:
                func = getattr(self, "help_" + arg)
            except AttributeError:
                return
            func()
        else:
            commands = {"quit": "Quit command to exit the program",
                        "EOF": "EOF command to exit the program",
                        "help": "Help command"}

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True


if __name__ == "__main__":

    HBNBCommand().cmdloop()
