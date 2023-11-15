# import version
import sys
# import json
# import requests
import argparse
# import rpc_methods
# import functions
# import cli
import re
import os
import configparser

from sys import exit
# from os.path import expanduser
from .version import __version__
from .rpc_methods import rpc_methods
from .cli import cli

# home = expanduser("~")
def load_config(config_file_path):
    if not os.path.isfile(config_file_path):
        return None

    config = configparser.ConfigParser()
    config.read(config_file_path)

    return config

def get_default_config_file_path():
    if os.name == 'posix':
        return '/etc/monero-api-cli/monero-api-cli.confg'
    elif os.name == 'nt':
        return 'C:\\ProgramData\\MoneroApiCli\\monero-api-cli.confg'
    else:
        return None
valid_rpc_methods = list(rpc_methods.keys())

parser = argparse.ArgumentParser(description='Cli for interacting with the MoneroDaemon-RPC API')
parser.add_argument("-v", "--version", action="version", version=__version__)
parser.add_argument("--daemon-address", help="Which daemon address to use, format: [IPv4 address]:[Port number]", default="127.0.0.1:18081")
#parser.add_argument("RPC_API_COMMAND", choices=valid_rpc_methods, help="Which RPC Method to use", nargs='*') 
parser.add_argument('--config-file', default=get_default_config_file_path(), help='Path to config file')

subparser = parser.add_subparsers(title='RPC methods', dest='subcommand', help='')
for rpc_method in valid_rpc_methods:
    if rpc_method == "help":
        rpc_parser = subparser.add_parser(rpc_method, help="Help information regarding a command")
        rpc_parser.add_argument("additional_args", nargs='?', help="Additional arguments for the RPC method")
    else:
        rpc_parser = subparser.add_parser(rpc_method, help=f"Invoke the {rpc_method} RPC method")
        rpc_parser.add_argument("additional_args", nargs='?', help="Additional arguments for the RPC method")



args = parser.parse_args()


ipv4_pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
port_pattern = r'^[1-9]\d{0,4}$|0$'
daemon_address = args.daemon_address

config = load_config(args.config_file)

if config:
    #print("Loaded configuration:")
    for key, value in config["settings"].items():
        #print(f"{key} = {value}")
        if key == "daemon-address":
            daemon_address = value

if len((daemon_address.split(":"))) != 2:
    print("Invalid input format. Please use [IPv4 address]:[Port number] format.")
    exit(1)

address, port = daemon_address.split(":")

if not re.match(ipv4_pattern, address):
    print("Invalid IPv4 address. Please use a valid IPv4 address.")

if not re.match(port_pattern, port):
    print("Invalid port number. Please use a valid port number (1-65535).")


if args.subcommand is None :
    print("No additional arguments parsed\nEntering cli mode\n")
    cli(address, port)
    exit(0)
elif (args.subcommand == 'help' and args.additional_args != None):
    rpc_methods[args.subcommand](address, port, args.additional_args)
else :
    rpc_methods[args.subcommand](address, port)
