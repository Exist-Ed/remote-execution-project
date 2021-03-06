# remote-execution-project server

### Usage: _python main.py [OPTIONAL ARGUMENTS]_

Starts the server that executes the code sent by clients in the Docker container.

After the client forms a set of files with the source code of the program and describes the control script, the data is sent to the server and the control script is executed in the __Docker container__. Base container image: __ubuntu:20.04__ with pre-installed Python components and updated package index files ("/bin/bash: apt update").

# Optional arguments:

* _-ip_ &emsp; sets the IP address of the server. __Default: 127.0.0.1__
* _-port_ &emsp; sets the server port. __Default: 10203__

# Examples:

```bash
python main.py
```
Starts the server with IP: 127.0.0.1 on port 10203.

```bash
python main.py -ip "168.182.0.1"
```
Starts the server with IP: 168.182.0.1 on port 10203.

```bash
python main.py -ip "168.182.0.1" -port 5555
```
Starts the server with IP: 168.182.0.1 on port 5555.

# Installation

After launching the terminal, go to the directory where you want to install the program and perform the following
manipulations:

1. Install Python if it has not been installed before: [Python download link](https://www.python.org/downloads/)
2. Install Docker if it has not been installed before: [Docker download link](https://www.docker.com/get-started/)
3. Download the repository:
```bash
git clone https://github.com/Exist-Ed/remote-execution-project.git
```
4. Build worker image: 
```bash
cd ./setup
source ./build_worker_image.sh
```

5. Use the program. Installation is complete

