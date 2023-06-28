#!/bin/bash

# Clone the GitHub repository
git clone https://github.com/vikaschenny/demo-runner.git -b master /opt/

# Run additional commands or start your application here

# Execute the CMD or whatever command was passed to the container
exec "$@"
