#!/usr/bin/python3
"""commenttttttttttttttttttttttttttttttttttt"""
import cmd
import json
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """commenttttttttttttttttttttttttttttttttttt"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """commenttttttttttttttttttttttttttttttttttt"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """commenttttttttttttttttttttttttttttttttttt"""
        pass

    def do_create(self, line):
        """commenttttttttttttttttttttttttttttttttttt"""
        if line in storage.classes:
            myc = storage.classes[line]()
            myc.save()
            print(myc.id)
        elif line == "" or line is None:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """commenttttttttttttttttttttttttttttttttttt"""
        tok = line.split()
        if len(tok) == 0:
            print("** class name missing **")
            return
        if tok[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(tok) == 1:
            print("** instance id missing **")
            return
        myshow = "{}.{}".format(tok[0], tok[1])
        if myshow not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[myshow])

    def do_destroy(self, line):
        """commenttttttttttttttttttttttttttttttttttt"""
        tok = line.split()
        if len(tok) == 0:
            print("** class name missing **")
            return
        if tok[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(tok) == 1:
            print("** instance id missing **")
            return
        mydestroy = "{}.{}".format(tok[0], tok[1])
        if mydestroy not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[mydestroy]
            storage.save()

    def do_all(self):
        """commenttttttttttttttttttttttttttttttttttt"""
        pass

    def do_update(self):
        """commenttttttttttttttttttttttttttttttttttt"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
