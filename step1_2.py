#!/usr/bin/env python3
import re
import sys

## Obejctive: General descriptives
# Create a dictionary within a dictionary:
# Sequence/chromosome name as the Main Key:
    #For each Main Key, create a dictionary consisting of:
    #   {'MainKey1': {'length'=123, 'GC_count' = 123, 'GC_content' =}, 'MainKey2'... }

fasta = open(sys.argv[1])

def GC_content(fasta):
    seq_dict = {}
    for line in fasta:
       line = line.rstrip()
       print(line)

       if line.startswith(">"):
           header = line
           #save the header as a key:
           if header not in seq_dict:
               ##can create the key codes inside here:
               ##*
              # header = line
               print(header)
               ##"all" versus "non" indicates whether or non the "n" nucelotides were included in the length calculation.
               seq_dict[header] = {'length_all': 0, 'length_non': 0,'GC_count' : 0, 'GC_content_all': 0.0, 'GC_content_non': 0.0,} 
               print(seq_dict)
               ##at this point we should have a dictionary that looks like this:
               ##{'MainKey1': {'length'='', 'GC_count' = '', 'GC_content' =''}, 'MainKey2'... }
       else: 
           #this is for the sequence itself:
               #calcualte the length:
               ##create a new dictionary inside the first:
               ##which will have three entries (for now empty):
               #seq_dict[header][line] = {}
               ##calculate the length of the line with and without Ns:
               line.upper()
               ##this shoudl include all bases: ATCGN
               seqlength = len(line)
               print(f"This is your entire sequence length (ATCGN): {seqlength}")
               seq_dict[header]['length_all'] += seqlength
               
               
               ##count only ATCG bases (no Ns) for length_non():
               countbases = 0
               for base in line:
                    if base == 'G':
                         countbases += 1
                    if base == 'C':
                         countbases += 1
                    if base == 'A':
                        countbases += 1
                    if base == 'T':
                        countbases += 1
                    else:
                         countbases +=0
               print(f"This is your shortened sequence length (ATCG): {countbases}")
               seq_dict[header]['length_non'] += countbases



               ## add the line length to the dictionary 
               ## with the key "length" 
               ## and "length var as the value"
               ##calcualte the GC count:
               count = 0
               for nt in line:
                    if nt == 'G':
                         count += 1
                    if nt == 'C':
                         count += 1
                    if nt == 'A':
                        count += 0
                    if nt == 'T':
                        count += 0
                    else:
                         count +=0
               print(count)
               seq_dict[header]['GC_count'] += count



               #calculate the GC content:
               #GC_content = count/seqlength
               if seq_dict[header]['length_all'] > 0:
                ##create the GC content for all bases in the file(ATCGN):
                seq_dict[header]['GC_content_all'] = seq_dict[header]['GC_count'] / seq_dict[header]['length_all']
                ##create the GC content in only ACTGs (no 'n's):
                seq_dict[header]['GC_content_non'] = seq_dict[header]['GC_count'] / seq_dict[header]['length_non']
              # print(GC_content)
               print(seq_dict[header]['GC_content_all'])
               print(seq_dict[header]['GC_content_non'])

    return(seq_dict)

result = GC_content(fasta)
print(result)

#               
#             
#                  
#                   
#                 
#                     
#                  
#                       
#                     
#           
#               
#              

                       
                
           
             