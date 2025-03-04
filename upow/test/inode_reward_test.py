import asyncio
import datetime
import decimal
from decimal import Decimal
from os import environ

from upow.constants import SMALLEST
from upow.database import Database
from upow.manager import get_block_reward, get_inode_rewards
from upow.upow_transactions import CoinbaseTransaction, TransactionOutput


async def inode_reward_test(block_no, active_inodes_json):
    # database: Database = await Database.create(
    #     user=environ.get('UPOW_DATABASE_USER', 'upow'),
    #     password=environ.get('UPOW_DATABASE_PASSWORD', '12345'),
    #     database=environ.get('UPOW_DATABASE_NAME', 'upow'),
    #     host=environ.get('UPOW_DATABASE_HOST', None),
    #     ignore=True
    # )
    # decimal.getcontext().prec = 9

    # active_inodes = await database.get_active_inodes(check_pending_txs=True)

    # active_inodes = [
    #     {
    #         "wallet": "Dsykm6pDTkD93Mx6fh8RBnXi47p2aWy7aaYNKGawjBPYq",
    #         "power": 122044.1492055,
    #         "registered_at": "2024-04-04T17:11:39",
    #         "emission": Decimal(86.94),
    #         "is_active": True
    #     },
    #     {
    #         "wallet": "DcohkkTbfrkY7ZZZabT2vCX6qagWPaRbxGJtF7m7TZry3",
    #         "power": 9699.34039526,
    #         "registered_at": "2024-04-05T11:40:13",
    #         "emission": Decimal(6.91),
    #         "is_active": True
    #     },
    #     {
    #         "wallet": "DXcFpExVR8ghpNBjY2oPam7nhqK6xrfTDphan5sJLduYm",
    #         "power": 8635.11039526,
    #         "registered_at": "2024-04-11T12:03:33",
    #         "emission": Decimal(6.15),
    #         "is_active": True
    #     }
    # ]       # with accurate_division block 1 inode_rewards [Decimal('2.60820'), Decimal('0.20730'), Decimal('0.18450')]
            # with decimal block 1 inode_rewards [Decimal('2.60820000'), Decimal('0.20730000'), Decimal('0.18450000')]
            # with decimal block 40000 inode_rewards [Decimal('2.60820000'), Decimal('0.20730000'), Decimal('0.18450000')]
            # with decimal block 40000 inode_rewards [Decimal('2.60820000'), Decimal('0.20730000'), Decimal('0.18450000')]

    # active_inodes = [{'wallet': 'Dsykm6pDTkD93Mx6fh8RBnXi47p2aWy7aaYNKGawjBPYq', 'power': Decimal('64825.9'),
    #   'registered_at': datetime.datetime(2024, 4, 4, 17, 11, 39), 'emission': Decimal('87.47'), 'is_active': True},
    #  {'wallet': 'DcohkkTbfrkY7ZZZabT2vCX6qagWPaRbxGJtF7m7TZry3', 'power': Decimal('9173.63'),
    #   'registered_at': datetime.datetime(2024, 4, 5, 11, 40, 13), 'emission': Decimal('12.38'), 'is_active': True}]

  #   active_inodes = [       # Testing node dobby_info
  #   {
  #     "wallet": "Dsykm6pDTkD93Mx6fh8RBnXi47p2aWy7aaYNKGawjBPYq",
  #     "power": 97725.5002055,
  #     "registered_at": "2024-04-04T17:11:39",
  #     "emission": Decimal(92.62),
  #     "is_active": True
  #   },
  #   {
  #     "wallet": "DcohkkTbfrkY7ZZZabT2vCX6qagWPaRbxGJtF7m7TZry3",
  #     "power": 4325.62,
  #     "registered_at": "2024-04-05T11:40:13",
  #     "emission": Decimal(4.10),
  #     "is_active": True
  #   },
  #   {
  #     "wallet": "DXcFpExVR8ghpNBjY2oPam7nhqK6xrfTDphan5sJLduYm",
  #     "power": 3451.5,
  #     "registered_at": "2024-04-11T12:03:33",
  #     "emission": Decimal(3.27),
  #     "is_active": True
  #   }
  # ]
        
        
  #       [
  #   {
  #     "wallet": "Dsykm6pDTkD93Mx6fh8RBnXi47p2aWy7aaYNKGawjBPYq",
  #     "power": 100749.5402055,
  #     "registered_at": "2024-04-04T17:11:39",
  #     "emission": Decimal(90.96),
  #     "is_active": True
  #   },
  #   {
  #     "wallet": "DcohkkTbfrkY7ZZZabT2vCX6qagWPaRbxGJtF7m7TZry3",
  #     "power": 5321.22,
  #     "registered_at": "2024-04-05T11:40:13",
  #     "emission": Decimal(4.80),
  #     "is_active": True
  #   },
  #   {
  #     "wallet": "DXcFpExVR8ghpNBjY2oPam7nhqK6xrfTDphan5sJLduYm",
  #     "power": 4697.1,
  #     "registered_at": "2024-04-11T12:03:33",
  #     "emission": Decimal(4.24),
  #     "is_active": True
  #   }
  # ]

    #     [{
    #   "wallet": "Dsykm6pDTkD93Mx6fh8RBnXi47p2aWy7aaYNKGawjBPYq",
    #   "power": 64825.9,
    #   "registered_at": "2024-04-04T17:11:39",
    #   "emission": Decimal(87.47),
    #   "is_active": True
    # },
    # {
    #   "wallet": "DcohkkTbfrkY7ZZZabT2vCX6qagWPaRbxGJtF7m7TZry3",
    #   "power": 9173.63,
    #   "registered_at": "2024-04-05T11:40:13",
    #   "emission": Decimal(12.38),
    #   "is_active": True
    # }]
    # print('active_inodes', active_inodes)

    block_reward = get_block_reward(block_no)
    print('active_inodes', active_inodes_json)
    miner_reward, inode_rewards = get_inode_rewards(block_reward, active_inodes_json, block_no=block_no)
    print('miner_reward', miner_reward)
    print('inode_rewards', [reward for inode_address, reward in inode_rewards.items()]) #inode_rewards [Decimal('2.62804206'), Decimal('0.37195794')]
    # coinbase_transaction = CoinbaseTransaction('block_hash', 'mineraddress', miner_reward + Decimal(0.000))
    # if inode_rewards:
    #     coinbase_transaction.outputs.extend(
    #         [
    #             TransactionOutput(inode_address, reward)
    #             for inode_address, reward in inode_rewards.items()
    #         ]
    #     )
    # print('decimal.getcontext().prec', decimal.getcontext().prec)

