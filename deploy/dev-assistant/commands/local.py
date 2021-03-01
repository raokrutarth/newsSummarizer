import logging
from subprocess import Popen, PIPE, STDOUT

log = logging.getLogger()

def run_local_cmd(cmd: str, directory: str):
    child = Popen(
        cmd,
        shell=True,
        executable='/bin/bash', # enforce bash shell
        stdout=PIPE,
        stderr=PIPE,
        stdin=PIPE,
        cwd=directory,  # run in given directory context
    )

    res, err = child.communicate()
    stdout, stderr = res.decode("utf-8").strip(), err.decode("utf-8").strip()

    return stdout, stderr

if __name__ == "__main__":
    print(run_local_cmd("ls -la", None))
    print(run_local_cmd("env", None))