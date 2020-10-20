'''
Code Golf Prompt 2020/10/16
======================
Challenge: Given a CSV file with purely integers, write a sorting algorithm to sort each row in as few characters as possible.

Rules:
 * Input and output IS NOT counted for your character counts.
 * Class implementation IS NOT counted
 * Function implementation IS counted
 * Import statenents ARE NOT counted (within reason; don't import your logic)
 * Whitespace IS counted
 * No using built in sorting algorithms
 * You can expect the CSV file to contain only integers, but may have irregular whitespacing you need to take care of.
 * The CSV file will have multiple integers per row. Sort each row, the entire file.
 * We will use this character counter: https://wordcounter.net/character-count

Valid Languages: Anything I can compile or run easily enough. Viable options are Python, Java, C++, Ruby, NODE.JS, but you can obviosuly choose other languages.

Deadline & Submission: Next Week Friday @ 6 PM CST, 2020/10/23. Submission through a GitHub link is preferred, but will accept pastebins, source file uploads, and messsages with the code properly formatted in a code block
'''

f = open("20201019.csv")  # not counted
n=[]
for i in f.readlines():
 z=list(map(int,list(filter(None,i.strip().split(",")))));m=0
 for j in range(len(z)**2,0,-1):
  if len(z)==1:break
  m=0 if m==len(z)-1else m
  if z[m]>z[m+1]:
   z.insert(m+1,z.pop(m))
  m+=1
 n.append(z)
print(n)  # not counted
