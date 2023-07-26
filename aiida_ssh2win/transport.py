from aiida.common.escaping import escape_for_bash
from aiida.transports import SshTransport


class SshToWindowsTransport(SshTransport):
    """
    Support connection, command execution and data transfer to
    remote computers running Windows Powershell via SSH+SFTP.
    """

    def _exec_command_internal(
        self,
        command,
        combine_stderr=False,
        bufsize=-1,
    ):
        """
        Executes the specified command in bash login shell.

        Before the command is executed, changes directory to the current
        working directory as returned by self.getcwd().

        For executing commands and waiting for them to finish, use
        exec_command_wait.

        :param  command: the command to execute. The command is assumed to be
            already escaped using :py:func:`aiida.common.escaping.escape_for_bash`.
        :param combine_stderr: (default False) if True, combine stdout and
                stderr on the same buffer (i.e., stdout).
                Note: If combine_stderr is True, stderr will always be empty.
        :param bufsize: same meaning of the one used by paramiko.

        :return: a tuple with (stdin, stdout, stderr, channel),
            where stdin, stdout and stderr behave as file-like objects,
            plus the methods provided by paramiko, and channel is a
            paramiko.Channel object.
        """
        channel = self.sshclient.get_transport().open_session()
        channel.set_combine_stderr(combine_stderr)

        if self.getcwd() is not None:
            escaped_folder = escape_for_bash(self.getcwd()[1:])
            command_to_execute = f"cd {escaped_folder}; {command}"
        else:
            command_to_execute = command

        self.logger.debug(
            f"Command to be executed: {command_to_execute[:self._MAX_EXEC_COMMAND_LOG_SIZE]}"
        )

        channel.exec_command(f'powershell "{command_to_execute}"')

        stdin = channel.makefile("wb", bufsize)
        stdout = channel.makefile("rb", bufsize)
        stderr = channel.makefile_stderr("rb", bufsize)

        return stdin, stdout, stderr, channel
