
#import modules and packages necessary to employ following code:
import time
from time import sleep
import datetime as dt
from datetime import timedelta
import datetime
from datetime import date
from encodings import utf_8
import hashlib
import json
from os import access
from time import time
import pandas as pd

# This code is written from a user POV. In this case, our user is Mike. The contacts in the DF are his, and the text information shows past texts between him 
# and his last three girlfriends. 


# Create a blockchain to safely store information on 
# Create the first block of blockchain, the 'genesis block', code from: https://medium.com/coinmonks/python-tutorial-build-a-blockchain-713c706f6531
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


# Search the blockchain for the most recent block.

    @property
    def last_block(self):
 
        return self.chain[-1]

# Add user information to the blockchain through a function, these are the contacts of our user, Mike.
    def contact_information(self, name, gender, relationship, access):
        transaction = {
            'name': name,
            'gender': gender,
            'relationship category': relationship, 
            'access': access
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

# Add a transaction with relevant information to the 'blockpool' - list of pending transactions. These, in our case, are the texts between Mike and his past girlfriends. 

    def new_transaction(self, sender, recipient, amount, date):
        transaction = {
            'sender': sender,
            'recipient': recipient,
            'photo': amount, 
            'date': date,
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

# Receive one block. 
# Turn this block into a string, turn that into Unicode (for hashing). 
# Hash with SHA256 encryption, then translate the Unicode into a hexidecimal string.

    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash

# Our first block of the blockchain, containing the contacts of Mike.

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


# Add transactions to second block, these are Mike's past texts.

t1 = blockchain.new_transaction("Emma", "Mike", '1', '2018/5/21')
t2 = blockchain.new_transaction("Mike", "Emma", '2', '2018/5/22')
t3 = blockchain.new_transaction("Mike", "Emma", '1', '2018/6/01')
t4 = blockchain.new_transaction("Mike", "Emma", '2', '2018/6/02')
t5 = blockchain.new_transaction("Emma", "Mike", '3', '2018/6/03')
t6 = blockchain.new_transaction("Emma", "Mike", '1', '2018/8/03')
t7 = blockchain.new_transaction("Mike", "Emma", '1', '2019/1/06')
t8 = blockchain.new_transaction("Mike", "Claire", '1', '2019/1/06')
t9 = blockchain.new_transaction("Emma", "Mike", '2', '2019/2/8')
t10 = blockchain.new_transaction("Emma", "Mike", '2', '2019/2/13')
t11 = blockchain.new_transaction("Mike", "Emma", '3', '2019/3/18')
t12 = blockchain.new_transaction("Emma", "Mike", '2', '2019/3/18')
t13 = blockchain.new_transaction("Mike", "Emma", '1', '2019/3/18')
t14 = blockchain.new_transaction("Mike", "Claire", '1', '2019/7/23')
t15 = blockchain.new_transaction("Claire", "Mike", '1', '2019/8/26')
blockchain.new_block(2)

t16 = blockchain.new_transaction("Mike", "Claire", '2', '2019/10/01')
t17 = blockchain.new_transaction("Claire", "Mike", '1', '2019/10/04')
t18 = blockchain.new_transaction("Claire", "Mike", '3', '2019/10/04')
t19 = blockchain.new_transaction("Claire", "Mike", '3', '2019/10/18')
t20 = blockchain.new_transaction("Mike", "Claire", '2', '2019/10/21')
t21 = blockchain.new_transaction("Mike", "Claire", '2', '2019/10/22')
t22 = blockchain.new_transaction("Mike", "Claire", '3', '2019/10/22')
t23 = blockchain.new_transaction("Claire", "Mike", '1', '2019/10/24')
t24 = blockchain.new_transaction("Mike", "Claire", '1', '2019/10/25')
t25 = blockchain.new_transaction("Claire", "Mike", '1', '2019/10/29')
t26 = blockchain.new_transaction("Claire", "Mike", '1', '2019/11/03')
t27 = blockchain.new_transaction("Mike", "Claire", '2', '2019/11/06')
t28 = blockchain.new_transaction("Mike", "Claire", '1', '2019/11/08')
t29 = blockchain.new_transaction("Claire", "Mike", '1', '2020/1/12')
t30 = blockchain.new_transaction("Claire", "Mike", '1', '2020/1/16')
t31 = blockchain.new_transaction("Mike", "Claire", '1', '2020/1/28')
blockchain.new_block(3)

t32 = blockchain.new_transaction("Mike", "Amber", '1', '2020/2/04')
t33 = blockchain.new_transaction("Amber", "Mike", '1', '2020/2/04')
t34 = blockchain.new_transaction("Amber", "Mike", '2', '2020/2/06')
t35 = blockchain.new_transaction("Mike", "Amber", '1', '2020/3/02')
t36 = blockchain.new_transaction("Mike", "Amber", '2', '2020/4/14')
t37 = blockchain.new_transaction("Mike", "Amber", '2', '2020/4/16')
t38 = blockchain.new_transaction("Amber", "Mike", '1', '2020/5/24')
t39 = blockchain.new_transaction("Mike", "Amber", '1', '2020/6/01')
t40 = blockchain.new_transaction("Amber", "Mike", '3', '2020/6/12')
t41 = blockchain.new_transaction("Mike", "Amber", '1', '2020/7/19')
t42 = blockchain.new_transaction("Mike", "Amber", '2', '2020/7/23')
t43 = blockchain.new_transaction("Amber", "Mike", '2', '2020/11/16')
t44 = blockchain.new_transaction("Amber", "Mike", '1', '2021/1/22')
t45 = blockchain.new_transaction("Amber", "Mike", '2', '2021/1/23')
t46 = blockchain.new_transaction("Mike", "Amber", '1', '2021/2/01')
t47 = blockchain.new_transaction("Amber", "Mike", '3', '2021/2/13')
blockchain.new_block(4)

# Create json file, store data from blocks here for further processing.
data = blockchain.chain 
with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Convert the column 'transactions' into seperate column, so that all necessary information is clearly displayed in a Panda's dataframe: https://www.geeksforgeeks.org/converting-nested-json-structures-to-pandas-dataframes/ 
df = pd.json_normalize(data,record_path=['transactions'], meta=[
                  'timestamp', 'proof'])

# Split the data structure into contact information (the first block) and transactions (the latter three blocks)
# Texting information
df_transactions = df.tail(47)
df_transactions = df_transactions.drop(['name', 'gender', 'relationship category', 'access'], axis=1)

# Contact information
df_contacts = df.head(8)
df_contacts = df_contacts.drop(['sender', 'recipient', 'photo', 'date'], axis=1)

# An important function of the prototype is the information the 'dashboard' holds, as to provide an overview to the users. Here, we see an example; 
# The following function asks for a contact, and shows all messages sent to that contact. Additionally, it shows if the contact still has access to Mike's sent photos. 

# Function 1: filter messages per contact, check if they still have access. 
# Please enter one of Mike's ex-girlfriends: 'Emma', or 'Claire'.
name = str(input('Enter contact: '))
sleep(1)
def selection(name):
    select_transaction = df_transactions.loc[df_transactions['sender'] == name]
    select_contact = df_contacts.loc[df['name'] == name].copy()
    print ('Texting log: ', select_transaction),
    print('Contact information: ', select_contact) 
selection(name)



# The selection we see printed in our terminal is the text history between Mike and 'chosen ex-girlfriend', additionally, we can see if she still has access to Mike's photos, 
# which is represented as a 'True' value in the column, 'access'.


# Additionally, a function is to let the dashboard suggest blocking a contact after a certain amount of time has passed. 
# Functie 2: suggest blocking a contact after not having text communication for three years or longer.

sleep(1)

df_transactions['month'] = df_transactions['date'].str.split('/').str[1]
month = df_transactions['month']
time_difference =  (pd.Timestamp.now().normalize() - pd.to_datetime(df_transactions['date'], errors='coerce'))
three_years = int(1095)

def date_block():
    if time_difference.any() > three_years :
         if df_contacts["access"].any() == True:
             print(df_transactions["sender"] + " " + 'You have not spoken with this person in a while, this person has access to your photos')
             input('Would you like to restrict this contact from seeing your photos? ')
             block_contact(df_transactions['sender'])
    else:
        print('else statement triggered')

date_block()


# The last functions shows the blocking of contacts at free will of the user (Mike). Mike broke up with his last girlfriend Amber in 2021, and in the spirit of cleaning up and moving on, 
# he now wants to block her from seeing his photos. The following function first asks for the contact he wants to block, please fill in, 'Amber'
name1 = str(input('Enter contact you want to block: '))
def block_contact(name1):
    df_contacts.loc[df_contacts['name'] == name1, 'access'] = False
    print('Contact blocked')

sleep(2)

# Confirmation that this contact needs to be blocked; 
block = str(input('Confirm restricting this contact from seeing your photos? ')) 
sleep(1)

if block == 'Yes':
    block_contact(name1)
    print('This contact is now blocked: ', df_contacts)
else: 
    print('Contact not blocked')

# We nog see that the contact 'Amber', has been blocked. The value 'True' has switched to 'False' for her in the column 'access'.
