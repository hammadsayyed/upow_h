import asyncio

from icecream import ic

from upow.node.nodes_manager import NodeInterface

_print = ic


async def get_miner_details(start_block, remote_node_url, local_node_url):
    node_interface = NodeInterface(remote_node_url)
    local_interface = NodeInterface(local_node_url)

    offset, limit = start_block, 1000
    # while True:
    local_block_miner_address = {}
    remote_block_miner_address = {}
    remote_blocks = await node_interface.get_blocks(offset, limit)
    local_blocks = await local_interface.get_blocks(offset, limit)
    for n, local_block in enumerate(local_blocks):
        print(local_block["block"]["id"], local_block["block"]["address"], remote_blocks[n]["block"]["id"],
              remote_blocks[n]["block"]["address"])
        key = local_block["block"]["address"]
        remote_key = remote_blocks[n]["block"]["address"]
        local_block_miner_address[key] = local_block_miner_address.get(key, 0) + 1
        remote_block_miner_address[remote_key] = remote_block_miner_address.get(remote_key, 0) + 1

    # local_block_miner_address_sorted = {k: v for k, v in sorted(local_block_miner_address.items(), key=lambda item: item[1])}
    sorted_items = sorted(local_block_miner_address.items(), key=lambda item: item[1])

    # Convert the sorted items back to a dictionary (if needed)
    sorted_dict = dict(sorted_items)

    # local_block_miner_address_sorted = dict(sorted(local_block_miner_address.items(), key=lambda item: item[1]))
    # remote_block_miner_address_sorted = dict(sorted(remote_block_miner_address.items(), key=lambda item: item[1]))
    common_keys = remote_block_miner_address.keys() & local_block_miner_address.keys()
    # _print(common_keys)
    _print(sorted_dict)
    # _print(remote_block_miner_address_sorted)

loop = asyncio.get_event_loop()
loop.run_until_complete(get_miner_details(164501, 'https://api.upow.ai', 'http://37.27.60.116:3706',))

