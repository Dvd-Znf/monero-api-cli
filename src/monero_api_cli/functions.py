import requests
import json
import re
from .help import helpcli

def ip_address_validation(daemon_address):
    ipv4_pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    port_pattern = r'^[1-9]\d{0,4}$|0$'
    domain_pattern = re.compile(
    r'^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|'
    r'([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|'
    r'([a-zA-Z0-9][-_.a-zA-Z0-9]{0,61}[a-zA-Z0-9]))\.'
    r'([a-zA-Z]{2,13}|[a-zA-Z0-9-]{2,30}.[a-zA-Z]{2,3})$'
    )

    if re.match(ipv4_pattern,daemon_address):
        return daemon_address, "18081"
    if re.match(port_pattern,daemon_address):
        return "127.0.0.1", daemon_address
    if domain_pattern.match(daemon_address):
        return daemon_address, "18080"
    if len((daemon_address.split(":"))) != 2:
        raise ValueError("Invalid input format. Please use [IPv4 address]:[Port number] format.")
    address, port = daemon_address.split(":")
    if not re.match(ipv4_pattern, address):
        raise ValueError("Invalid IPv4 address. Please use a valid IPv4 address.")
    if not re.match(port_pattern, port):
        raise ValueError("Invalid port number. Please use a valid port number (1-65535).")
    return address, port

def help(address, port, additional_args=None):
    helpcli(additional_args)

def get_info(address, port):
    print("Running get_info")
    url = "http://" + address + ":" + port + "/json_rpc"
    headers = {"Content-Type": "application/json"}
    data = {
        "jsonrpc": "2.0",
        "id": "0",
        "method": "get_info"
    }
    try:
        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            result = response.json()["result"]
            formatted_result = json.dumps(result, indent=4)
            #print("Response:\n", formatted_result)
            print("Information:")
            print("Adjusted Time:", result["adjusted_time"])
            print("Alt Blocks Count:", result["alt_blocks_count"])
            print("Block Size Limit:", result["block_size_limit"])
            print("Block Size Median:", result["block_size_median"])
            print("Block Weight Limit:", result["block_weight_limit"])
            print("Block Weight Median:", result["block_weight_median"])
            print("Bootstrap Daemon Address:", result["bootstrap_daemon_address"])
            print("Busy Syncing:", result["busy_syncing"])
            print("Credits:", result["credits"])
            print("Cumulative Difficulty:", result["cumulative_difficulty"])
            print("Cumulative Difficulty (Top 64 bits):", result["cumulative_difficulty_top64"])
            print("Database Size:", result["database_size"])
            print("Difficulty:", result["difficulty"])
            print("Difficulty (Top 64 bits):", result["difficulty_top64"])
            print("Free Space:", result["free_space"])
            print("Grey Peerlist Size:", result["grey_peerlist_size"])
            print("Height:", result["height"])
            print("Height Without Bootstrap:", result["height_without_bootstrap"])
            print("Incoming Connections Count:", result["incoming_connections_count"])
            print("Is Mainnet:", result["mainnet"])
            print("Nettype:", result["nettype"])
            print("Offline:", result["offline"])
            print("Outgoing Connections Count:", result["outgoing_connections_count"])
            print("Restricted:", result["restricted"])
            print("RPC Connections Count:", result["rpc_connections_count"])
            print("Is Stagenet:", result["stagenet"])
            print("Start Time:", result["start_time"])
            print("Status:", result["status"])
            print("Synchronized:", result["synchronized"])
            print("Target:", result["target"])
            print("Target Height:", result["target_height"])
            print("Is Testnet:", result["testnet"])
            print("Top Block Hash:", result["top_block_hash"])
            print("Top Hash:", result["top_hash"])
            print("Transaction Count:", result["tx_count"])
            print("Transaction Pool Size:", result["tx_pool_size"])
            print("Untrusted:", result["untrusted"])
            print("Update Available:", result["update_available"])
            print("Version:", result["version"])
            print("Was Bootstrap Ever Used:", result["was_bootstrap_ever_used"])
            print("White Peerlist Size:", result["white_peerlist_size"])
            print("Wide Cumulative Difficulty:", result["wide_cumulative_difficulty"])
            print("Wide Difficulty:", result["wide_difficulty"])
        else:
            print("Request failed with status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {str(e)}")
