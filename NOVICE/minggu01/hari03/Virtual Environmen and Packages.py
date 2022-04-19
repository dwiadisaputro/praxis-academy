###-- Creat Virtuan Envirotments
##di linux
#masukkan script
#  sudo apt install python3.8-venv
#hasilnya
# Reading package lists... Done
# Building dependency tree       
# Reading state information... Done
# The following packages were automatically installed and are no longer required:
#   libfwupdplugin1 libllvm11 libnvidia-cfg1-460 libnvidia-common-460 libnvidia-compute-460
#   libnvidia-decode-460 libnvidia-encode-460 libnvidia-extra-460 libnvidia-fbc1-460 libnvidia-gl-460
#   libnvidia-ifr1-460 nvidia-compute-utils-460 nvidia-kernel-common-460 nvidia-kernel-source-460
#   nvidia-utils-460 shim xserver-xorg-video-nvidia-460
# Use 'sudo apt autoremove' to remove them.
# The following NEW packages will be installed:
#   python3.8-venv
# 0 upgraded, 1 newly installed, 0 to remove and 15 not upgraded.
# Need to get 5.448 B of archives.
# After this operation, 27,6 kB of additional disk space will be used.
# Get:1 http://id.archive.ubuntu.com/ubuntu focal-updates/universe amd64 python3.8-venv amd64 3.8.10-0ubuntu1~20.04.4 [5.448 B]
# Fetched 5.448 B in 2s (2.637 B/s)                        
# Selecting previously unselected package python3.8-venv.
# (Reading database ... 203902 files and directories currently installed.)
# Preparing to unpack .../python3.8-venv_3.8.10-0ubuntu1~20.04.4_amd64.deb ...
# Unpacking python3.8-venv (3.8.10-0ubuntu1~20.04.4) ...
# Setting up python3.8-venv (3.8.10-0ubuntu1~20.04.4) ...

### --- install novas---
#masukkan script
# python3 -m pip install novas
##---hasilnya---
# Collecting novas
#   Downloading novas-3.1.1.5.tar.gz (135 kB)
#      |████████████████████████████████| 135 kB 268 kB/s 
# Building wheels for collected packages: novas
#   Building wheel for novas (setup.py) ... done
#   Created wheel for novas: filename=novas-3.1.1.5-cp38-cp38-linux_x86_64.whl size=169871 sha256=3a9fc7326b9886ccc4a3e41096cee3058d3a97c42f7dc28b62d62745ce572290
#   Stored in directory: /home/blk/.cache/pip/wheels/5f/3b/72/e7dba9d085106f46a87b5c1ce1405b6132fb10e343d8d312a0
# Successfully built novas
# Installing collected packages: novas
# Successfully installed novas-3.1.1.5


##----instal requests---
#masukkan script:
# pip install requests
##---hasilnya----
# Requirement already satisfied: requests in /usr/lib/python3/dist-packages (2.22.0)

##---show request---
#pip show requests
##---hasilnya---
# Name: requests
# Version: 2.22.0
# Summary: Python HTTP for Humans.
# Home-page: http://python-requests.org
# Author: Kenneth Reitz
# Author-email: me@kennethreitz.org
# License: Apache 2.0
# Location: /usr/lib/python3/dist-packages
# Requires: 
# Required-by: 

