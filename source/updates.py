import threading

import git

import source.global_variables


def check_for_update():
    repo = git.Repo('.')

    current_commit = repo.head.commit
    repo.remote().fetch()
    remote_commit = repo.remote().refs['master'].commit
    if current_commit != remote_commit:
        source.global_variables.UPDATE = True
    else:
        source.global_variables.UPDATE = False


def start_check_update():
    update_check_thread = threading.Thread(target=check_for_update)
    update_check_thread.start()
