import json
import os


def open_file(file_name):
    with open(
        os.path.abspath(f"task_manager/fixtures/{file_name}"), "r"
    ) as file:
        return json.loads(file.read())
