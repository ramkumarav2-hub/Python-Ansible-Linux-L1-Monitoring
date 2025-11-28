Process Explanation
This workflow automates Linux L1 monitoring tasks using a Python script and Ansible playbooks. The process begins with a menu-driven Python script that prompts the user 
to select a task (Disk, CPU, Memory, Connectivity, or Qualys Restart). Based on user input, the script dynamically constructs an Ansible command, optionally including 
parameters like server name or mount point. The command is executed using subprocess.run(), and error handling ensures failures are reported. This approach reduces manual 
effort, ensures consistency, and improves operational efficiency.
 
Python Script Workflow
Key steps in the Python script:
1. Display menu with available tasks.
2. Prompt user for choice and validate input.
3. Collect additional inputs (server name, mount point if applicable).
4. Build Ansible command dynamically based on user input.
5. Execute playbook using subprocess.run().
6. Handle errors and display appropriate messages.
7. Exit or prompt for invalid choice.

Ansible Playbooks
Below are the playbooks used in this workflow:
1.	connectivity_check.yml
2.	cpu_usage.yml
3.	disk_usage.yml
4.	memory_usage.yml
5.	qualys_restart.yml
   
Playbook Purposes
Below are the purposes of each playbook included in this workflow:
•	Disk Usage Monitoring: Checks disk usage for specified mount points and alerts if usage exceeds a defined threshold.
•	CPU Usage Monitoring: Monitors CPU utilization and retrieves top processes when usage exceeds a defined threshold.
•	Memory Usage Monitoring: Calculates memory usage and alerts if usage exceeds a defined threshold.
•	Linux Connectivity Check: Verifies connectivity to Linux servers, checks SSH port availability, and gathers system information.
•	Qualys Service Restart: Restarts the Qualys Cloud Agent service and confirms its process is running.
