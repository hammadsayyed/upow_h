import asyncio

from icecream import ic

from upow.node.nodes_manager import NodeInterface

# print = ic
async def fork_detect(last_block_id, remote_node_url, local_node_url):
    next_block_id = last_block_id + 1
    # starting_from = next_block_id = await db.get_next_block_id()
    node_interface = NodeInterface(remote_node_url)
    local_interface = NodeInterface(local_node_url)
    local_cache = None
    # if last_block != {} and last_block["id"] > 500:
    if last_block_id > 500:
        remote_last_block = (await node_interface.get_block(next_block_id - 1))["block"]
        # if remote_last_block["hash"] != last_block["hash"]:
        print(remote_last_block["hash"])
        offset, limit = next_block_id - 500, 500
        remote_blocks = await node_interface.get_blocks(offset, limit)
        local_blocks = await local_interface.get_blocks(offset, limit)
        # local_blocks = await db.get_blocks(offset, limit)
        local_blocks = local_blocks[: len(remote_blocks)]
        local_blocks.reverse()
        remote_blocks.reverse()
        print(len(remote_blocks), len(local_blocks))
        for n, local_block in enumerate(local_blocks):
            print(local_block["block"]["id"], local_block["block"]["hash"], remote_blocks[n]["block"]["id"],
                  remote_blocks[n]["block"]["hash"])
            if local_block["block"]["hash"] == remote_blocks[n]["block"]["hash"]:
                print(local_block, remote_blocks[n])
                last_common_block = local_block["block"]["id"]
                local_cache = local_blocks[:n]
                local_cache.reverse()
                print('last_common_block', last_common_block)
                # await db.remove_blocks(last_common_block + 1)
                break

last_block = {
      "id": 167387,
      "hash": "15800dadd27ba3c4a8ff8c401848db69d76926ec83a3ff8dfa490a7c425421c9",
      "content": "0264ddfef0917d51a87068e10ad51a4a64542706abd2ab24d005b035815800dadd2a5ee03596d431453cbaaba2173a0a352875e5ee7427de20e3108f71b1280f86b4f1d748b4d8e6ab1be758e651a8c56a40ee7fa87ae97fdf61c0523febc0e8ee90f90b8a6662009cd90329",
      "address": "Db2fBYYCyk39xyjLa6BT4kjGAP7MZ5B7RrC8rqz7QqF8w",
      "random": 688118172,
      "difficulty": 9.8,
      "reward": 6.0,
      "timestamp": 1720323065
    }
loop = asyncio.get_event_loop()
loop.run_until_complete(fork_detect(164900, 'https://api.upow.ai', 'http://37.27.60.116:3706',))
