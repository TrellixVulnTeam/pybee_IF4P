# -*- coding: utf-8 -*-

from pybee import path
from pybee import compress
from pybee import shell
from pybee import download
from pybee import sed
from pybee import awk
from pybee import git
from pybee import pip
from pybee import importutil
from pybee import netstat
from pybee import springboot
from pybee import iptables
from pybee import network
from pybee import firewalld
from pybee import ask
from pybee import user

from datetime import datetime

net = netstat

__version__ = '0.1.0'

def get_date_time(dt, fmt='%Y-%m-%d %H:%M:%S'):
	return dt.strftime(fmt)

def get_curr_date_time(fmt='%Y-%m-%d %H:%M:%S'):
	d = datetime.now()
	return get_date_time(d, fmt)
