import os
from distutils.core import setup

# sync with __init__.py
version = '0.5'

setup(
    name="DynectDNS-proxy",
    version=version,
    keywords=["dynect", "api", "dns"],
    long_description=open(os.path.join(os.path.dirname(__file__),"README.md"), "r").read(),
    description="Dynect REST API wrapper with proxy support",
    author="Cole Tuininga",
    author_email="ctuininga@dyn.com",
    url="https://github.com/socrata/Dynect-API-Python-Library",
    packages=['dynect'],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: Name Service (DNS)',
        'Topic :: Software Development :: Libraries', 
    ],
)
