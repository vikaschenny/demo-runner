#!/bin/bash
#!/bin/bash

inventory_file="inventory.ini"

echo "[legacy]" > "/opt/$inventory_file"
echo "$1" >> "/opt/$inventory_file"
echo "" >> "/opt/$inventory_file"

echo "[legacy:vars]" >> "/opt/$inventory_file"
echo "ansible_user=$2" >> "/opt/$inventory_file"
echo "ansible_password=$3" >> "/opt/$inventory_file"

echo "Inventory file created successfully at /opt/$inventory_file."

# Clone the GitHub repository
git clone https://github.com/vikaschenny/demo-runner.git -b master 

# Run additional commands or start your application here
#ansible-runner run -p /opt/demo-runner/playbook.yml -i /opt/inventory.ini
ansible-runner run /tmp/demo-runner -p /opt/demo-runner/playbook.yml -i inventory.ini
# Execute the CMD or whatever command was passed to the container
#exec "$@"
