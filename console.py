#!/usr/bin/python3
"""This module defines a simple command-line interface using the cmd module.
Commands available:
 - create: Creates a new instance of BaseModel, prints id.
 - help: Provides help information for commands.
 - quit: Exits the program.
 - EOF: Exits the program."""
import cmd
from models.base_model import BaseModel


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

    def do_create(self, cls):
        if not cls:
            print("** class name missing **")
            return

        if cls != "BaseModel":
            print("** class doesn't exit **")
            return

        instance = BaseModel()
        # still need to write!!!
        # save to JSON file
        print(instance.id)

    def do_show(self, arg):
        args = arg.split()
        
        if not args:
            print("** class name missing **")
            return

        cls = args[0]
        if cls != "BaseModel":
            print("** class doesn't exit **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        with open("{}.json".format(cls.__name__), "r") as file:
            json_string = file.read()
                
                    



        

    def help_quit(self, line):
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
