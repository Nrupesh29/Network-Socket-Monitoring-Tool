# Network-Socket-Monitoring-Tool

## Abstract

<table>
<tr>
<td>
<p align="justify">Use <a href="https://pythonhosted.org/psutil/">psutil</a> and implement a network socket monitoring tool that can check how many TCP sockets are being created by a web application. List all processes that have any socket connections (meaning the laddr and raddr fields exist). Group by the PID and sort the output by the number of the connections per process.</p>
</td>
</tr>
</table>

## System Requirements

* Python Version: 2.7.12

## Installation

1. Install psutil library

    ### UNIX
        sudo pip install psutil

    ### Linux
    Ubuntu / Debian
    
        sudo apt-get install gcc python-dev python-pip
        pip install psutil

    RedHat / CentOS
    
        sudo yum install gcc python-devel python-pip
        pip install psutil

    RedHat and CentOS
    
        sudo yum install python-psutil

    ### OSX
    Install [Xcode](https://developer.apple.com/downloads/?name=Xcode) first, then:
    
         pip install psutil

    ### Windows
    The easiest way to install psutil on Windows is to just use the pre-compiled exe/wheel installers hosted on [PYPI](https://pypi.python.org/pypi/psutil/#downloads) via pip
    
          C:\Python27\python.exe -m pip install psutil

2. Download [socket-mon.py](socket-mon.py)
3. Run the downloaded python script   
          
          sudo python socket-mon.py
          
## Output

```sh
$ sudo python socket-mon.py
"pid","laddr","raddr","status"
"2959","10.0.0.199@55169","173.194.203.188@5228","ESTABLISHED"
"2959","10.0.0.199@55206","151.101.128.133@443","ESTABLISHED"
"2959","10.0.0.199@55315","216.58.194.163@443","ESTABLISHED"
"2959","10.0.0.199@55304","192.30.253.125@443","ESTABLISHED"
"2959","10.0.0.199@55298","192.30.253.125@443","ESTABLISHED"
"2959","10.0.0.199@55268","151.101.128.133@443","ESTABLISHED"
"2959","10.0.0.199@55297","192.30.253.124@443","ESTABLISHED"
"2959","10.0.0.199@55269","172.217.6.78@443","ESTABLISHED"
"2959","10.0.0.199@55316","192.30.253.125@443","ESTABLISHED"
"2959","10.0.0.199@55271","172.217.6.78@443","ESTABLISHED"
"2959","10.0.0.199@55320","130.65.255.124@80","ESTABLISHED"
"2959","10.0.0.199@55193","151.101.128.133@443","ESTABLISHED"
"2959","10.0.0.199@55183","151.101.128.133@443","ESTABLISHED"
"2959","10.0.0.199@55187","151.101.128.133@443","ESTABLISHED"
"2959","10.0.0.199@55317","130.65.255.124@80","CLOSE_WAIT"
"2959","10.0.0.199@55194","151.101.128.133@443","ESTABLISHED"
"2959","10.0.0.199@55318","130.65.255.124@80","CLOSE_WAIT"
"2959","10.0.0.199@55196","151.101.128.133@443","ESTABLISHED"
"2959","10.0.0.199@55198","151.101.128.133@443","ESTABLISHED"
"2959","10.0.0.199@55199","151.101.128.133@443","ESTABLISHED"
"2959","10.0.0.199@55200","151.101.128.133@443","ESTABLISHED"
"2959","10.0.0.199@55272","216.58.195.78@443","ESTABLISHED"
"2733","10.0.0.199@54719","23.101.203.117@443","CLOSE"
"2733","10.0.0.199@54721","23.101.203.117@443","CLOSE"
"2733","10.0.0.199@54722","23.101.203.117@443","CLOSE"
"2733","10.0.0.199@54723","23.101.203.117@443","CLOSE"
"2733","10.0.0.199@54724","23.101.203.117@443","CLOSE"
"2733","10.0.0.199@54725","23.101.203.117@443","CLOSE"
"2505","10.0.0.199@55137","172.217.6.69@443","ESTABLISHED"
"2505","10.0.0.199@54328","74.125.28.189@443","ESTABLISHED"
"2505","10.0.0.199@54398","31.13.70.1@443","ESTABLISHED"
"2505","10.0.0.199@54356","31.13.77.36@443","ESTABLISHED"
"551","10.0.0.199@55053","174.129.220.120@443","ESTABLISHED"
"551","10.0.0.199@55053","174.129.220.120@443","ESTABLISHED"
"551","10.0.0.199@55310","54.84.180.22@443","ESTABLISHED"
"551","10.0.0.199@55310","54.84.180.22@443","ESTABLISHED"
"107","10.0.0.199@54048","17.249.12.21@5223","ESTABLISHED"
"107","10.0.0.199@54048","17.249.12.21@5223","ESTABLISHED"
"107","10.0.0.199@54137","17.188.165.200@5223","ESTABLISHED"
"107","10.0.0.199@54137","17.188.165.200@5223","ESTABLISHED"
"2514","127.0.0.1@54330","127.0.0.1@54332","ESTABLISHED"
"2514","127.0.0.1@54330","127.0.0.1@54333","ESTABLISHED"
"2513","127.0.0.1@54332","127.0.0.1@54330","ESTABLISHED"
"2513","127.0.0.1@54333","127.0.0.1@54330","ESTABLISHED"
"2735","10.0.0.199@55326","104.45.136.42@443","ESTABLISHED"
"296","10.0.0.199@54103","54.84.51.200@443","ESTABLISHED"
```

## Credits
Abstract - [Prof. Sithu Aung](https://github.com/sithu/cmpe273-spring17/blob/master/lab1/README.md) <br/>
psutil Installation Guide - [Giampaolo Rodola](https://github.com/giampaolo/psutil/blob/master/INSTALL.rst)

## Contributor
| [![Nrupesh Patel](https://avatars.githubusercontent.com/nrupesh29?s=100)<br /><sub>Nrupesh Patel<br />CMPE 273</sub>](https://github.com/Nrupesh29)<br /> |
| :---: |