##--Pip list---
#script: pip list
##----hasilnya---
# Package                 Version             
# ----------------------- --------------------
# apturl                  0.5.2               
# bcrypt                  3.1.7               
# blinker                 1.4                 
# Brlapi                  0.7.0               
# certifi                 2019.11.28          
# chardet                 3.0.4               
# Click                   7.0                 
# colorama                0.4.3               
# command-not-found       0.3                 
# cryptography            2.8                 
# cupshelpers             1.0                 
# dbus-python             1.2.16              
# defer                   1.0.6               
# distro                  1.4.0               
# distro-info             0.23ubuntu1         
# duplicity               0.8.12.0            
# EditorConfig            0.12.2              
# entrypoints             0.3                 
# fasteners               0.14.1              
# Fibo                    1.0.0               
# future                  0.18.2              
# httplib2                0.14.0              
# idna                    2.8                 
# jsbeautifier            1.10.3              
# keyring                 18.0.1              
# language-selector       0.1                 
# launchpadlib            1.10.13             
# lazr.restfulclient      0.14.2              
# lazr.uri                1.0.3               
# lockfile                0.12.2              
# louis                   3.12.0              
# macaroonbakery          1.3.1               
# Mako                    1.1.0               
# MarkupSafe              1.1.0               
# monotonic               1.5                 
# netifaces               0.10.4              
# novas                   3.1.1.5             
# numpy                   1.22.3              
# oauthlib                3.1.0               
# olefile                 0.46                
# paramiko                2.6.0               
# pexpect                 4.6.0               
# Pillow                  7.0.0               
# pip                     20.0.2              
# protobuf                3.6.1               
# pycairo                 1.16.2              
# pycups                  1.9.73              
# PyGObject               3.36.0              
# PyJWT                   1.7.1               
# pymacaroons             0.13.0              
# PyNaCl                  1.3.0               
# pyRFC3339               1.1                 
# python-apt              2.0.0+ubuntu0.20.4.7
# python-dateutil         2.7.3               
# python-debian           0.1.36ubuntu1       
# pytz                    2019.3              
# pyxdg                   0.26                
# PyYAML                  5.3.1               
# reportlab               3.5.34              
# requests                2.22.0              
# requests-unixsocket     0.2.0               
# screen-resolution-extra 0.0.0               
# SecretStorage           2.3.1               
# setuptools              45.2.0              
# simplejson              3.16.0              
# six                     1.14.0              
# systemd-python          234                 
# ubuntu-advantage-tools  27.7                
# ubuntu-drivers-common   0.0.0               
# ufw                     0.36                
# unattended-upgrades     0.1                 
# urllib3                 1.25.8              
# usb-creator             0.3.7               
# wadllib                 1.3.3               
# wheel                   0.34.2              
# xkit                    0.0.0  

##--- pip freeze dan cat requirements--
##--hasilnya---
# apturl==0.5.2
# bcrypt==3.1.7
# blinker==1.4
# Brlapi==0.7.0
# certifi==2019.11.28
# chardet==3.0.4
# Click==7.0
# colorama==0.4.3
# command-not-found==0.3
# cryptography==2.8
# cupshelpers==1.0
# dbus-python==1.2.16
# defer==1.0.6
# distro==1.4.0
# distro-info===0.23ubuntu1
# duplicity==0.8.12.0
# EditorConfig==0.12.2
# entrypoints==0.3
# fasteners==0.14.1
# Fibo==1.0.0
# future==0.18.2
# httplib2==0.14.0
# idna==2.8
# jsbeautifier==1.10.3
# keyring==18.0.1
# language-selector==0.1
# launchpadlib==1.10.13
# lazr.restfulclient==0.14.2
# lazr.uri==1.0.3
# lockfile==0.12.2
# louis==3.12.0
# macaroonbakery==1.3.1
# Mako==1.1.0
# MarkupSafe==1.1.0
# monotonic==1.5
# netifaces==0.10.4
# novas==3.1.1.5
# numpy==1.22.3
# oauthlib==3.1.0
# olefile==0.46
# paramiko==2.6.0
# pexpect==4.6.0
# Pillow==7.0.0
# protobuf==3.6.1
# pycairo==1.16.2
# pycups==1.9.73
# PyGObject==3.36.0
# PyJWT==1.7.1
# pymacaroons==0.13.0
# PyNaCl==1.3.0
# pyRFC3339==1.1
# python-apt==2.0.0+ubuntu0.20.4.7
# python-dateutil==2.7.3
# python-debian===0.1.36ubuntu1
# pytz==2019.3
# pyxdg==0.26
# PyYAML==5.3.1
# reportlab==3.5.34
# requests==2.22.0
# requests-unixsocket==0.2.0
# screen-resolution-extra==0.0.0
# SecretStorage==2.3.1
# simplejson==3.16.0
# six==1.14.0
# systemd-python==234
# ubuntu-advantage-tools==27.7
# ubuntu-drivers-common==0.0.0
# ufw==0.36
# unattended-upgrades==0.1
# urllib3==1.25.8
# usb-creator==0.3.7
# wadllib==1.3.3
# xkit==0.0.0

