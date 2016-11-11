# -*- coding: utf-8 -*-
"""
Created on Wed Nov 09 13:52:38 2016

@author: Badrinath
"""

import pandas as pd
import networkx as nx
import csv
import time

start_time = time.time()
csv.field_size_limit(1000 * 1024 * 1024)
csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)
    
    
loc = r'paymo_input/batch_payment.csv'
 

fileds = ['id1','id2']
df_batch_payment = pd.read_csv(open(loc,'rU'), encoding='utf-8', engine='c',usecols=fileds,skipinitialspace=True,low_memory=False,infer_datetime_format=True,lineterminator='\n')
first_degree_friends_for_id1 = {k: g["id2"].tolist() for k,g in df_batch_payment.groupby("id1")}
del df_batch_payment

graph = first_degree_friends_for_id1
del first_degree_friends_for_id1

G = nx.Graph(graph)

#path = nx.shortest_path(G,source='12',target='23')

with open(r'paymo_input/stream_payment.csv', 'rU') as mycsvfile:
    thedata = csv.reader(mycsvfile, dialect='mydialect')
    next(thedata, None)
    with open(r'paymo_output/output1.txt', 'w') as f1:
        for row in thedata:
            try:
                if len(nx.shortest_path(G,source=row[1],target=row[2])) == 1:
                    f1.write('trusted\n')
                elif len(nx.shortest_path(G,source=row[1],target=row[2])) != 1:
                    f1.write('unverified\n')    
            except:
                f1.write('unverified\n')                
            finally:
                pass
mycsvfile.close()
f1.close() 

           
with open(r'paymo_input/stream_payment.csv', 'rU') as mycsvfile:
    thedata1 = csv.reader(mycsvfile, dialect='mydialect')
    next(thedata1, None)    
    with open(r'paymo_output/output2.txt', 'w') as f2:
        for row in thedata1:
            try:
                if len(nx.shortest_path(G,source=row[1],target=row[2])) <= 2:
                    f2.write('trusted\n')
                elif len(nx.shortest_path(G,source=row[1],target=row[2])) > 2:
                    f2.write('unverified\n')    
            except:
                f2.write('unverified\n')                
            finally:
                pass 
mycsvfile.close()
f2.close()
            
with open(r'paymo_input/stream_payment.csv', 'rU') as mycsvfile:
    thedata2 = csv.reader(mycsvfile, dialect='mydialect')
    next(thedata2, None)        
    with open(r'paymo_output/output3.txt', 'w') as f3:
        for row in thedata2:
            try:
                if len(nx.shortest_path(G,source=row[1],target=row[2])) <= 4:
                    f3.write('trusted\n')
                elif len(nx.shortest_path(G,source=row[1],target=row[2])) > 4:
                    f3.write('unverified\n')    
            except:
                f3.write('unverified\n')                
            finally:
                pass           
mycsvfile.close()            
f3.close() 
del graph  
del G     
print("--- %s seconds ---" % (time.time() - start_time))    
