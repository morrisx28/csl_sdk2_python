# csl_sdk2_python
Python interface for csl sdk2
refer to https://github.com/unitreerobotics/unitree_sdk2_python.git

# Installation
## Dependencies
- Python >= 3.8
- cyclonedds == 0.10.2
- numpy
- opencv-python
## Install csl_sdk2_python

Execute the following commands in the terminal:
```bash
cd ~
sudo apt install python3-pip
git clone https://github.com/morrisx28/csl_sdk2_python.git
cd csl_sdk2_python
pip3 install -e .
```
## FAQ
##### 1. Error when `pip3 install -e .`:
```bash
Could not locate cyclonedds. Try to set CYCLONEDDS_HOME or CMAKE_PREFIX_PATH
```
This error mentions that the cyclonedds path could not be found. First compile and install cyclonedds:

```bash
cd ~
git clone https://github.com/eclipse-cyclonedds/cyclonedds -b releases/0.10.x 
cd cyclonedds && mkdir build install && cd build
cmake .. -DCMAKE_INSTALL_PREFIX=../install
cmake --build . --target install
```
Enter the csl_sdk2_python directory, set `CYCLONEDDS_HOME` to the path of the cyclonedds you just compiled, and then install csl_sdk2_python.
```bash
cd ~/csl_sdk2_python
export CYCLONEDDS_HOME="~/cyclonedds/install"
pip3 install -e .
```
