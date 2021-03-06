'''
Code Golf Prompt 2020/10/16
======================
Challenge: Given a CSV file with purely integers, write a sorting algorithm to sort each row in as few characters as possible.

Rules:
 * Input and output IS NOT counted for your character counts.
 * Class implementation IS NOT counted
 * Function implementation IS counted
 * Import statements ARE NOT counted (within reason; don't import your logic)
 * Whitespace IS counted
 * No using built in sorting algorithms
 * You can expect the CSV file to contain only integers, but may have irregular whitespacing you need to take care of.
 * The CSV file will have multiple integers per row. Sort each row, the entire file.
 * We will use this character counter: https://wordcounter.net/character-count

Valid Languages: Anything I can compile or run easily enough. Viable options are Python, Java, C++, Ruby, NODE.JS, but you can obviosuly choose other languages.

Deadline & Submission: Next Week Friday @ 6 PM CST, 2020/10/23. Submission through a GitHub link is preferred, but will accept pastebins, source file uploads, and messsages with the code properly formatted in a code block
'''

f = open("20201019.csv").readlines()  # not counted
n=[]
for i in f:
 z=list(map(int,list(filter(None,i.strip().split(",")))));m,u=0,len(z)
 for j in range(u**2):
  if u==1:break
  m=0if m==u-1else m
  if z[m]>z[m+1]:z.insert(m+1,z.pop(m))
  m+=1
 n+=[z]
print(n)  # not counted
