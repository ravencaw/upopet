#!/bin/bash

sudo systemctl stop odoo && sudo service postgresql restart && sudo systemctl start odoo