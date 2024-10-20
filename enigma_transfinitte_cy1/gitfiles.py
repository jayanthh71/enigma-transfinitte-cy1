from git import Repo
from time import time as t
import os

s = str(int(t()))


def collect_code_files(folder_path, code_extensions):
    global s
    code_files = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(code_extensions):
                code_files.append(os.path.join(root, file))

    return code_files


def git_repository(git_url):
    global s
    Repo.clone_from(
        git_url, os.path.join(os.path.expanduser("~"), "Desktop\\tests" + s)
    )
    folder_path = os.path.join(os.path.expanduser("~"), "Desktop\\tests" + s)
    code_extensions = (
        ".py",
        ".java",
        ".cpp",
        ".c",
        ".js",
        ".html",
        ".css",
        ".php",
        ".rb",
        ".swift",
        ".go",
        ".sh",
        ".ts",
        ".xml",
        ".json",
        ".cs",
        ".h",
    )
    code_files = collect_code_files(folder_path, code_extensions)
    s = ""
    for i in code_files:
        s = s + "\nfile name:" + i.split("\\")[-1] + "\n"
        with open(i, "r") as f:
            s = s + f.read()
    return s


if __name__ == "__main__":
    print(git_repository(input("Enter the github repository link: ")))
