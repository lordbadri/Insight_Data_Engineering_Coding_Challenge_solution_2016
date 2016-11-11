###Badrinath Thirumalachari
# Insight Data Engineering Coding Challenge Jan 2017

My Solutions to [Insight Data Engineering Coding Challenge jan 2017](https://github.com/InsightDataScience/digital-wallet)


###Solution
------------------------------------------------
I have create a file under the `/src` dictionary called `antifraud.py`. It reads `batch_payment.csv` file from the `paymo_input` directory as a pandas dataframe and later is stored as a python dictionary for easy conversion to a network using the networkx library in python. After implementing the required features the output is written into the `paymo_output` directory as `output1.txt`, `output2.txt` and `output3.txt`.


In particular, I converted the csv file into a pandas dataframe, cleaning and extracting the data that was required to complete the challenge. I then convert the dataframe into a python dictonary with the user id1 as the key and all the transacted users as the values under that specific key. Later I convert the dictonary to a network graph using the networkx library in python. I use this networkx object to implement the features asked in the coding challenge for the `stream_payment.csv` file provided.
Finding the degree of seperation between the user ids was a matter of calculating the shortest path in the network graph created using the `batch_payment.csv` file between the users transacting in the `stream_payment.csv` file.

###Environment
--------
* Python 2.7
* pandas library version 0.18.1 in python
* networkx library version 1.11 in python
* Linux

###Usage
--------
To execute the code, go to the file directory and just run the command `bash run.sh`. The python program will implement all the features for the `stream_payment.csv` file into the output files as mentioned above. 
* Note1: The code assumes that the `batch_payment.csv` and `stream_payment.csv` are avliable in the  `paymo_input` in `csv` format.
* Note2: The code currently works for pandas vesrion 0.18.1 in python. I have taken this issue into account and my shell script takes  care of this issue by changing the version of pandas on the system the script is running to the version needed to excecute the code.

###Output details
--------
Outputs are in the required formate.
* `output1.txt` - When anyone makes a payment to another user, they'll be notified if they've never made a transaction with that user before.
* `output2.txt` - Users should be able to pay each other without triggering a warning notification if they're "2nd degree" friends. 
* `output3.txt` - Implementing a feature to warn users only when they're outside the "4th degree friends network".
