# raspberry-pi-timelapse-camera

# Setup Access Point
After install [Raspbian Jessie Lite](https://www.raspberrypi.org/downloads/raspbian/) run:
```
$ sudo -s
$ apt-get install hostapd
$ apt-get install dnsmasq
$ apt-get update
$ apt-get upgrade
```

Edit the `iface wlan0` part of your `/etc/network/interfaces` file to look like:
```
iface wlan0 inet static
    address 10.0.0.1
    netmask 255.255.255.0
```

At the bottom of `/etc/dhcpcd.conf` add:
```
interface wlan0  
    static ip_address=172.24.1.1/24
```

Edit the `DAEMON_CONF` part of your `/etc/default/hostapd` file to look like:
```
DAEMON_CONF="/etc/hostapd/hostapd.conf"
```

Make a `/etc/hostapd/hostapd.conf` file with:
```
interface=wlan0
driver=nl80211
ssid=a_potato
channel=1
```

Make a `/etc/dnsmasq.conf` file with:
```
interface=wlan0
dhcp-range=10.0.0.2,10.0.0.5,255.255.255.0,12h 
```

Reboot your device and an open access point called `a_potato` will automatically run!
You should be able to see it and connect to it from another device, however it may give you a warning about not having an internet connection.

Credit:
- https://frillip.com/using-your-raspberry-pi-3-as-a-wifi-access-point-with-hostapd
- http://sirlagz.net/2012/08/09/how-to-use-the-raspberry-pi-as-a-wireless-access-pointrouter-part-1
- https://nims11.wordpress.com/2012/04/27/hostapd-the-linux-way-to-create-virtual-wifi-access-point

# Setup local server
```
$ apt-get install apache2
```
You should be able to acess the apache homepage now by connecting to the wifi network and going to `http://10.0.0.1`

# Mount USB drive (to store the images)
```
$ mkdir /media/usbstick
$ mount -t vfat -o rw /dev/sda1 /media/usbstick/
$ mount -t vfat -o uid=pi,gid=pi /dev/sda1 /media/usbstick/
```

Credit:
- http://raspi.tv/2012/mount-a-usb-flash-drive-on-raspberry-pi


# Communicating with the LinkitOne
Deploy the LinkitOne application through the regular Arduino upload method. Then connect it to the Raspberry Pi and run:
```
$ apt-get install python-serial
$ apt-get install git
$ apt-get install python-pip
$ cd raspberry-pi-timelapse-camera/raspberry-pi-code
$ pip install -r requirments.txt
$ python app.py
```
