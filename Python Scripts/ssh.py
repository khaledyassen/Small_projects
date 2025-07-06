import paramiko
import getpass

# SSH connection details
hostname = '143.42.19.242'  # Replace with the target hostname or IP address
port = 22  # Replace with the desired SSH port
username = 'root'  # Replace with your SSH username

# Prompt for SSH password
password = getpass.getpass(prompt='Enter SSH password: ')

# Create SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to SSH server
    client.connect(hostname, port=port, username=username, password=password)

    # Open a remote shell
    ssh_shell = client.invoke_shell()

    # Enter an interactive loop to interact with the shell
    while True:
        # Read from the shell
        output = ssh_shell.recv(1024).decode()
        if not output:
            break

        # Print the output
        print(output, end='')

        # Read user input and send to the shell
        command = input()
        ssh_shell.send(command + '\n')

    # Close the SSH connection
    client.close()

except paramiko.AuthenticationException:
    print("Authentication failed. Please check your username and password.")
except paramiko.SSHException as ssh_exception:
    print(f"SSH error occurred: {ssh_exception}")
except paramiko.Exception as e:
    print(f"Error occurred: {e}")
