from typing import Union

import eth_account
from brownie.account import Account, Accounts, LocalAccount

from .web3 import web3


class VoterAccount(LocalAccount):

    def __init__(self, data, address: str, account: Account, priv_key: Union[int, bytes, str]):
        """Init."""
        self.data = data
        super().__init__(address, account, priv_key)

class VoterAccounts(Accounts):

    def add(self, data, private_key: Union[int, bytes, str] = None) -> "VotingAccount":
        """
        Create a new ``VotingAccount`` instance and appends it to the container.

        When the no private key is given, a mnemonic is also generated and outputted.

        Arguments
        ---------
        private_key : int | bytes | str, optional
            Private key of the account. If none is given, one is randomly generated.

        Returns
        -------
        VotingAccount
        """
        if private_key is None:
            w3account, mnemonic = eth_account.Account.create_with_mnemonic()
            print(f"mnemonic: '{color('bright cyan')}{mnemonic}{color}'")
        else:
            w3account = web3.eth.account.from_key(private_key)

        if w3account.address in self._accounts:
            return self.at(w3account.address)

        account = VoterAccount(data, w3account.address, w3account, w3account.key)
        self._accounts.append(account)

        return account
