import subprocess
import os
import sys
from github import Github
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")
login = os.getenv("LOGIN")

#https://github.com/settings/tokens
def create_repo(folder_name):
    Github(token).get_user().create_repo(folder_name)

folder_name = str(sys.argv[1])

Remote = f"git@github.com:{login}/{folder_name}.git"

def automate():
    os.chdir('D:/Documentos/Projetos')
    os.system(f"mkdir {folder_name}")
    os.chdir(f"./{folder_name}")
    os.system("git init")
    os.system("touch README.md")
    os.system("git add .")
    os.system(f'git commit -m "First commit for {folder_name}"')
    create_repo(folder_name)
    os.system(f"git remote add origin {Remote}")
    os.system("git push origin master")

if __name__ == "__main__":
    automate()