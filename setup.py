from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'pzbasket Python package'
LONG_DESCRIPTION = 'My first Python package about baskatball statistcs.'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="pzbasket",
    version=VERSION,
    author="zosialaa",
    author_email="zofia.lapinska@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=open("requirements.txt").readlines(),

    keywords=['python', 'pzkosz'],
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)
