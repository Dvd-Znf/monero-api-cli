from prompt_toolkit.completion import WordCompleter
from prompt_toolkit import PromptSession
from .version import __version__
from prompt_toolkit.styles import Style

help_methods = {
    "help": "Print help information regarding a command\nIf no command is specified, will enter read-eval-print loop (REPL)\nInputs: RPC_Method/Command\nOutputs: help information\n",
    "get_info": "Retrieve general information about the state of your node and the network.\nInputs: None\nOutputs: See get_info_output\n",
    #
    "get_info_output": "adjusted_time - unsigned int; Current time approximated from chain data, as Unix time.\n"+
    "alt_blocks_count - unsigned int; Number of alternative blocks to main chain.\n"+
    "block_size_limit - unsigned int; Backward compatibility, same as block_weight_limit, use that instead\n"+
    "block_size_median - unsigned int; Backward compatibility, same as block_weight_median, use that instead\n"+
    "block_weight_limit - unsigned int; Maximum allowed adjusted block size based on latest 100000 blocks\n"+
    "block_weight_median - unsigned int; Median adjusted block size of latest 100000 blocks\n"+
    "bootstrap_daemon_address - string; Bootstrap node to give immediate usability to wallets while syncing by proxying RPC to it. (Note: the replies may be untrustworthy).\n"+
    "busy_syncing - boolean; States if new blocks are being added (true) or not (false).\n"+
    "credits - unsigned int; If payment for RPC is enabled, the number of credits available to the requesting client. Otherwise, 0.\n"+
    "cumulative_difficulty - unsigned int; Least-significant 64 bits of the 128-bit cumulative difficulty.\n"+
    "cumulative_difficulty_top64 - unsigned int; Most-significant 64 bits of the 128-bit cumulative difficulty.\n"+
    "database_size - unsigned int; The size of the blockchain database, in bytes.\n"+
    "difficulty - unsigned int; Least-significant 64 bits of the 128-bit network difficulty.\n"+
    "difficulty_top64 - unsigned int; Most-significant 64 bits of the 128-bit network difficulty.\n"+
    "free_space - unsigned int; Available disk space on the node.\n"+
    "grey_peerlist_size - unsigned int; Grey Peerlist Size\n"+
    "height - unsigned int; Current length of longest chain known to daemon.\n"+
    "height_without_bootstrap - unsigned int; Current length of the local chain of the daemon.\n"+
    "incoming_connections_count - unsigned int; Number of peers connected to and pulling from your node.\n"+
    "mainnet - boolean; States if the node is on the mainnet (true) or not (false).\n"+
    "nettype - string; Network type (one of mainnet, stagenet or testnet).\n"+
    "offline - boolean; States if the node is offline (true) or online (false).\n"+
    "outgoing_connections_count - unsigned int; Number of peers that you are connected to and getting information from.\n"+
    "rpc_connections_count - unsigned int; Number of RPC client connected to the daemon (Including this RPC request).\n"+
    "stagenet - boolean; States if the node is on the stagenet (true) or not (false).\n"+
    "start_time - unsigned int; Start time of the daemon, as UNIX time.\n"+
    "status - string; General RPC error code. \"OK\" means everything looks good.\n"+
    "synchronized - boolean; States if the node is synchronized (true) or not (false).\n"+
    "target - unsigned int; Current target for next proof of work.\n"+
    "target_height - unsigned int; The height of the next block in the chain.\n"+
    "testnet - boolean; States if the node is on the testnet (true) or not (false).\n"+
    "top_block_hash - string; Hash of the highest block in the chain.\n"+
    "top_hash - string; If payment for RPC is enabled, the hash of the highest block in the chain. Otherwise, empty.\n"+
    "tx_count - unsigned int; Total number of non-coinbase transaction in the chain.\n"+
    "tx_pool_size - unsigned int; Number of transactions that have been broadcast but not included in a block.\n"+
    "untrusted - boolean; States if the result is obtained using the bootstrap mode, and is therefore not trusted (true), or when the daemon is fully synced and thus handles the RPC locally (false)\n"+
    "update_available - boolean; States if a newer Monero software version is available.\n"+
    "version - string; The version of the Monero software the node is running.\n"+
    "was_bootstrap_ever_used - boolean; States if a bootstrap node has ever been used since the daemon started.\n"+
    "white_peerlist_size - unsigned int; White Peerlist Size\n"+
    "wide_cumulative_difficulty - Cumulative difficulty of all blocks in the blockchain as a hexadecimal string representing a 128-bit number.\n"+
    "wide_difficulty - string; Network difficulty (analogous to the strength of the network) as a hexadecimal string representing a 128-bit number.\n",
    "exit": "exit the cli | Press Ctrl + C to exit help",
    #
    "version": "Print curent version\n",
}

style = Style.from_dict({
    # User input (default text).
    '':          '#ff0066',

    # Prompt.
    'prompt':           'ansicyan underline',
    'afterprompt':      '#ff0066 nounderline',
})

message = [
    ('class:prompt', 'help'),
    ('class:afterprompt', ': '),
]

cli_completer = WordCompleter(['get_info', 'get_info_output', 'exit', 'version', 'help'])
session = PromptSession()

def helpcli(additional_args=None):
    if additional_args != None:
        if additional_args in help_methods:
            print(help_methods[additional_args])
        else:
            print(additional_args + " is not known")
        return
    while True:
        try:
            user_input = session.prompt(message, style=style, completer=cli_completer) 
            
            #print(f"Logic for: {user_input}")
            if user_input in help_methods:
                print(help_methods[user_input])
            elif len(user_input) > 0 and not str.isspace(user_input):
                print(user_input + " is not known")
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt. Exiting the help CLI.")
            break
        except EOFError:
            print("\nEOF (Ctrl+D) detected. Exiting the help CLI.")
            break
