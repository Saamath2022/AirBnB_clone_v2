#!/usr/bin/env python3

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if arg == "BaseModel":
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show an instance based on the class name and id"""
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            instance_id = f"BaseModel.{args[1]}"
            if instance_id in storage.all():
                print(storage.all()[instance_id])
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

