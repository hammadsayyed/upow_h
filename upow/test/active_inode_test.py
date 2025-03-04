import asyncio
import datetime
import decimal
from decimal import Decimal
from os import environ
from time import perf_counter

from upow.constants import SMALLEST
from upow.database import Database
from upow.manager import get_block_reward, get_inode_rewards
from upow.upow_transactions import CoinbaseTransaction, TransactionOutput


async def measure_function_time(func, *args, **kwargs):
    start_time = perf_counter()
    result = await func(*args, **kwargs)
    end_time = perf_counter()
    duration = end_time - start_time
    return result, duration


async def inode_reward_test(block_no):
    database: Database = await Database.create(
        user=environ.get("UPOW_DATABASE_USER", "upow"),
        password=environ.get("UPOW_DATABASE_PASSWORD", ""),
        database=environ.get("UPOW_DATABASE_NAME", "upow"),
        host=environ.get("UPOW_DATABASE_HOST", None),
        ignore=True,
    )
    # decimal.getcontext().prec = 9

    print("\nPerformance Test Results:")
    print("-" * 50)

    # Test original function
    active_inodes, time1 = await measure_function_time(
        database.get_active_inodes, check_pending_txs=True
    )
    print(f"Original get_active_inodes took: {time1:.3f} seconds")

    # Test optimized function
    active_inodes2, time2 = await measure_function_time(
        database.get_active_inodes2, check_pending_txs=True
    )
    print(f"Optimized get_active_inodes2 took: {time2:.3f} seconds")

    # Calculate improvement
    improvement = ((time1 - time2) / time1) * 100
    print(f"\nPerformance improvement: {improvement:.2f}%")

    print("\nResults Comparison:")
    print("-" * 50)
    print("Original active_inodes:", active_inodes)
    print("\nOptimized active_inodes2:", active_inodes2)

    block_reward = get_block_reward(block_no)
    print("\nReward Calculations:")
    print("-" * 50)
    print("block_reward:", block_reward)

    miner_reward, inode_rewards = get_inode_rewards(
        block_reward, active_inodes, block_no=39000
    )
    miner_reward2, inode_rewards2 = get_inode_rewards(
        block_reward, active_inodes2, block_no=39000
    )

    print("\nRewards Comparison:")
    print("-" * 50)
    print("Original miner_reward:", miner_reward)
    print("Optimized miner_reward2:", miner_reward2)
    print(
        "Original inode_rewards:",
        [reward for inode_address, reward in inode_rewards.items()],
    )
    print(
        "Optimized inode_rewards2:",
        [reward for inode_address, reward in inode_rewards2.items()],
    )

    # Verify results match
    rewards_match = sorted([reward for _, reward in inode_rewards.items()]) == sorted(
        [reward for _, reward in inode_rewards2.items()]
    )
    print("\nValidation:")
    print("-" * 50)
    print(f"Results match: {'Yes' if rewards_match else 'No'}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(inode_reward_test(395863))
