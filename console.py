#!/usr/bin/python3
"""This module defines a simple command-line interface using the cmd module.
Commands available:
 - create: Creates a new instance of BaseModel, prints id.
 - help: Provides help information for commands.
 - quit: Exits the program.
 - EOF: Exits the program."""
import cmd
from models.base_model import BaseModel
from models import storage


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
        """This method creates a new instance of BaseModel and saves it to
        the JSON file, then prints the ID."""
        if not cls:
            print("** class name missing **")
            return

        name = cls.split()[0]

        if name != "BaseModel":
            print("** class doesn't exist **")
            return

        instance = BaseModel()
        instance.save()
        print(instance.id)

    def do_show(self, arg):

        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] != "BaseModel":
            print("** class doesn't exit **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        print(storage.all()[key])

    def do_all(self, line):
        list_inst = []
        if line:

            args = line.split()

            if args[0] != "BaseModel":
                print("** class doesn't exist **")
                return

            for key, obj in storage.all().items():
                if key:
                    list_inst.append(str(obj))
        else:
            for obj in storage.all().values():
                list_inst.append(str(obj))
        print(list_inst)

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
