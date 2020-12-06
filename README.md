<img src="images/GitHub_Logo.png" />

# Github Automation for Windows

A github automation for my workflow inspired by [Kalle Halden video](https://www.youtube.com/watch?v=7Y8Ppin12r4) 

## Description

A small script to make the process of starting your projects faster. I made this for myself since
I use windows with git bash and the process of creating a project set was kinda boring after the 200 time,
So this is script is made with my way of starting a project, create the repo, readme, push to github BUT also
create a note file in markdown with a simple structure that I use to start my projects. If you get to like the way 
I do feel free to use the script :)

## Getting Started

### Dependencies
The dependencies are:
- python-dotenv
- PyGithub

but you can install it just by doing `pip install -r requirements.txt`

### Installing
Create an `.env` file and use this format in it:

```bash
LOGIN="your login"
TOKEN="your token"
PATH="path/to/put/project/folder"
NOTE_PATH="path/to/project/note/file"
```

IMPORTANT: you can get your token from https://github.com/settings/tokens . Just check the first box called "repo" and write something in the "Note" to generate it!

-----

Open `command.sh` and put the file path to index.py so the line will be `python file/path/index.py`.
You need to put the `command.sh` file in your `~`. Thi is usually in `C:\Users\<your name>` folder, but you can see exactly what folder is
by typing `echo ~` in yout git bash terminal. Inside this folder you will need to find a file called `.bash_profile`, open this file in any
text editor and put `source ~/.command.sh` in the final line.

### Executing
Now you can run the command from anywhere, the command is called `create` so just go to your terminal and put:

```bash
create amazingProjectName
```

### Authors
- [GMkonan](https://github.com/GMkonan)

### License

[MIT](https://github.com/GMkonan/githubAutomation/blob/master/LICENSE.md)

### Acknowledgments

- [Kalle Halden video](https://www.youtube.com/watch?v=7Y8Ppin12r4) 