import paramiko
import logging
from os.path import expanduser, abspath
import sys

log = logging.getLogger()

# restrict paramiko logging
logging.getLogger("paramiko").setLevel(logging.WARNING)


class RemoteSession:

    def __init__(self, hostname, username, password, ssh_key_path, ssh_port=22):
        '''
            return a session object to an active ssh
            bash session to the CL instance
        '''
        self.hostname = hostname
        self.username = username
        self.ssh_port = ssh_port
        self.ssh_key_path = abspath(expanduser(ssh_key_path)) if ssh_key_path else None
        self.password = password

        self.bash_sesh = self._get_new_bash_sesh()

    def _get_new_bash_sesh(self):
        try:
            log.info(
                "Establishing new ssh session on %s@%s:%d using ssh key file %s",
                self.username,
                self.hostname,
                self.ssh_port,
                self.ssh_key_path,
            )

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            if self.password:
                ssh.connect(
                    self.hostname,
                    username=self.username,
                    password=self.password,
                    port=self.ssh_port,
                    auth_timeout=15,  # max 15s wait for authentication
                    timeout=10,
                )
            else:
                ssh.connect(
                    self.hostname,
                    username=self.username,
                    key_filename=self.ssh_key_path,
                    look_for_keys=False,
                    port=self.ssh_port,
                    auth_timeout=15,  # max 15s wait for authentication
                    timeout=10,
                )

            log.info("Successfully established remote ssh session")
            return ssh
        except Exception as e:
            self._failed_secure_login(e)

    # the ": str" is a python3 only feature and acts as
    # a quick sanity check to confirm the python version is >3
    def send_bash_cmd(self, command: str, timeout=30):
        _, stdout, stderr = self.bash_sesh.exec_command(
            command,
            timeout=timeout,
        )

        result = stdout.readlines() + stderr.readlines()
        response = '\n'
        for r in result:
            response += r

        return response

    # def put_file_on_remote_device(remote_dir, local_file):
    #     local_file = abspath(local_file)
    #     if not exists(local_file) and not isfile(local_file):
    #         log('[-] Error uploading file %s to device. File does not exist' % (local_file))
    #         return
    #     err = '[-] Error uploading file %s to device. \nTrying again...' % (local_file)
    #     success = 'file %s uploaded to %s' % (local_file, HOSTNAME)
    #     _file_op_with_retry('put', remote_dir, local_file, success, err)

    # def get_file_from_device(remote_file_path, local_dest_dir):
    #     err = '[-] Error getting file %s from device. \nTrying again...' % remote_file_path
    #     success = 'file %s downloaded from %s saved in %s' % (remote_file_path, HOSTNAME, local_dest_dir)
    #     _file_op_with_retry('get', remote_file_path, local_dest_dir, success, err)

    # def _file_op_with_retry(op, remote_path, local_path, success_msg='', fail_msg='', retry=10):
    #     sftp = _get_ftp_sesh()
    #     for i in range(retry):
    #         try:
    #             if op == 'get':
    #                 sftp.get(remote_path, local_path)
    #             elif op == 'put':
    #                 sftp.put(local_path, remote_path)
    #             else:
    #                 log('[-] unknown op in _file_op_with_retry. op: {}'.format(op))
    #                 exit(-1)
    #         except Exception as err:
    #             log('[-] Error: %s' % err.__str__())
    #             log('[fail]' + fail_msg)
    #             sleep(5)
    #         else:
    #             log(success_msg)
    #             log("sucessfully %s %s on device after %d attempt(s)" % (op, local_path, i))
    #             return
    #     log("[-] failed to %s %s after %d retries" % (op, local_path, retry))

    # def _get_ftp_sesh():
    #     global _REMOTE_FTP_SESH
    #     if not _REMOTE_FTP_SESH:
    #         privilege_uname = 'root'
    #         # FIXME
    #         # need to set empty root password since
    #         # the new halon default does not allows openssl commands
    #         privilege_pwd = "''" # str(uuid4())
    #         _set_usr_pwd(privilege_uname, privilege_pwd)

    #         ssh = paramiko.SSHClient()
    #         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #         ssh.connect(HOSTNAME, username=privilege_uname, password=privilege_pwd, port=SSH_PORT)
    #         sftp = SCPClient(ssh.get_transport(), socket_timeout=BASH_TIMEOUT)
    #         _REMOTE_FTP_SESH = sftp

    #         if not _REMOTE_FTP_SESH:
    #             failed_secure_login(failed_at='sftp')
    #     return _REMOTE_FTP_SESH

    # def _set_usr_pwd(usr, pwd):
    #     log('setting %s password to %s' % (usr, pwd))
    #     if pwd != "''":
    #         pwd = '$(openssl passwd %s)' % (pwd)
    #     # send_bash_cmd("sudo usermod %s -p %s" % (usr, pwd))
    #     send_bash_cmd("usermod %s -p %s" % (usr, pwd))

    # def _terminate_remote_ftp_sesh():
    #     if _REMOTE_FTP_SESH:
    #         _REMOTE_FTP_SESH.close()

    def _failed_secure_login(self, exception, failed_at="ssh"):
        log.error('exception: %s\n\n', exception)
        log.error(
            '\n\n'
            'Unable to establish {} session to {}.\n'
            'Are you able to manually log in to the CL instance?\n'
            'Is the CL instance active?\n'
            'Verify port {} is available and is the ssh port\n'
            'Verify ssh login is enabled\n'
            'Verify username is "{}"\n'
            'Verify password is "{}"\n'
            'Verify ssh keys are in  {}\n'
            'Try remove old keys with:\n'
            '\tssh-keygen -f "$HOME/.ssh/known_hosts" -R {}\n'
            'Exiting...\n'.format(
                failed_at,
                self.hostname,
                self.ssh_port,
                self.username,
                self.password,
                self.ssh_key_path,
                self.hostname,
            )
        )
        sys.exit(-1)

    # # proc_name_substr does not need to be full process name
    # # but should be unique enough to identify one process
    # def kill_existing_proc(proc_name_substr):
    #     log('killing pocess with %s in process name' % (proc_name_substr))
    #     pid_get = "$(ps -ef | grep \"%s\" | grep -v grep | awk '{print $2}')" % (proc_name_substr)
    #     # kill_cmd = "for pid in {}; do sudo kill -9 $pid; done".format(pid_get)
    #     kill_cmd = "for pid in {}; do kill -9 $pid; done".format(pid_get)
    #     send_bash_cmd(kill_cmd)

    def terminate_sessions(self):
        self.bash_sesh.close()

