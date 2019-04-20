import os
import pyfiglet
import sys
import getopt

banner = pyfiglet.figlet_format('git - dir')

# text colors
red = '\033[1;31;40m'
green = '\033[1;32;40m'
blue = '\033[1;36;40m'
white = '\033[1;37;40m'
end = '\033[0m'

# global args
opts= ''
args = ''
newTool = ''
removeTool = ''

# clear screen function
def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# help page
def usage():
    clearScreen()
    print(green, banner)
    print('{} __________________________________________________'.format(blue))
    print(' |                    {}Help Page{}                   |'.format(green, blue))
    print(' |                                                |')
    print(' |     {}-h{}           |   {}Display help page{}         |'.format(red, blue, green, blue))
    print(' |     {}-l{}           |   {}List tools{}                |'.format(red, blue, green, blue))
    print(' |     {}-d{}           |   {}Download tools{}            |'.format(red, blue, green, blue))
    print(' |     {}-u{}           |   {}Update all tools{}          |'.format(red, blue, green, blue))
    print(' |     {}--add={}       |   {}Add tool{}                  |'.format(red, blue, green, blue))
    print(' |     {}--remove={}    |   {}Remove tool{}               |'.format(red, blue, green, blue))
    print(' |     {}--directory={} |   {}Change download directory{} |'.format(red, blue, green, blue))
    print(' |                                                |')
    print(' | {}Examples:{}                                      |'.format(green, blue))
    print(' |    {}python repo-git.py {}-d{}                       |'.format(green, red, blue))
    print(' |    {}python repo-git {}--add{} github.com/usr/repo{}   |'.format(green, red, green, blue))
    print(' |________________________________________________|\n{}'.format(green))
    quit()

# lists github links in txt file.
def listRepo():
    clearScreen()
    print(green, banner)
    with open('git-links.txt', encoding = 'utf-8') as repo:
        for number, line in enumerate(repo, start=1):
            print(' {}[{}{}{}] {}{}{}'.format(blue, red, number, blue, green, line.strip('git clone '), end))


def addRepoLoop():
    loop = True
    while loop == True:
        loopTool = input(' {}Enter Github tool link or Q to quit: {}'.format(blue, white))

        if loopTool.lower() == 'q':
            loop = False
            quit
        else:
            with open("git-links.txt", "a") as linkFile:
                linkFile.write('\n{}'.format(loopTool))
                print('Link added succesfully.')
        addRepoLoop()


def addRepo():
    clearScreen()
    print(green, banner)
    addTool = newTool

    with open("git-links.txt", "a") as linkFile:
        linkFile.write('\n{}'.format(addTool))

    addInput = input('\n {}Add another tool? ({}Y{}/{}N{}): {}'.format(blue, green, blue, green, blue, end))
            
    if addInput.lower() == 'y':
        addRepoLoop()
    elif addInput.lower() == 'n':
        quit
    else:
        print('{}Invalid Argument.'.format(red))


def removeRepo():
    clearScreen()
    print(green, banner)
    #removeArg = input(' {}Under construction: {}'.format(blue, end))
    with open('git-links.txt', 'r+', encoding = 'utf-8') as repo:
        for line in repo:
            line = line.split('/')[-1]
            line = line.split('.')[0]
            if removeTool.lower() == line.lower():
                repo.write(line)
            repo.truncate()


def download():
    clearScreen()
    print(green, banner)

    with open("tool-directory.txt", "r") as dirFile:
        directory = dirFile.readline()

    with open("git-links.txt", "r") as links:
        for link in links:
            link = link.rstrip()
            toolName = link.split('/')[-1]
            toolName = toolName.split('.')[0]
            os.system('git clone {} {}/{}'.format(link, directory, toolName))


def update():
    clearScreen()
    print(green, banner)

    with open("tool-directory.txt", "r") as dirFile:
        directory = dirFile.readline()

    with open("git-links.txt", "r") as links:
        for link in links:
            link = link.rstrip()
            toolName = link.split('/')[-1]
            toolName = toolName.split('.')[0]
            os.system('rm -rf {}/{}'.format(directory, toolName))
            os.system('git clone {} {}/{}'.format(link, directory, toolName))

    

def main():
    global opts, args, newTool, removeTool
    clearScreen()

    try: 
        opts, args = getopt.getopt(sys.argv[1:], "hdula:r:d:", 
        ["help","download","update","list","add=","remove=","directory="])

    except getopt.GetoptError as err:
        print(str(err))
        usage()

    for o,a in opts:
        if o in ('-h','--help'):
            usage()
        elif o in ('-d','--download'):
            download()
        elif o in ('-u', '--update'):
            update()
        elif o in ('-l','--list'):
            listRepo()
        elif o in ('-a','--add'):
            newTool = str(a)
            addRepo()
        elif o in ('-r','--remove'):
            removeTool = str(a)
            removeRepo()

main()
