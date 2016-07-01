import pip

from pip.req import parse_requirements
from setuptools import find_packages, setup


def requirements(requirements_file):
    return [
        str(ir.req)
        for ir in parse_requirements(
         filename=requirements_file,
         session=pip.download.PipSession()
        )
    ]

app_description = (
    "Slackmoji: scripts for emoji control on Slack"
)

config = {
    "install_requires": requriements(requirements.txt),
    "description": app_description,
    "author": "Soham Roy",
    "author_email": "sr735@cornell.edu",
    "packages": find_packages(),
    "name": "slackmoji",
    "use_scm_version": {"write_to": "slackmoji/_version.py"},
    "setup_requires": ["setuptools_scm"],
    }
