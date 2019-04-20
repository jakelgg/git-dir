
#  git-dir

  

A tool made to manage the downloads and updates of Github tools. It uses a set directory to locate and install tools that aren't already downloaded.

  

##  Features

  

* Add and remove tools from repository.

* Download tools that aren't installed already.

* Update all tools by uninstalling version on host machine and downloading the new version.

  

##  Getting Started

  

This tools currently works in Linux but will be working to get Windows support.

###  Prerequisites

  

Ensure you have git downloaded before running the program. This tool only uses one module that is not in the Python standard library called Pyfiglet. Install it with the following command.

  

```

pip install pyfiglet or pip3 install pyfiglet

```

  

##  Using the tool

  

This tool uses arguments to identify the functions you want to run. Don't forget you can always use -h to get to the help page and -l to get a list of tools you have in your repository.

  

```

python git-dir.py -h or python git-dir.py -l

```

  

###  Adding and removing tools

  

To add tools to your repo use the --add= argument then enter the link to to Github page.
  

```

python git-dir.py --add=https://github.com/user/repo

```

  

###  Downloading tools

  

This function will only download the tools that aren't already in the directory path you set.

  

```

python git-dir.py -d

```
### Updating tools

The update function will remove all the tools in the repo list and reinstall the updated version of all tools. Working on a way to only update tools that have actually been updated.

```
python git-dir.py -u
```

  

##  License

  

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
