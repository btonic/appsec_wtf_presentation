from setuptools import setup

setup(name='appsec_wtf',
    version='0.0.1',
    description='Source code for the AppSec WTF? presentation.',
    packages=['app', 'cli', 'exploit'],
    scripts=['scripts/wtf', 'scripts/exec_poc']
)
