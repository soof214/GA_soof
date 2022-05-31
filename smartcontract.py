from datetime import date
from encodings import utf_8
import hashlib
import json
from os import access
from time import time
import pandas as pd




# create first block of blockchain, the 'genesis block': https://medium.com/coinmonks/python-tutorial-build-a-blockchain-713c706f6531
class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        self.new_block(previous_hash="Account information Mike.", proof=100)

# Create a new block listing key/value pairs of block information in a JSON object. Reset the list of pending transactions & append the newest block to the chain.

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)

        return block


#Search the blockchain for the most recent block.

    @property
    def last_block(self):
 
        return self.chain[-1]

# add user information to the blockchain
    def contact_information(self, name, gender, relationship, access):
        transaction = {
            'name': name,
            'gender': gender,
            'relationship category': relationship, 
            'access': access
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

# Add a transaction with relevant info to the 'blockpool' - list of pending tx's. 

    def new_transaction(self, sender, recipient, amount, date):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'photo': amount, 
            'date': date,
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

# receive one block. Turn it into a string, turn that into Unicode (for hashing). Hash with SHA256 encryption, then translate the Unicode into a hexidecimal string.

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

blockchain = Blockchain()
u1=blockchain.contact_information('Emma', 'female', 'ex-girlfriend', True)
u2=blockchain.contact_information('Amber', 'female', 'ex-girlfriend', True)
u3=blockchain.contact_information('Mark', 'male', 'business', False)
u4=blockchain.contact_information('Claire', 'female', 'ex-girlfriend', True)
u5=blockchain.contact_information('Sara', 'female', 'co-worker', False)
u6=blockchain.contact_information('Marcus', 'male', 'friend', False)
u7=blockchain.contact_information('George', 'male', 'soccer-coach', False)
u8=blockchain.contact_information('Jordan', 'male', 'friend', False)
blockchain.new_block(1)


#add transactions to second block
t1 = blockchain.new_transaction("Emma", "Mike", '1', '20/09/2018')
t2 = blockchain.new_transaction("Mike", "Emma", '2', '21/09/2018')
t3 = blockchain.new_transaction("Mike", "Emma", '1', '13/10/2018')
t4 = blockchain.new_transaction("Mike", "Emma", '2', '14/10/2018')
t5 = blockchain.new_transaction("Emma", "Mike", '3', '15/12/2018')
t6 = blockchain.new_transaction("Emma", "Mike", '1', '6/01/2019')
t7 = blockchain.new_transaction("Mike", "Emma", '1', '17/02/2019')
t8 = blockchain.new_transaction("Mike", "Claire", '1', '03/03/2019')
t9 = blockchain.new_transaction("Emma", "Mike", '2', '05/03/2019')
t10 = blockchain.new_transaction("Emma", "Mike", '2', '06/03/2019')
t11 = blockchain.new_transaction("Mike", "Emma", '3', '07/03/2019')
t12 = blockchain.new_transaction("Emma", "Mike", '2', '08/04/2019')
t13 = blockchain.new_transaction("Mike", "Emma", '1', '23/05/2019')
t14 = blockchain.new_transaction("Mike", "Claire", '1', '26/06/2019')
t15 = blockchain.new_transaction("Claire", "Mike", '1', '26/06/2019')
blockchain.new_block(2)

t16 = blockchain.new_transaction("Mike", "Claire", '2', '2/08/2019')
t17 = blockchain.new_transaction("Claire", "Mike", '1', '4/08/2019')
t18 = blockchain.new_transaction("Claire", "Mike", '3', '7/08/2019')
t19 = blockchain.new_transaction("Claire", "Mike", '3', '9/08/2019')
t20 = blockchain.new_transaction("Mike", "Claire", '2', '2/09/2019')
t21 = blockchain.new_transaction("Mike", "Claire", '2', '26/09/2019')
t22 = blockchain.new_transaction("Mike", "Claire", '3', '26/09/2019')
t23 = blockchain.new_transaction("Claire", "Mike", '1', '26/09/2019')
t24 = blockchain.new_transaction("Mike", "Claire", '1', '4/10/2019')
t25 = blockchain.new_transaction("Claire", "Mike", '1', '4/10/2019')
t26 = blockchain.new_transaction("Claire", "Mike", '1', '5/10/2019')
t27 = blockchain.new_transaction("Mike", "Claire", '2', '7/10/2019')
t28 = blockchain.new_transaction("Mike", "Claire", '1', '18/10/2019')
t29 = blockchain.new_transaction("Claire", "Mike", '1', '18/10/2019')
t30 = blockchain.new_transaction("Claire", "Mike", '1', '18/10/2019')
t31 = blockchain.new_transaction("Mike", "Claire", '1', '18/10/2019')
blockchain.new_block(3)

t32 = blockchain.new_transaction("Mike", "Amber", '1', '2/03/2020')
t33 = blockchain.new_transaction("Amber", "Mike", '1', '5/03/2020')
t34 = blockchain.new_transaction("Amber", "Mike", '2', '7/04/2020')
t35 = blockchain.new_transaction("Mike", "Amber", '1', '9/04/2020')
t36 = blockchain.new_transaction("Mike", "Amber", '2', '13/04/2020')
t37 = blockchain.new_transaction("Mike", "Amber", '2', '26/05/2020')
t38 = blockchain.new_transaction("Amber", "Mike", '1', '26/05/2020')
t39 = blockchain.new_transaction("Mike", "Amber", '1', '28/07/2020')
t40 = blockchain.new_transaction("Amber", "Mike", '3', '29/07/2020')
t41 = blockchain.new_transaction("Mike", "Amber", '1', '4/08/2020')
t42 = blockchain.new_transaction("Mike", "Amber", '2', '5/08/2020')
t43 = blockchain.new_transaction("Amber", "Mike", '2', '7/08/2020')
t44 = blockchain.new_transaction("Amber", "Mike", '1', '19/09/2020')
t45 = blockchain.new_transaction("Amber", "Mike", '2', '19/09/2020')
t46 = blockchain.new_transaction("Mike", "Amber", '1', '23/09/2020')
t47 = blockchain.new_transaction("Amber", "Mike", '3', '23/10/2020')
blockchain.new_block(4)

#create json file, store data from blocks here for further processing
data = blockchain.chain 
with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

#Convert the column 'transactions' into seperate column, display in panda's dataframe: https://www.geeksforgeeks.org/converting-nested-json-structures-to-pandas-dataframes/ 
df = pd.json_normalize(data,record_path=['transactions'], meta=[
                  'timestamp', 'proof'])

#split the data structure into contact information and transactions
#texting information
df_transactions = df.tail(45)
df_transactions = df_transactions.drop(['name', 'gender', 'relationship category', 'access'], axis=1)

#contact information
df_contacts = df.head(7)
df_contacts = df_contacts.drop(['sender', 'recipient', 'photo', 'date'], axis=1)
print(df_contacts)

#filter messages per contact, check if they still have access

#FUNCTIE 1: ZIE GEGEVENS + BERICHT GESCHIEDENIS GEKOZEN CONTACT
#Kan/moet dit ook in een functie misschien?
name = str(input('Enter contact: '))
select_transaction = df_transactions.loc[df_transactions['sender'] == name]
select_contact = df_contacts.loc[df['name'] == name].copy()
print ('Texting log: ', select_transaction, 
'Contact information: ', select_contact) #kan dit ook op aparte regel want ziet er beetje rommelig uit als je hem nu print.

# FUNCTIE 2: BEVESTIG DAT DEZE NAAM GEBLOCKED MOET WORDEN, VERANDER IN ACCESS COLUMN VOOR DEZE NAAM DE WAARDE TRUE NAAR FALSE

#hierboven kies je een naam, waarvan de bericht geschiedenis geprint wordt. Dan ziet dus de user (wij), van he, zij heeft nog toegang tot mijn contacten (Access = True), dat is niet goed
# Deze functie vraagt dus eerst of de toegang, van boven gedefinieerde persoon, geblokkeerd moet worden. 
block = str(input('Confirm restricting this contact from seeing your photos? ')) 
#nu moet hier een functie die, op basis van de naam die eerder opgegeven is, de waarde in de column 'Access', van True naar False verandert. 
def switch_access (name):
        if block == 'yes':
            df_contacts.loc[df_contacts["access"] == True, False]
        print(df_contacts)

switch_access(name)

# FUNCTIE 3: SUGGESTIE 
#selecteer een contact uit de lijst
#conditional statement:
# is het laatste bericht langer dan 3 maanden geleden verstuurd? 
# if true -> print iets in de trant van 'Je hebt al zolang niet met deze persoon gepraat, deze heeft nog wel toegang tot fotos dat is balen'
    # if true -> deze persoon heeft nog wel toegang tot je fotos
        # zelfde blokkeer functie als hierboven 
# if false -> print gewoon berichten geschiedenis of iets van 'open messages' voor de leuk 

#dashboard ?
