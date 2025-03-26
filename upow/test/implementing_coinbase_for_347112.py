import asyncio
from decimal import Decimal
from os import environ

from upow.database import Database
from upow.manager import get_inode_rewards, get_block_reward
from upow.upow_transactions import CoinbaseTransaction, TransactionOutput


async def build_coinbase_tx():
    block_hash = '488ac6552714de5154f4699bc9ef9fc9f88e963e04a0ace4b590fc582493ee15'
    address = 'DdWqu4ygpkPowCtLvb9bgDAHvcpvgh8ygQYSQcmQj6wjx'
    fees = 0
    active_inodes = [
        {
            "wallet": "Dsykm6pDTkD93Mx6fh8RBnXi47p2aWy7aaYNKGawjBPYq",
            "power": 802151.47600970,
            "emission": Decimal("74.24"),
            # "inode_reward": "2.22697730"
        },
        {
            "wallet": "DcohkkTbfrkY7ZZZabT2vCX6qagWPaRbxGJtF7m7TZry3",
            "power": 144313.02199400,
            "emission": Decimal("13.36"),
            # "inode_reward": "0.40075992"
        },
        {
            "wallet": "DXcFpExVR8ghpNBjY2oPam7nhqK6xrfTDphan5sJLduYm",
            "power": 134057.75789684,
            "emission": Decimal("12.41"),
            # "inode_reward": "0.37226277"
        }
    ]
    block_no = 347112
    block_reward = get_block_reward(block_no)
    miner_reward, inode_rewards = get_inode_rewards(block_reward, active_inodes, block_no=block_no)
    coinbase_transaction = CoinbaseTransaction(block_hash, address, miner_reward + fees)
    if inode_rewards:
        coinbase_transaction.outputs.extend(
            [
                TransactionOutput(inode_address, reward)
                for inode_address, reward in inode_rewards.items()
            ]
        )

    print(coinbase_transaction)
    database: Database = await Database.create(
        user=environ.get('UPOW_DATABASE_USER', 'upow'),
        password=environ.get('UPOW_DATABASE_PASSWORD', '12345'),
        database=environ.get('UPOW_DATABASE_NAME', 'upow_local'),
        host=environ.get('UPOW_DATABASE_HOST', None),
        ignore=True
    )
    # block_content = '02b81bacc3b42341c37f8a7f269625be85eb8e31d52ea0dc4069ceb9995488ac652a83cff65faaedfbf91f5f378d557094db3bdd14a3132ab6c3e116c601da2ecf9be3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855388205674c00b32a21bf'
    # random = 3206621875
    # difficulty = Decimal(7.6)
    # content_time = 1728414264
    # await database.add_block(
    #     block_no,
    #     block_hash,
    #     block_content,
    #     address,
    #     random,
    #     difficulty,
    #     block_reward + fees,
    #     content_time,
    # )

    await database.add_transaction(coinbase_transaction, block_hash)
    await database.add_transaction_outputs([coinbase_transaction])

loop = asyncio.get_event_loop()
loop.run_until_complete(build_coinbase_tx())

# [('987fe127525a469c186356fe09a7abdf83cda53444d25e29f1c0e7c31bfa9faa', 0,
#   'DdWqu4ygpkPowCtLvb9bgDAHvcpvgh8ygQYSQcmQj6wjx', False),
#  ('987fe127525a469c186356fe09a7abdf83cda53444d25e29f1c0e7c31bfa9faa', 1,
#   'Dsykm6pDTkD93Mx6fh8RBnXi47p2aWy7aaYNKGawjBPYq', False),
#  ('987fe127525a469c186356fe09a7abdf83cda53444d25e29f1c0e7c31bfa9faa', 2,
#   'DcohkkTbfrkY7ZZZabT2vCX6qagWPaRbxGJtF7m7TZry3', False),
#  ('987fe127525a469c186356fe09a7abdf83cda53444d25e29f1c0e7c31bfa9faa', 3, 'DXcFpExVR8ghpNBjY2oPam7nhqK6xrfTDphan5sJLduYm', False)]

# [('488ac6552714de5154f4699bc9ef9fc9f88e963e04a0ace4b590fc582493ee15',
#   '987fe127525a469c186356fe09a7abdf83cda53444d25e29f1c0e7c31bfa9faa',
#   '0201488ac6552714de5154f4699bc9ef9fc9f88e963e04a0ace4b590fc582493ee150000042a83cff65faaedfbf91f5f378d557094db3bdd14a3132ab6c3e116c601da2ecf9b0400a3e111002b5ab873cd4dc96b7ec03ceb22ae836c0839a092f06aca5d01484b8cc973f835fe040219460d002a7945f1006cc45267be73509550da12e27c14b1ee57a9da08199bedb25c33c4f604d8826302002a2c0cc9a37c7ae46dfb16de4a405b03e0962ef3b7a5653abfe424e3fdb237697204250738020024',
#   [],
#   ['DdWqu4ygpkPowCtLvb9bgDAHvcpvgh8ygQYSQcmQj6wjx',
#    'Dsykm6pDTkD93Mx6fh8RBnXi47p2aWy7aaYNKGawjBPYq',
#    'DcohkkTbfrkY7ZZZabT2vCX6qagWPaRbxGJtF7m7TZry3',
#    'DXcFpExVR8ghpNBjY2oPam7nhqK6xrfTDphan5sJLduYm'],
#   [Decimal('300000000.0'),
#    Decimal('222697730.00000000'),
#    Decimal('40075992.00000000'),
#    Decimal('37226277.00000000')],
#   0)]

