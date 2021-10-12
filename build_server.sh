python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
export FLASK_APP=server.py
export FLASK_DEBUG=1
python3 -m flask run --host=0.0.0.0 --port=5000
