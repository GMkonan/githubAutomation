import os
import sys
from github import Github
from dotenv import load_dotenv


load_dotenv()

def createRepo(folder_name):
    token = os.getenv("TOKEN")
    if len(sys.argv) == 3:
        if sys.argv[2] == "p":
            print("Creating Private repository...")
            Github(token).get_user().create_repo(folder_name, private=True)
    else:
        #use github token from .env file to get the user and create the repo
        Github(token).get_user().create_repo(folder_name)

def create_note(folder_name):
    note_path = os.getenv("NOTE_PATH")
    
    #change to path specified in the .env file
    os.chdir(note_path) 
    
    #the "with" will guarantee the file will be closed :)
    # the "w" writes to file but if it already exists, doesnt create
    with open(f"{folder_name}.md", "w") as f:
        f.writelines(f"# {folder_name}\n## Todo:\n - [ ] \n## Resources:\n- \n")

def automate():
    
    file_path = os.getenv("FILE_PATH")
    login = os.getenv("LOGIN")

    #gets folder name from second argument passed in command
    folder_name = str(sys.argv[1])
    Remote = f"git@github.com:{login}/{folder_name}.git"

    #create my structured note file
    create_note(folder_name)
    #creates and starts git folder
    os.chdir(file_path)
    path = os.path.join(file_path, folder_name)
    os.makedirs(path, exist_ok=True)
    os.chdir(f"{file_path}/{folder_name}")
    os.system("git init")

    #creates readme
    with open("README.md", "w") as f:
        f.writelines(f"# {folder_name}\n\n## Description\n\n## Getting Started\n\n ### Authors\n - [GMkonan](https://github.com/GMkonan)\n### License")
    
    #creates repo, commits and push to master
    os.system("git add .")
    os.system(f'git commit -m "First commit for {folder_name}"')
    createRepo(folder_name)
    os.system(f"git remote add origin {Remote}")
    os.system("git push origin master")
    #finally open editor and lets code :)
    os.system("code .")

if __name__ == "__main__":
    automate()