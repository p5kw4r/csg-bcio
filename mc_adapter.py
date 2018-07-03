from binascii import hexlify, unhexlify
from mcrpc import RpcClient
from adapter import Adapter
from config import amount, encoding

host = 'localhost'
port = '7324'

# The API credentials for each blockchain are stored in the
# ~/.multichain/[chain-name]/multichain.conf
rpcuser = 'multichainrpc'
rpcpassword = 'GkHfnch8QBgqvZJeMLyb57h42h6TZREr25Uhp5iZ8T2E'

# The private key can be found by running `dumpprivkey [address]` command in
# interactive mode, i.e. `$ multichain-cli [chain-name]`
address = '1RuG62c89Vk1V6psGhtAwywan9mWsvFvBv2cLM'
key = 'VAUWVB6KStqzemdzXqak77cbkaz6tyYyRbcG3pqBcpP2xNFzAvT8bt2E'


class MCAdapter(Adapter):
    client = RpcClient(host, port, rpcuser, rpcpassword)

    @classmethod
    def get_transaction(cls, transaction_hash):
        return cls.client.getrawtransaction(transaction_hash, verbose=1)

    @classmethod
    def extract_data(cls, transaction):
        # workaround needed because potentially multiple output addresses in
        # single transaction (and also potentially multiple data items)
        output = cls.extract_output(transaction, 1)
        return output['data'][0]

    @staticmethod
    def extract_output(transaction, output_index):
        outputs = transaction['vout']
        return outputs[output_index]

    @staticmethod
    def to_text(data_hex):
        data = unhexlify(data_hex)
        return data.decode(encoding=encoding)

    @classmethod
    def create_transaction(cls, text, input_transaction_hash=None):
        data_hex = cls.to_hex(text)
        output = {address: amount}
        transaction_hex = cls.client.createrawsendfrom(
            address,
            output,
            [data_hex])
        return transaction_hex

    @staticmethod
    def to_hex(text):
        data = bytes(text, encoding=encoding)
        return hexlify(data)

    @classmethod
    def sign_transaction(cls, transaction_hex):
        parent_outputs = []
        signed_transaction = cls.client.signrawtransaction(
            transaction_hex,
            parent_outputs,
            [key])
        assert signed_transaction['complete']
        return signed_transaction['hex']

    @classmethod
    def send_raw_transaction(cls, transaction_hex):
        transaction_hash = cls.client.sendrawtransaction(transaction_hex)
        return transaction_hash
