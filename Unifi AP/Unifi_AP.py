
import paramiko
import json
import datetime
from mac_vendor_lookup import MacLookup

def convert_seconds(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    months, weeks = divmod(weeks, 4)  # Assuming 4 weeks in a month

    if months > 0:
        return f"{months} months   "
    elif weeks > 0:
        return f"{weeks} weeks    "
    elif days > 0:
        return f"{days} days     "
    elif hours > 0:
        return f"{hours} hours    "
    elif minutes > 0:
        return f"{minutes} minutes  "
    else:
        return f"{seconds} seconds  "



def ssh_command(hostname, username, password, command):
    # Create an SSH client
    client = paramiko.SSHClient()

    # Automatically add the remote host's SSH key (insecure)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        x = 1
        # Connect to the remote device
        client.connect(hostname, username=username, password=password)

        # Execute the command on the remote device
        stdin, stdout, stderr = client.exec_command(command)

        # Read the output from the command
        output = stdout.read().decode('utf-8')

        # Print the output
        data = json.loads(output)

        print("\nNo.\tIP Address\tMAC Address\t\tUptime\t\tHostname")
        print("-" * 75)

        for vap_entry in data["vap_table"]:
            sta_table = vap_entry.get("sta_table", [])
            for sta_entry in sta_table:
                hostname = sta_entry.get("hostname")
                ip = sta_entry.get("ip")
                mac = sta_entry.get("mac")
                timestamp = sta_entry.get("uptime")
                converted_time = convert_seconds(timestamp)

#---------------------------- Convert Mac --------------------------#
                if mac == "a4:97:5c:07:ce:28":
                     hostname = "baby camera"
                elif mac == "a4:97:5c:07:ce:27":
                     hostname = "baby monitor"
                elif mac == "d8:1f:12:8d:9a:5c":
                     hostname = "Tuya Smart"
                elif mac == "d8:1f:12:8d:87:93":
                     hostname = "Tuya Smart"
                elif mac == "d8:1f:12:8d:89:c2":
                     hostname = "Tuya Smart"
                elif mac == "d8:0d:17:e7:e3:c7":
                     hostname = "TP-Link Smart Plug"
                elif mac == "ba:81:4f:14:2c:a1":
                     hostname = "iPhone 8 Plus"


                else:
                     hostname = sta_entry.get("hostname")
#-------------------------------------------------------------------#

                print(f"{x})\t{ip}\t{mac}\t{converted_time}\t{hostname}")
                #print(vendor)
                x += 1

    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your credentials.")
    except paramiko.SSHException as ssh_exception:
        print("Error occurred while establishing SSH connection:", str(ssh_exception))
    finally:
        # Close the SSH connection
        client.close()


# Provide the necessary details for SSH connection
hostname = '192.168.1.111'
username = 'admin'
password = 'ssh-password'
command = 'mca-dump'

# Call the function to SSH into the remote device and run the command
ssh_command(hostname, username, password, command)