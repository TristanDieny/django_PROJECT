import sqlite3
import pandas as pd
from pandas import DataFrame


#conn = sqlite3.connect('db.sqlite3')
#c = conn.cursor()
#
## Create table - SNPs
#
#c.execute('''DROP TABLE SNPTABLE''')
#
#        
#c.execute('''CREATE TABLE SNPTABLE
#             ([PUBMEDID] integer, [FIRST AUTHOR] text, [DATE] date, [JOURNAL] text, [LINK] text, [STUDY] text,
#             [DISEASE/TRAIT] text, [INITIAL SAMPLE SIZE] text, [REGION] text, [CHR_ID] integer, 
#             [CHR_POS] integer, [STRONGEST SNP-RISK ALLELE] text, [SNPS] text, [SNP_ID_CURRENT] integer, 
#             [CONTEXT] text, [RISK ALLELE FREQUENCY] text, [P-VALUE] text, [PVALUE_MLOG] text)''')
#        
#conn.commit()

# Insert data

file = open('gwas_catalog_v1.0-associations_e96_r2019-09-24_european_nature_genetics_1000.tsv', "r+")
file2 = open('gwas_catalog_v1.0-associations_e96_r2019-09-24_european_nature_genetics_1000_ID.tsv', "w+")
i=0

for line in file:
    if i == 0:
        line = line[:len(line)-2] + "\tID\n"
    else:
        line = line[:len(line)-2] + "\t"+str(i)+"\n"
    i+=1
    file2.write(line)
    
file.close()
file2.close()