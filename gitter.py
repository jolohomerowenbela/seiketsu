import git
import os
import datetime

def commit(repo: git.Repo):
    branch_name = "branch_" + str(datetime.datetime.now()).replace(" ", "").replace("-", ".").replace(":", ".")
    repo.git.switch("-c", branch_name)
    repo.git.add(".")
    repo.git.commit("-m", input("What changes have you done? (kahit ilang words lang) "))
    repo.git.push("-u", "origin", branch_name)
    
if __name__ == '__main__':
    dirPath = os.getcwd()
    
    
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

    print("\n\n\nThe following files are edited but not tracked...")
    for f in repo.untracked_files:
        print(f)
    
    confirmation = input("Do you want to upload them? (Yes/No) ? ")

    if confirmation.upper() == "YES":
        commit(repo)
    else:
        print("Stopping...")
    
    
    