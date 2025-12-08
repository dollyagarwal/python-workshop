# Setup Instructions
Ensure Python 3.10+ is installed: python --version.

# create & activate venv
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

# install base tools
pip install -r requirements.txt

# (optional) notebooks
pip install notebook jupyterlab

# Run notebooks
jupyter lab

