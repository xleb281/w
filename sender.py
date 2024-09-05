import os
from colorama import *
try:
    from github import Github
except:
    os.system("pip install PyGithub")
os.system("clear")
while True:
    access_token = "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"
    repo_name = "xleb281/init64308"  # например, "octocat/Hello-World"
    file_path = "init"  # путь к файлу в репозитории
    commit_message = "Изменено значение в файле"
    new_content = input(Fore.RED + "command:")  # новое значение для записи в файл
    if new_content == "0":
        exit()
    g = Github(access_token)
    repo = g.get_repo(repo_name)
    file_content = repo.get_contents(file_path)
    repo.update_file(file_content.path, commit_message, new_content, file_content.sha)
    print(f"Update command '{file_path}'")