##---requirements.txt--
##-- masukkan script : python3 -m pip install -r requirements.txt
###----hasilnya---
# Requirement already satisfied: apturl==0.5.2 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 1)) (0.5.2)
# Requirement already satisfied: bcrypt==3.1.7 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 2)) (3.1.7)
# Requirement already satisfied: blinker==1.4 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 3)) (1.4)
# Requirement already satisfied: Brlapi==0.7.0 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 4)) (0.7.0)
# Requirement already satisfied: certifi==2019.11.28 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 5)) (2019.11.28)
# Requirement already satisfied: chardet==3.0.4 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 6)) (3.0.4)
# Requirement already satisfied: Click==7.0 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 7)) (7.0)
# Requirement already satisfied: colorama==0.4.3 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 8)) (0.4.3)
# Requirement already satisfied: command-not-found==0.3 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 9)) (0.3)
# Requirement already satisfied: cryptography==2.8 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 10)) (2.8)
# Requirement already satisfied: cupshelpers==1.0 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 11)) (1.0)
# Requirement already satisfied: dbus-python==1.2.16 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 12)) (1.2.16)
# Requirement already satisfied: defer==1.0.6 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 13)) (1.0.6)
# Requirement already satisfied: distro==1.4.0 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 14)) (1.4.0)
# Requirement already satisfied: distro-info===0.23ubuntu1 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 15)) (0.23ubuntu1)
# Requirement already satisfied: duplicity==0.8.12.0 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 16)) (0.8.12.0)
# Requirement already satisfied: EditorConfig==0.12.2 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 17)) (0.12.2)
# Requirement already satisfied: entrypoints==0.3 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 18)) (0.3)
# Requirement already satisfied: fasteners==0.14.1 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 19)) (0.14.1)
# Requirement already satisfied: Fibo==1.0.0 in /home/blk/.local/lib/python3.8/site-packages (from -r requirements.txt (line 20)) (1.0.0)
# Requirement already satisfied: future==0.18.2 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 21)) (0.18.2)
# Requirement already satisfied: httplib2==0.14.0 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 22)) (0.14.0)
# Requirement already satisfied: idna==2.8 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 23)) (2.8)
# Requirement already satisfied: jsbeautifier==1.10.3 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 24)) (1.10.3)
# Requirement already satisfied: keyring==18.0.1 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 25)) (18.0.1)
# Requirement already satisfied: language-selector==0.1 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 26)) (0.1)
# Requirement already satisfied: launchpadlib==1.10.13 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 27)) (1.10.13)
# Requirement already satisfied: lazr.restfulclient==0.14.2 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 28)) (0.14.2)
# Requirement already satisfied: lazr.uri==1.0.3 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 29)) (1.0.3)
# Requirement already satisfied: lockfile==0.12.2 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 30)) (0.12.2)
# Requirement already satisfied: louis==3.12.0 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 31)) (3.12.0)
# Requirement already satisfied: macaroonbakery==1.3.1 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 32)) (1.3.1)
# Requirement already satisfied: Mako==1.1.0 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 33)) (1.1.0)
# Requirement already satisfied: MarkupSafe==1.1.0 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 34)) (1.1.0)
# Requirement already satisfied: monotonic==1.5 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 35)) (1.5)
# Requirement already satisfied: netifaces==0.10.4 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 36)) (0.10.4)
# Requirement already satisfied: novas==3.1.1.5 in /home/blk/.local/lib/python3.8/site-packages (from -r requirements.txt (line 37)) (3.1.1.5)
# Requirement already satisfied: numpy==1.22.3 in /home/blk/.local/lib/python3.8/site-packages (from -r requirements.txt (line 38)) (1.22.3)
# Requirement already satisfied: oauthlib==3.1.0 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 39)) (3.1.0)
# Requirement already satisfied: olefile==0.46 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 40)) (0.46)
# Requirement already satisfied: paramiko==2.6.0 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 41)) (2.6.0)
# Requirement already satisfied: pexpect==4.6.0 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 42)) (4.6.0)
# Requirement already satisfied: Pillow==7.0.0 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 43)) (7.0.0)
# Requirement already satisfied: protobuf==3.6.1 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 44)) (3.6.1)
# Requirement already satisfied: pycairo==1.16.2 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 45)) (1.16.2)
# Requirement already satisfied: pycups==1.9.73 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 46)) (1.9.73)
# Requirement already satisfied: PyGObject==3.36.0 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 47)) (3.36.0)
# Requirement already satisfied: PyJWT==1.7.1 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 48)) (1.7.1)
# Requirement already satisfied: pymacaroons==0.13.0 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 49)) (0.13.0)
# Requirement already satisfied: PyNaCl==1.3.0 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 50)) (1.3.0)
# Requirement already satisfied: pyRFC3339==1.1 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 51)) (1.1)
# Requirement already satisfied: python-apt==2.0.0+ubuntu0.20.4.7 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 52)) (2.0.0+ubuntu0.20.4.7)
# Requirement already satisfied: python-dateutil==2.7.3 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 53)) (2.7.3)
# Requirement already satisfied: python-debian===0.1.36ubuntu1 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 54)) (0.1.36ubuntu1)
# Requirement already satisfied: pytz==2019.3 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 55)) (2019.3)
# Requirement already satisfied: pyxdg==0.26 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 56)) (0.26)
# Requirement already satisfied: PyYAML==5.3.1 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 57)) (5.3.1)
# Requirement already satisfied: reportlab==3.5.34 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 58)) (3.5.34)
# Requirement already satisfied: requests==2.22.0 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 59)) (2.22.0)
# Requirement already satisfied: requests-unixsocket==0.2.0 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 60)) (0.2.0)
# Requirement already satisfied: screen-resolution-extra==0.0.0 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 61)) (0.0.0)
# Requirement already satisfied: SecretStorage==2.3.1 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 62)) (2.3.1)
# Requirement already satisfied: simplejson==3.16.0 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 63)) (3.16.0)
# Requirement already satisfied: six==1.14.0 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 64)) (1.14.0)
# Requirement already satisfied: systemd-python==234 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 65)) (234)
# Requirement already satisfied: ubuntu-advantage-tools==27.7 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 66)) (27.7)
# Requirement already satisfied: ubuntu-drivers-common==0.0.0 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 67)) (0.0.0)
# Requirement already satisfied: ufw==0.36 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 68)) (0.36)
# Requirement already satisfied: unattended-upgrades==0.1 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 69)) (0.1)
# Requirement already satisfied: urllib3==1.25.8 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 70)) (1.25.8)
# Requirement already satisfied: usb-creator==0.3.7 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 71)) (0.3.7)
# Requirement already satisfied: wadllib==1.3.3 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 72)) (1.3.3)
# Requirement already satisfied: xkit==0.0.0 in /usr/lib/python3/dist-packages (from -r requirements.txt (line 73)) (0.0.0)
# Requirement already satisfied: setuptools in /usr/lib/python3/dist-packages (from launchpadlib==1.10.13->-r requirements.txt (line 27)) (45.2.0)
# Collecting testresources
#   Downloading testresources-2.0.1-py2.py3-none-any.whl (36 kB)
# Collecting pbr>=1.8
#   Downloading pbr-5.8.1-py2.py3-none-any.whl (113 kB)
#      |████████████████████████████████| 113 kB 140 kB/s 
# Installing collected packages: pbr, testresources
#   WARNING: The script pbr is installed in '/home/blk/.local/bin' which is not on PATH.
#   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
# Successfully installed pbr-5.8.1 testresources-2.0.1


##---instal numpy---
# pip install numpy
##--hasilnya---
# Collecting numpy
#   Downloading numpy-1.22.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.8 MB)
#      |████████████████████████████████| 16.8 MB 1.6 MB/s 
# Installing collected packages: numpy
#   WARNING: The scripts f2py, f2py3 and f2py3.8 are installed in '/home/blk/.local/bin' which is not on PATH.
#   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
# Successfully installed numpy-1.22.3