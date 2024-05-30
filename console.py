#!/usr/bin/python3
import cmd

class Console(cmd.Cmd):
    def do_greet(self, line):
        print("hello")

    def do_exit(self, line):
        return True

    def do_printLine(self, line):
if __name__ == "__main__":
    Console().cmdloop()
