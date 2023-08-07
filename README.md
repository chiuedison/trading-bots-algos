# trading-bots-algos
Various trading strategy bots for undergraduate trading competitions.

### Install Python
Install a recent version of Python.
#### macOS
```bash
$ brew install python3
```
#### WSL or Linux
```bash
$ sudo apt-get update
$ sudo apt-get install python3 python3-pip python3-venv python3-wheel python3-setuptools
```
### Create a Python virtual environment
This section will help you install the Python tools and packages locally, which won’t affect Python tools and packages installed elsewhere on your computer.

After finishing this section, you’ll have a folder called `env/` that contains all the Python packages you need for this project.

**Pitfall:** Do not use the version of Python provided by Anaconda. 

Create a virtual environment in your project’s root directory. 
```bash
$ pwd
/mnt/c/Users/gurish/OneDrive/Documents/jane-street-etc/jane-street-etc-UMICH
$ python3 -m venv env
```
Activate virtual environment. You’ll need to do this **every time** you start a new shell.
```bash
$ source env/bin/activate
```
We now have a complete local environment for Python. Everything lives in one directory. Environment variables point to this virtual environment.
```bash
$ echo $VIRTUAL_ENV
/mnt/c/Users/gurish/OneDrive/Documents/jane-street-etc/jane-street-etc-UMICH/env
```

### Install Python Tools
Upgrade the Python tools in your virtual environment
```bash
$ pip install --upgrade pip setuptools wheel
```
Install remaining requirements.
```bash
$ pip install -r requirements.txt
```
Double-check you have a .gitignore
