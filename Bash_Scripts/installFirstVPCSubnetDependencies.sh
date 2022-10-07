#!/bin/bash
sudo apt update && sudo apt -y install python3-pip &&  sudo apt -y install python3.10-venv
sleep 5
git clone https://github.com/kura-labs-org/kuralabs_deployment_1.git
cd kuralabs_deployment_1
python3 -m venv test3
sleep 5
source test3/bin/activate
sleep 5
pip install pip --upgrade
pip install -r requirements.txt
export FLASK_APP=application
flask run --host=0.0.0.0