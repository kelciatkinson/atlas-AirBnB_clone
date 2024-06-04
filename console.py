#!/usr/bin/python3
"""This module defines a simple command-line interface using the cmd module.
Commands available:
 - create: Creates a new instance of BaseModel, prints id.
 - help: Provides help information for commands.
 - quit: Exits the program.
 - EOF: Exits the program."""
import cmd
from models.base_model import BaseModel
from models.user import User
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
            print("Documented commands(type help <topic>):\n"
                  "========================================\n"
                  "EOF  help  quit")

    def do_create(self, line):
        """This method creates a new instance of BaseModel and saves it to
        the JSON file, then prints the ID."""
        if not line:
            print("** class name missing **")
            return

        cls = line.split()[0]

        if cls not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return

        if cls == "BaseModel":
            instance = BaseModel()
        elif cls == "User":
            instance = User()

        instance.save()
        print(instance.id)

    def do_show(self, arg):

        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        cls = arg.split()[0]
        if cls not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_all(self, line):
        list_inst = []
        if line:

            cls = line.split()[0]

            if cls not in ["BaseModel", "User"]:
                print("** class doesn't exist **")
                return

            for key, obj in storage.all().items():
                if key:
                    list_inst.append(str(obj))
        else:
            for obj in storage.all().values():
                list_inst.append(str(obj))
        print(list_inst)

    def do_destroy(self, line):
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        cls = args[0]

        if cls not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_update(self, line):
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        cls = args[0]

        if cls not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        object = storage.all()[key]
        setattr(object, args[2], args[3])
        object.save()

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
