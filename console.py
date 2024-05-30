#!/usr/bin/python3
import cmd

class Console(cmd.Cmd):
    def do_greet(self, line):
        print("hello")

    def do_exit(self, line):
        return True

if __name__ == "__main__":
    Console().cmdloop()
