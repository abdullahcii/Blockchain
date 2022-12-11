# hashlib importieren
import hashlib

# Klasse Blockchain
class Blockchain:

    def __init__(self, previous_hash, transactions):
        self.previous_hash = previous_hash
        self.transactions = transactions
        

        self.block_data = "||".join(transactions) + "||" + previous_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
        


t1 = "Anna schickt 1 Coins an Mike"
t2 = "Mike schickt 5.9 Coins an Anna"
t3 = "Michael schickt 0.2 Coins an Mike"

t4 = "Lusi schickt 2.0 Coins an Kadir"
t5 = "Jeremy schickt 9 Coins an Stefan"
t6 = "Luka schickt 1.8 Coins an Stefan"

t7 = "Stefan schickt 2 Coins an Mike"
t8 = "Lusi schickt 6.2 Coins an Luka"
t9 = "Michael schickt 1.1 Coins an to Anna"

# hash Verschlüsselung
block1 = Blockchain("1.Block", [t1, t2, t3])
print(f"Block 1 Daten: {block1.block_data}")
print(f"Block 1 hash: {block1.block_hash}")

block2 = Blockchain("2.Block", [t4, t5, t6])
print(f"Block 2 Daten: {block2.block_data}")
print(f"Block 2 hash: {block2.block_hash}")

block3 = Blockchain("3.Block", [t7, t8, t9])
print(f"Block 3 Daten: {block3.block_data}")
print(f"Block 3 hash: {block3.block_hash}")
