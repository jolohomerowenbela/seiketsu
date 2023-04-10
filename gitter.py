import git
import os
import datetime
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

def commit(repo: git.Repo):
    branch_name = ""
    if repo.active_branch.name == "main":
        branch_name = "branch_" + str(datetime.datetime.now()).replace(" ", "").replace("-", ".").replace(":", ".")
        repo.git.switch("-c", branch_name)
    else:
        branch_name = repo.active_branch.name
    repo.git.add(".")
    repo.git.commit("-m", input("What changes have you done? (kahit ilang words lang) "))
    repo.git.push("-u", "origin", branch_name)
    
if __name__ == '__main__':
    dirPath = os.getcwd()
    
    key = rsa.generate_private_key(backend=default_backend(), public_exponent=65537, key_size=2048)
    public_key = key.public_key().public_bytes(serialization.Encoding.OpenSSH, serialization.PublicFormat.OpenSSH)
    print(f"\n\n\nTHE KEY IS: \n{public_key.decode('utf-8')}\n\n\n")
    
    repo = git.Repo.init(dirPath)

    reader = repo.config_reader()

    email = reader.get_value("user","email")
    name = reader.get_value("user", "name")
    
    if email == "" or email == None:
        email = input("Ano yung username na ginamit mo sa github? ")
        reader.set_value("user", "email", email)
    if name == "" or name == None:
        name = input("Eh ano naman yung user name? ")
        reader.set_value("user", "name", name)

    print(f"Hi {name} with email {email} !!!")
    
    status = repo.git.status()
    if "Changes not staged" in status or "Untracked files" in status:
        print("\n\n\nThe following files are edited but not tracked...")
        for f in repo.untracked_files:
            print(f)
        
        confirmation = input("Do you want to upload them? (Yes/No) ? ")

        if confirmation.upper() == "YES":
            commit(repo)
        else:
            print("Stopping...")
    else:
        print("You are up to date so far...")
    
    
    