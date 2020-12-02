import subprocess
import os
import sys
from github import Github
from dotenv import load_dotenv

load_dotenv()

def create_repo(folder_name):
    token = os.getenv("TOKEN")
    Github(token).get_user().create_repo(folder_name)

def create_note(folder_name):
    note_path = os.getenv("NOTE_PATH")
    
    os.chdir(note_path) #the "with" will guarantee the file will be closed :)
    with open(f"{folder_name}.md", "w") as f:
        f.writelines(f"# {folder_name}\n## Todo:\n - [ ] \n## Resources:\n- \n")

def automate():
    
    file_path = os.getenv("FILE_PATH")
    login = os.getenv("LOGIN")

    folder_name = str(sys.argv[1])
    Remote = f"git@github.com:{login}/{folder_name}.git"

    create_note(folder_name)
    os.chdir(file_path)
    os.system(f"mkdir {folder_name}")
    os.chdir(f"./{folder_name}")
    os.system("git init")
    os.system("touch README.md")
    os.system(f'echo # {folder_name} >> README.md')
    os.system("git add .")
    os.system(f'git commit -m "First commit for {folder_name}"')
    create_repo(folder_name)
    os.system(f"git remote add origin {Remote}")
    os.system("git push origin master")
    os.system("code .")

if __name__ == "__main__":
    automate()