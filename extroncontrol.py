import yaml
import paramiko


class ExtronControl:

    def __init__(self):
        self.units = []
        self.commands = []
        self.__get_units()
        self.__get_commands()

    def __get_units(self):
        with open(r'config\units.yml') as file2:
            self.units = yaml.safe_load(file2)
        self.units = self.units['units']

    def get_units(self):
        return self.units

    def get_commands(self):
        return self.commands

    def __get_commands(self):
        with open(r'config\commands.yml') as file:
            self.commands = yaml.safe_load(file)
        self.commands = self.commands['commands']

    def __init_connection(self, hostname, username, password, port):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password, port=port)
        return ssh

    def __read_response(self, value):
        lines = []
        for line in iter(value.readline, ""):
            print(line, end="")
            lines.append(line)
        return lines
    
    def __get_routing_port_command(self, level, name):
        return self.commands[level][name]

    def set_routing_ports(self, top, bottom, unit):
        """

        :param top: This is the string representation of the port number
        :param bottom: This is the string representation of the port number
        :param unit: This is the unit we want to run against.
        """
        ssh = self.__init_connection(unit['hostname'], unit['ssh_user'], unit['ssh_pass'], unit['ssh_port'])
        top = self.__get_routing_port_command("top", top)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(top)
        self.__read_response(ssh_stdout)
        bottom = self.__get_routing_port_command("bottom", bottom)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(bottom)
        self.__read_response(ssh_stdout)
        ssh.close()

    def start_recording(self, unit):
        """
        Starts recording on the specified extron SMP Unit
        :param unit:
        """
        ssh = self.__init_connection(unit['hostname'], unit['ssh_user'], unit['ssh_pass'], unit['ssh_port'])
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(self.commands['start_recording'])
        self.__read_response(ssh_stdout)
        ssh.close()

    def stop_recording(self, unit):
        """
        Stops recording on the specified extron SMP Unit
        :param unit:
        """
        ssh = self.__init_connection(unit['hostname'], unit['ssh_user'], unit['ssh_pass'], unit['ssh_port'])
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(self.commands['stop_recording'])
        self.__read_response(ssh_stdout)
        ssh.close()


