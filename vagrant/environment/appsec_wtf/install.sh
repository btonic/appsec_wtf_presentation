# Set up the virtual environment for the module
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
mkvirtualenv appsec_wtf

# Install the module into the virtualenv
cd /vagrant
pip install -r requirements.txt
python setup.py develop
