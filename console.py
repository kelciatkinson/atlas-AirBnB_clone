#!/usr/bin/python3
"""This module defines a simple command-line interface using the cmd module.
Commands available:
 - help: Provides help information for commands.
 - quit: Exits the program
 - EOF: Exits the program"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

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
            command = ["EOF", "help", "quit"]
            print("Documented commands(type help <topic>):\n"
                  "========================================\n"
                  "EOF  help  quit")

    def help_quit(self):
        print("Quit command to exit the program")

    def do_quit(self, line):
        return True

    def help_EOF(self, line):
        print("EOF command to exit the program")

    def do_EOF(self, line):
        return True

    def emptyline(self):
        return


if __name__ == "__main__":

    HBNBCommand().cmdloop()
