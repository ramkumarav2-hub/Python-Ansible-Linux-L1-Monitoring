
import subprocess

# List of playbooks
playbooks = [
    "Disk Check",
    "CPU Check",
    "Memory Check",
    "Linux Connectivity Check",
    "Restart Qualys"
]

# Show menu
print("\n" + "#" * 90)
print("#" + " " * 30 + "Linux L1 Monitoring" + " " * 39 + "#")
print("#" * 90 + "\n")

print("Please select the task you want to run:\n")
for i, pb in enumerate(playbooks, start=1):
    print(f"{i}. {pb}")

print("\n" + "*" * 90 + "\n")

choice = input("Enter your choice (number): ").strip()

# Validate choice
if choice == "1":
    extra_vars = ""
    server_name = input("Enter the server name or IP [Press Enter to use default inventory]: ").strip()
    mount_point = input("Enter the mount point (e.g., /var) [Press Enter for all mount points]: ").strip()
    extra_vars = f"--extra-vars mount_point={mount_point}"

    # Build command
    cmd = ["ansible-playbook", "/home/rvi2815-2/monitoring/tasks/disk_usage.yml"]
    
    
    if server_name:
       cmd.extend(["-i", f"{server_name},"])

    if extra_vars:
       cmd.extend(extra_vars.split())

    # Run playbook
    print(f"\nRunning: {' '.join(cmd)}\n")

    try:
       subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
       print(f"Error running playbook: {e}")

elif choice == "2":
    server_name = input("Enter the server name or IP [Press Enter to use default inventory]: ").strip()
    cmd = ["ansible-playbook", "/home/rvi2815-2/monitoring/tasks/cpu_usage.yml"]

    if server_name:
       cmd.extend(["-i", f"{server_name},"])

    # Run playbook
    print(f"\nRunning: {' '.join(cmd)}\n")

    try:
       subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
       print(f"Error running playbook: {e}")

elif choice == "3":
    server_name = input("Enter the server name or IP [Press Enter to use default inventory]: ").strip()
    cmd = ["ansible-playbook", "/home/rvi2815-2/monitoring/tasks/memory_usage.yml"]

    if server_name:
       cmd.extend(["-i", f"{server_name},"])

    # Run playbook
    print(f"\nRunning: {' '.join(cmd)}\n")

    try:
       subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
       print(f"Error running playbook: {e}")

elif choice == "4":
    server_name = input("Enter the server name or IP [Press Enter to use default inventory]: ").strip()
    cmd = ["ansible-playbook", "/home/rvi2815-2/monitoring/tasks/connectivity_check.yml"]

    if server_name:
       cmd.extend(["-i", f"{server_name},"])

    # Run playbook
    print(f"\nRunning: {' '.join(cmd)}\n")

    try:
       subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
       print(f"Error running playbook: {e}")

elif choice == "5":
    server_name = input("Enter the server name or IP [Press Enter to use default inventory]: ").strip()
    cmd = ["ansible-playbook", "/home/rvi2815-2/monitoring/tasks/qualys_restart.yml"]

    if server_name:
       cmd.extend(["-i", f"{server_name},"])

    # Run playbook
    print(f"\nRunning: {' '.join(cmd)}\n")

    try:
       subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
       print(f"Error running playbook: {e}")

else:
    print("Invalid choice!")
