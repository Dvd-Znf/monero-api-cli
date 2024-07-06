# Monero-api-cli       
![GitHub Release](https://img.shields.io/github/v/release/Dvd-Znf/monero-api-cli?include_prereleases&logo=GitHub&label=Latest%20release%3A&color=lightgreen)
![PyPI - Version](https://img.shields.io/pypi/v/monero-api-cli?logo=Python&label=Latest%20PyPi%20version%3A&color=lightyellow)
![AUR Version](https://img.shields.io/aur/version/monero-api-cli?logo=Arch%20Linux&label=Latest%20AUR%20version%3A)
## Cli for interacting with the MoneroDaemon-RPC API       
![Banner](./imgs/Banner.png)    
`monero-api-cli` is a Python cli application meant for remotely interacting with a Monero Daemon via its [RPC API](https://www.getmonero.org/resources/developer-guides/daemon-rpc.html)     
Under the hood it mostly uses the [Prompt-Toolkit module](https://python-prompt-toolkit.readthedocs.io/en/master/) for its [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) interface and [Requests](https://requests.readthedocs.io/en/latest/) for the actual interaction with the API
## Usage:
```
$ monero-api-cli --help
usage: [-h] [-v] [--daemon-address DAEMON_ADDRESS] [--config-file CONFIG_FILE] {help,get_info} ...

Cli for interacting with the MoneroDaemon-RPC API

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --daemon-address DAEMON_ADDRESS
                        Which daemon address to use, format: [IPv4 address]:[Port number]
  --config-file CONFIG_FILE
                        Path to config file

RPC methods:
  {help,get_info}
    help                Help information regarding a command
    get_info            Invoke the get_info RPC method
```
If you call the app with no additional arguments it will enter into a REPL cli mode otherwise it will just take the argument as a RPC method.
### Available RPC Methods/Arguments:
#### help    
![helpimage](./imgs/Screenshot_Help.png)
   
If no additional arguments are passed it will go into REPL mode    
Otherwise it will just take the argument and display the help message associated with it    
#### get_info    
Calls the get_info RPC method         
#### version (REPL only)
Print current version        
#### exit (REPL only)
Exit the cli REPL mode       
You can also use Ctrl+C to exit        
### Available options:
#### -h, --help
Show help message and exits  
#### -v, --version 
Show current version and exit  
#### --daemon-address
Which daemon address to use, format: [IPv4 address]:[Port number]  
#### --config-file
Path for a config file   
Check Config File section for more details         
### Example usage:
![example](./imgs/Screenshot_Usage.png)
## Config File:
Default location for config file is /etc/monero-api-cli/monero-api-cli.config for MacOS/Linux     
And C:\ProgramData\MoneroApiCli\monero-api-cli.confg for Windows                
Example config file located at root of this repo, named `monero-api-config.config`
``` ini 
# Config File INI/TOML like syntax
# Lines starting with # are comments and have their respective default options
[settings]
# Which daemon address to use, format: [IPv4 address]:[Port number]
daemon-address = 127.0.0.1:18081
```
## Dependencies:
Because the app is bundled using pyinstaller dependencies are _not_ required on the binary versions     
The dependencies are only required when working direclty with the source         
Install all python module dependencies with: `pip install -r requirements.txt`        
     
| Name | PyPi Name | What is it used for? |
| ---- | ------- | -------------------- |
| Python | N/A | Necessary for interpreting source code |
| Requests module | `requests` | Used in the implementation of interacting with the API |
| Prompt Toolkit module | `prompt_toolkit` | Used in the implementation of REPL cli mode |
     
## How to install
### From AUR package
If you use Arch Linux you know what to do.     
Here is the link to the AUR package: https://aur.archlinux.org/packages/monero-api-cli
### From PyPi via pip   
`pip install monero-api-cli`     
### From repo:
You can either use the source code with the Python interpretor directly        
Or you could use the provided binary available at `dist/monero-api-cli` for MacOS/Linux and `dist/monero-api-cli.exe` for Windows            
### Step 0:
Clone this repo :P   
``` bash
$ git clone https://github.com/Dvd-Znf/monero-api-cli
```
### Step 1 (With binary):
Use the provided binary         
Dependencies are already bundled in, you dont need to install anything!      
``` bash
$ cd monero-api-cli
$ ./dist/monero-api-cli  # MacOS/Linux     
```
``` PowerShell
PS> ./dist/monero-api-cli.exe # Windows     
```
If you get permisions error add execute permisions with: `chmod +x <path to binary>`   
### Step 1 (From source, recommended for development):   
Make sure you have all dependencies installed       
Then just use the Python interpretor on the `launcher.py` script      
``` bash
$ cd monero-api-cli   
$ python launcher.py     
```
Or you can run the source directly as a module      
``` bash
$ python -m src.monero_api_cli
```
## Why make this from zero when python-monero module already exists?      
1. This is not meant as a replacement for python-monero module!        
Instead, this is an independent cli application for interacting with monerod via its RPC API        
i.e. cli-app & no wallet RPC        
2. This is mostly meant for monero node operators who would like a nice, intuitive and easy way to interact with their daemon    
This is the reason I made this.      
3. python-monero last update to its source code was more than a year ago, even tho it could use some improvements, at least to its docs.     
This is activly developed.      
After first release you may integrate monero-api-cli into whatever you want but thats not my problem/focus.      
## Can't you ssh into your node then just use monerod?      
Some setups require the daemon to be non-interactive       
Also that sound super laaaameeeeeee       
## TODO:    
- Implement `get_connections` RPC Method
- Implement `get_version` RPC Method
- Implement `/get_height` RPC Method
- Implement `/get_net_stats` RPC Method 
### TODO for v1.0.0:       
- Implement more of the API :P     
