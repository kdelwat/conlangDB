import cmd
import argparse
from Interface import *


class Lexeme(cmd.Cmd):
    intro = "Welcome to Lexeme! Input '?' for help and commands."
    prompt = "\nEnter command: "

    def getHelp(self, command):
        with open("help.txt", "r") as f:
            line = f.readline().rstrip()
            while line != command:
                line = f.readline().rstrip()
            f.readline()
            while line != "====":
                print(line)
                line = f.readline().rstrip()

    def do_list(self, arg):
        clearScreen()
        listwords()

    def help_list(self):
        clearScreen()
        self.getHelp("LIST")

    def do_quit(self, arg):
        quit()

    def help_quit(self):
        clearScreen()
        self.getHelp("QUIT")

    def do_add(self, arg):
        clearScreen()
        add()

    def help_add(self):
        clearScreen()
        self.getHelp("ADD")

    def do_decline(self, arg):
        clearScreen()
        decline()

    def help_decline(self):
        clearScreen()
        self.getHelp("DECLINE")

    def do_modify(self, arg):
        clearScreen()
        modify()

    def help_modify(self):
        clearScreen()
        self.getHelp("MODIFY")

    def do_statistics(self, arg):
        clearScreen()
        statistics()

    def help_statistics(self):
        clearScreen()
        self.getHelp("STATISTICS")

    def do_search(self, arg):
        clearScreen()
        search()

    def help_search(self):
        clearScreen()
        self.getHelp("SEARCH")

    def do_generate(self, arg):
        clearScreen()
        generate()

    def help_generate(self, arg):
        clearScreen()
        self.getHelp("GENERATE")

    def do_export(self, arg):
        clearScreen()
        export()

    def help_export(self, arg):
        clearScreen()
        self.getHelp("EXPORT")

    def do_exportwords(self, arg):
        clearScreen()
        exportText()

    def help_exportwords(self):
        clearScreen()
        self.getHelp("EXPORTWORDS")

    def do_batch(self, arg):
        clearScreen()
        batchgenerate()

    def help_batch(self):
        clearScreen()
        self.getHelp("BATCH")

    def do_import(self, arg):
        clearScreen()
        importWords()

    def help_import(self):
        clearScreen()
        self.getHelp("IMPORT")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--database", help="set database file")
    parser.add_argument("--config", help="set configuration file")
    args = parser.parse_args()

    if args.database is not None:
        Library.loadDatabase(args.database)

    else:
        Library.loadDatabase()

    if args.config is not None:
        loadData(args.config)
    else:
        loadData()

    clearScreen()

    Lexeme().cmdloop()
