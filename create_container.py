import subprocess
import json

def spin_container(host):
    # Spin up a container for the given host
    container_id = subprocess.check_output(['docker', 'run', '-d', '-it', 'demo-runner:1.0']).strip().decode()

    # Run playbook inside the container using Ansible runner
    ansible_command = f'docker exec {container_id} ansible-runner run /opt/demo-runner/logs.yaml'
    subprocess.run(ansible_command, shell=True)

    # Stop and remove the container
    subprocess.run(['docker', 'stop', container_id])
    subprocess.run(['docker', 'rm', container_id])

def main():
    inventory_file = '/opt/demo-runner/inv-env'

    # Read the inventory file
    with open(inventory_file, 'r') as f:
        inventory_data = json.load(f)

    # Get the list of hosts from the inventory
    hosts = inventory_data['_meta']['hostvars'].keys()

    # Spin up containers and run playbook for each host
    for host in hosts:
        spin_container(host)

if __name__ == '__main__':
    main()
