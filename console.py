#!/usr/bin/python3
"""commenttttttttttttttttttttttttttttttttttt"""
import cmd


class HBNBCommand(cmd.Cmd):
    """commenttttttttttttttttttttttttttttttttttt"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """commenttttttttttttttttttttttttttttttttttt"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """commenttttttttttttttttttttttttttttttttttt"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