# inode_rewards {'Dsykm6pDTkD93Mx6fh8RBnXi47p2aWy7aaYNKGawjBPYq': Decimal('2.62804206'), 'DcohkkTbfrkY7ZZZabT2vCX6qagWPaRbxGJtF7m7TZry3': Decimal('0.37195794')}


inode_reward_at_48863 = [
        {
            "emission": Decimal(80.65),
            # "inode_reward": "2.41974197",
            "power": 142164.1202055,
            "wallet": "Dsykm6pDTkD93Mx6fh8RBnXi47p2aWy7aaYNKGawjBPYq"
        },
        {
            "emission": Decimal(6.53),
            # "inode_reward": "0.19591959",
            "power": 11515.54067926,
            "wallet": "DcohkkTbfrkY7ZZZabT2vCX6qagWPaRbxGJtF7m7TZry3"
        },
        {
            "emission": Decimal(6.43),
            # "inode_reward": "0.19291929",
            "power": 11336.74039526,
            "wallet": "DXcFpExVR8ghpNBjY2oPam7nhqK6xrfTDphan5sJLduYm"
        },
        {
            "emission": Decimal(6.38),
            # "inode_reward": "0.19141914",
            "power": 11250,
            "wallet": "DyB5CcpfTdY3GyvqZ4M8BqPgtiBkzbYyr7guALpLT1HMJ"
        }
    ]

# go_calc_result_of_inode_reward_at_48863 = inode_rewards [Decimal('2.41974198'), Decimal('0.19591959'), Decimal('0.19291929'), Decimal('0.19141914')]
# decimal_result_of_inode_reward_at_48863 inode_rewards [Decimal('2.41974197'), Decimal('0.19591959'), Decimal('0.19291929'), Decimal('0.19141914')]




loop = asyncio.get_event_loop()
loop.run_until_complete(inode_reward_test(48863, inode_reward_at_48863))