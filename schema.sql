CREATE TABLE IF NOT EXISTS blocks (
	id SERIAL PRIMARY KEY,
	hash CHAR(64) UNIQUE,
	content TEXT NOT NULL,
	address VARCHAR(128) NOT NULL,
	random BIGINT NOT NULL,
	difficulty NUMERIC(3, 1) NOT NULL,
	reward NUMERIC(14, 6) NOT NULL,
	timestamp TIMESTAMP(0)
);

CREATE TABLE IF NOT EXISTS transactions (
	block_hash CHAR(64) NOT NULL REFERENCES blocks(hash) ON DELETE CASCADE,
	tx_hash CHAR(64) UNIQUE,
	tx_hex TEXT,
	inputs_addresses TEXT[],
	outputs_addresses TEXT[],
	outputs_amounts BIGINT[],
	fees NUMERIC(14, 6) NOT NULL
);

CREATE TYPE tx_output AS (
    tx_hash CHAR(64),
    index SMALLINT
);

CREATE TABLE IF NOT EXISTS unspent_outputs (
	tx_hash CHAR(64) REFERENCES transactions(tx_hash) ON DELETE CASCADE,
	index SMALLINT NOT NULL,
	address TEXT NULL,
	is_stake BOOLEAN
);

CREATE TABLE IF NOT EXISTS pending_transactions (
	tx_hash CHAR(64) UNIQUE,
	tx_hex TEXT,
	inputs_addresses TEXT[],
	fees NUMERIC(14, 6) NOT NULL,
	propagation_time TIMESTAMP(0) NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS pending_spent_outputs (
	tx_hash CHAR(64) REFERENCES transactions(tx_hash) ON DELETE CASCADE,
	index SMALLINT NOT NULL
);

CREATE TABLE IF NOT EXISTS inode_registration_output (
    tx_hash CHAR(64) REFERENCES transactions(tx_hash) ON DELETE CASCADE,
    index SMALLINT NOT NULL,
    address TEXT NULL
);

CREATE TABLE IF NOT EXISTS validator_registration_output (
    tx_hash CHAR(64) REFERENCES transactions(tx_hash) ON DELETE CASCADE,
    index SMALLINT NOT NULL,
    address TEXT NULL
);

CREATE TABLE IF NOT EXISTS validators_voting_power (
    tx_hash CHAR(64) REFERENCES transactions(tx_hash) ON DELETE CASCADE,
    index SMALLINT NOT NULL,
    address TEXT NULL
);

CREATE TABLE IF NOT EXISTS delegates_voting_power (
    tx_hash CHAR(64) REFERENCES transactions(tx_hash) ON DELETE CASCADE,
    index SMALLINT NOT NULL,
    address TEXT NULL
);

CREATE TABLE IF NOT EXISTS validators_ballot (
    tx_hash CHAR(64) REFERENCES transactions(tx_hash) ON DELETE CASCADE,
    index SMALLINT NOT NULL,
    address TEXT NULL
);

CREATE TABLE IF NOT EXISTS inodes_ballot (
    tx_hash CHAR(64) REFERENCES transactions(tx_hash) ON DELETE CASCADE,
    index SMALLINT NOT NULL,
    address TEXT NULL
);

CREATE INDEX tx_hash_idx ON unspent_outputs (tx_hash);
CREATE INDEX block_hash_idx ON transactions (block_hash);