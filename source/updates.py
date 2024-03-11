import threading
import time

import git

import source.global_variables


def check_for_update():
    while True:
        repo = git.Repo('.')

        current_commit = repo.head.commit
        repo.remote().fetch()
        remote_commit = repo.remote().refs['master'].commit
        if current_commit != remote_commit:
            source.global_variables.UPDATE = True
        else:
            source.global_variables.UPDATE = False
        # print(source.global_variables.UPDATE)
        time.sleep(60)


def start_check_update():
    update_check_thread = threading.Thread(target=check_for_update)
    update_check_thread.start()
