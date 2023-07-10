### Unifi-AP Script
This Python script will ssh into a Unifi AP, run a `mca-dump` command, and pull and process all the information from that output.

 #### Running the Script. 
`python3 Unifi_AP.py` 

#### Output
```
root@computer:~/scripts# python3 Unifi_AP.py

No.     IP Address      MAC Address             Uptime          Hostname
---------------------------------------------------------------------------
1)      192.168.2.112   a8:5f:0a:50:57:66       20 hours        iPhone 11
2)      192.168.2.113   a4:9f:63:2a:16:f4       3 days          iPad 
3)      192.168.2.111   ac:7f:8b:v2:e9:91       15 hours        Samsung TV
4)      192.168.2.17    a4:5f:9a:36:07:62       20 hours        iPhone 12
5)      192.168.2.18    a0:af:cb:5a:ec:a3       8 hours         Mac Air
6)      192.168.2.19    a4:7f:33:c4:e5:e3       7 minutes       Chromecast
7)      192.168.2.17    a4:cf:4e:95:4d:13       11 hours        Google-Nest-Mini
8)      192.168.2.16    a8:1f:12:2d:9b:5d       2 months        IR Bluster 
9)      192.168.2.13    a8:1f:12:4d:88:95       1 months        Andriod TV
10)     192.168.2.11    a8:1f:12:4d:81:c3       1 months        Samsung Galaxy
11)     192.168.2.15    a8:0f:17:b7:e2:c2       1 weeks         TP-Link Smart Plug
12)     192.168.2.14    a4:9f:5c:67:cd:25       15 hours        baby camera
13)     192.168.2.12    ac:ff:c4:77:34:63       2 hours         Raspberry Pi
```
 ----

Requirements.

pip install paramiko
pip install json
pip install datetime
pip install mac-vendor-lookup

----
 
Note I am using the `UniFi U6-Lite` but this should work for any Unifi Access Point. 
Credentials will need to be updated accordingly and these are found in the Unifi APP
