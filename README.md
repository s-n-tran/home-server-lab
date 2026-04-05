Overview:
I built a web server hosted on an Ubuntu virtual machine. I configured SSH with key-based authentication and deployed a Dockerised Python web service served on nginx. 
Architecture:
Client --> nginx (port 80) --> Docker container (port 5000) --> Python App
Technology and tools:
Ubuntu Server (VM)
VirtualBox
SSH (OpenSSH key-based authentication)
UFW (firewall)
nginx
Docker
Python

Instructions:
docker build -t myapp .
docker run -d -p 5000:5000 myapp

Learning lessons:
Difference between NAT and bridged networking
Reverse proxies
debugging service failures
How containers isolate applications
