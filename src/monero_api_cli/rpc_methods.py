from . import functions


rpc_methods = { "help": functions.help,
                #//////JSON RPC Methods:
                #"get_block_count": ,
                #"on_get_block_hash": ,
                #"get_block_template": ,
                #"submit_block": ,
                #"generateblocks": ,
                #"get_last_block_header": ,
                #"get_block_header_by_hash": ,
                #"get_block_header_by_height": ,
                #"get_block_headers_range": ,
                #"get_block": ,
                #"get_connections": ,
                "get_info": functions.get_info
                #"hard_fork_info": ,
                #"set_bans": ,
                #"get_bans": ,
                #"banned": ,
                #"flush_txpool": ,
                #"get_output_histogram": ,
                #"get_version": ,
                #"get_coinbase_tx_sum": ,
                #"get_fee_estimate": ,
                #"get_alternate_chains": ,
                #"relay_tx": ,
                #"sync_info": ,
                #"get_txpool_backlog": ,
                #"get_output_distribution": ,
                #"get_miner_data": ,
                #"prune_blockchain": ,
                #"calc_pow": ,
                #"flush_cache": ,
                #"add_aux_pow": ,
                #//////Other RPC Methods: ,
                #"/get_height": ,
                #"/get_blocks.bin": ,
                #"/get_blocks_by_height.bin": ,
                #"/get_hashes.bin": ,
                #"/get_o_indexes.bin": ,
                #"/get_outs.bin": ,
                #"/get_transactions": ,
                #"/get_alt_blocks_hashes": ,
                #"/is_key_image_spent": ,
                #"/send_raw_transaction": ,
                #"/start_mining": ,
                #"/stop_mining": ,
                #"/mining_status": ,
                #"/save_bc": ,
                #"/get_peer_list": ,
                #"/set_log_hash_rate": ,
                #"/set_log_level": ,
                #"/set_log_categories": ,
                #"/set_bootstrap_daemon": ,
                #"/get_transaction_pool": ,
                #"/get_transaction_pool_hashes.bin": ,
                #"/get_transaction_pool_stats": ,
                #"/stop_daemon": ,
                #"/get_info": ,
                #"/get_limit": ,
                #"/set_limit": ,
                #"/out_peers": ,
                #"/in_peers": ,
                #"/get_net_stats": ,
                #"/start_save_graph": ,
                #"/stop_save_graph": ,
                #"/get_outs": ,
                #"/update": ,
                #"/pop_blocks": 
                }

    
    
    
    
    
    
    
    
    
    
    
