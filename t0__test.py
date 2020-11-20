from dataclasses import asdict, dataclass

import toml


@dataclass
class Config:
    @dataclass
    class Account:
        @dataclass
        class Tx:
            to_address: str
            value: int

        from_address: str
        private_key: str
        txs: list[Tx]

    accounts: list[Account]
    gas_price: int


config = Config(
    gas_price=777,
    accounts=[
        Config.Account(
            from_address="0x111",
            private_key="secret",
            txs=[
                Config.Account.Tx(to_address="a1", value=2),
                Config.Account.Tx(to_address="a2", value=3),
            ],
        ),
        Config.Account(
            from_address="0x222",
            private_key="secret",
            txs=[
                Config.Account.Tx(to_address="a3", value=4),
                Config.Account.Tx(to_address="a4", value=5),
            ],
        ),
    ],
)

print(asdict(config))

res = toml.dumps(asdict(config))
print(res)
