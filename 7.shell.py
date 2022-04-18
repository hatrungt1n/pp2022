import os
from colorama import Fore

def ls():
    # get current directory
    files = os.getcwd()
    getFiles = os.listdir(files)
    print('\t'.join(map(str, getFiles)))


def cat(cmd):
    fileName = cmd[1]
    with open(fileName, 'r')as f:
        data = f.read()
    print(data)


def cd(cmd):
    path = cmd[1]
    try:
        os.chdir(path)
        # print("Current working directory: {0}".format(os.getcwd()))
    except FileNotFoundError:
        print("Directory: {0} does not exist".format(path))
    except NotADirectoryError:
        print("{0} is not a directory".format(path))
    except PermissionError:
        print("You do not have permissions to change to {0}".format(path))


def touch(cmd):
    newFile = cmd[1]
    if os.path.exists(newFile): 
        print("File has already existed!")
    open(newFile, "w")

def remove(cmd):
    file = cmd[1]
    if (not os.path.exists(file)):
        print("The file does not exist")
    os.remove(file)


while True:
    directory = os.getcwd()
    command = input(Fore.RED + directory + ": ")
    cmd = command.split(" ")
    if (cmd[0] == "cat"):
        cat(cmd)
    elif cmd[0] == "ls":
        ls()
    elif cmd[0] == "cd":
        cd(cmd)
    elif cmd[0] == "touch":
        touch(cmd)
    elif cmd[0] == "rm":
        remove(cmd)