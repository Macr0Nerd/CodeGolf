"""
Build a binary to string translator in as few characters as possible (white space included!).

Rules:
• Class implementation IS counted
• Import statements ARE counted
• Print statements (within reason) ARE NOT counted
• The input will be a string and IS NOT counted
• Whitespace IS counted
• Any Turing complete language is allowed
• Sharing solutions is allowed (I will have all my code public on my GitHub)
• The string will be only 1s, 0s, and spaces. It will be complete bytes space separated.
• Using built in binary translators ARE NOT allowed!
"""

z = input("Enter in binary string, space separated: ")  # Not counted; input
a=""
for i in z.split():
 x=0
 for j in range(8):
  x+=(2**(7-j) if int(i[j]) else 0)
 a+=chr(x)
print(a)  # Not counted; output
