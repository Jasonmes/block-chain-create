#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Jason Mess

"""
Blockchain 类用来管理链条，它能存储交易，加入新块等
"""
import hashlib
import json
from time import time


class Blockchain(object):
    def __init__(self):
        """
        在构造函数里面创建两个表
            一个储存区块链
            一个储存交易
        """

        def __init__(self):
            self.chain = []
            self.current_transaction = []

            # create the genesis block
            self.new_block(previous_hash=1, proof=100)

    """
    字典 -->> 块block结构包含索引index  时间戳timestamp   交易列表transactions   工作量证明proof   前一个区块的hash值
            每个区块都需要经过工作量证明，俗称挖矿
    """

    def new_block(self, proof, previous_hash=None):
        """
        生成新块
        :param self:
        :param prrof:
        :param previous_hash:
        :return:
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])

        }
        # 重制最近的交易表: Reset the current list of transactions
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        生成新的交易，信息将加入到下一个待挖的区块中
        :param self:
        :param sender: 发送者的地址
        :param recipient: 接受者的地址
        :param amount: <int>amount
        :return: <int>The index of the Block that will hold this transaction
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        生成块的吗 SHA-256 hash 值
        我们必须确保字典是有序的, 否则我们将有不一致的哈希
        :param block: <dict> Block
        :return: <str>
        dumps是将dict转化成str格式，loads是将str转化成dict格式。
        dump和load也是类似的功能，只是与文件操作结合起来了
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    """
    实现工作量的证明
    实现一个相似PoW的算法规则如下
    : 寻找一个数P，使得它与前一个区块的proof拼接成的字符串的Hash值以4个0开头。
    """
    def proof_of_work(self, last_proof):
        """
        简单的工作量证明
          - 查找一个P' 使得hash(PP')以4个0开头
          - P 是上一个块的证明，P'是当前的证明
        :param last_proof: <int>
        :return: <int>
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        验证证明: 是否hash(last_proof, proof)以4个0开头
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"




