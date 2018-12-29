"""#Python 3.7.1 Blockchain by Sam Henry Larsen"""
import datetime
import hashlib
import sys

print("Welcome!\n")

print("To start the blockchain enter the following inputs\n")

difficulty = input("Enter the difficulty (1-16): ")

if int(difficulty) > 16:
    print("\nCAN NOT COMPLY DIFFICULTY SET TOO HIGH!")
    sys.exit()
elif int(difficulty) < 0:
    print("\nCAN NOT COMPLY DIFFICULTY IS A NEGATIVE!")
    sys.exit()

length = input("\nEnter the amount of blocks you wish the blockchain to be (1-16): ")

if int(length) > 16:
    print("\nCAN NOT COMPLY BLOCKCHAIN LENGTH TOO LONG!")
    sys.exit()
elif int(length) < 0:
    print("\nCAN NOT COMPLY BLOCKCHAIN LENGTH IS A NEGATIVE!")
    sys.exit()


class Block:
    blockNo = 0
    data = None
    next = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNo).encode('utf-8')
            )
        return h.hexdigest()

    def __str__(self):
        return str(self.data) + "\nHash: " + str(self.hash()) + \
               "\nHashes: " + str(self.nonce) + "\n----------------------------------------"


class Blockchain:

    diff = int(difficulty)
    maxNonce = 2**32
    target = 2 ** (256-diff)

    block = Block("The genesis block has been created!")
    dummy = head = block

    def add(self, block):

        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for i in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1


blockchain = Blockchain()

print("\n")
print(blockchain.head)

for n in range(int(length)):
    blockchain.mine(Block("Block " + str(n+1)))

while blockchain.head is not None:
    blockchain.head = blockchain.head.next
print("\n")
