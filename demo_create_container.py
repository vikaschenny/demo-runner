import os
import shutil
from docker import DockerClient
from ansible_runner import Runner

def create_container(host):
    client = DockerClient.from_env()
    container = client.containers.create(
        image='demo-runner:1.0',
        command='tail -f /dev/null',
        name='container_' + host,
        detach=True,
        hostname=host,
        network_mode='host',
        volumes={
            os.path.abspath(os.getcwd()): {
                'bind': '/ansible',
                'mode': 'rw'
            }
        }
    )
    container.start()
    return container

def run_playbook(host):
    runner = Runner(
        inventory='inventory.ini',
        playbook='playbook.yml',
        private_data_dir='runner_' + host
    )
    runner.run()

def main():
    inventory_file = 'inventory.ini'
    playbook_file = 'playbook.yml'

    with open(inventory_file, 'r') as f:
        inventory_content = f.read()

    hosts = [host.strip() for host in inventory_content.splitlines() if host.strip()]
    
    for host in hosts:
        container = create_container(host)
        try:
            shutil.copytree(os.path.dirname(playbook_file), 'runner_' + host + '/artifacts')
            run_playbook(host)
        finally:
            container.stop()
            container.remove()

if __name__ == '__main__':
    main()

