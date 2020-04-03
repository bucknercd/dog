#!/bin/bash

mongod&
sleep 15
mongo < create_admin.js
echo -e "\nCreated admin db user.\n"
sleep 5
pkill mongod
echo -e "\nMongo daemon killed.\n"
sleep 10
mongod --bind_ip_all --port 10000 --auth
echo -e "\nMongo daemon restarted with auth.\n"
