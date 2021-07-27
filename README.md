# Simple example showing how to communicate between containers

Repository
```
├── client		: to be mounted on client container
│   └── client-udp.py	: "client" of the communication
├── docker-compose.yml	: docker compose file
├── Dockerfile		: docker build context folder
│   └── Dockerfile	: docker image to be used both for server and client
└── server		: to be mounted on server container
    └── server-udp.py	: "server" of the communication
```
