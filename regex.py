import re

# 1. Matching Literal Text
pattern1 = r'cat'
text1 = 'concatenate'
match1 = re.search(pattern1, text1)
print(match1.group() if match1 else "No match")

# 2. Matching Any Single Digit
pattern2 = r'\d'
text2 = 'I have 3 apples.'
match2 = re.search(pattern2, text2)
print(match2.group() if match2 else "No match")

# 3. Matching Any Whitespace Character
pattern3 = r'\s'
text3 = 'Hello\tworld\n'
matches3 = re.findall(pattern3, text3)
print(matches3)

# 4. Matching Specific Characters (Case Insensitive)
pattern4 = r'[Pp]ython'
text4 = 'Python is great, but python is also nice.'
matches4 = re.findall(pattern4, text4)
print(matches4)

# 5. Matching One or More Digits
pattern5 = r'\d+'
text5 = 'I have 123 apples.'
match5 = re.search(pattern5, text5)
print(match5.group() if match5 else "No match")

# 6. Matching Email Addresses
pattern6 = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
text6 = 'Contact me at john.doe@example.com'
match6 = re.search(pattern6, text6)
print(match6.group() if match6 else "No match")

# 7. Matching Dates (MM/DD/YYYY format)
pattern7 = r'\b(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}\b'
text7 = 'Date of birth: 12/31/1990'
match7 = re.search(pattern7, text7)
print(match7.group() if match7 else "No match")

# 8. Matching Phone Numbers (US format)
pattern8 = r'\b\d{3}-\d{3}-\d{4}\b'
text8 = 'Call me at 123-456-7890'
match8 = re.search(pattern8, text8)
print(match8.group() if match8 else "No match")

# 9. Matching HTML Tags
pattern9 = r'<([A-Za-z][A-Za-z0-9]*)\b[^>]*>(.*?)</\1>'
text9 = '<h1>Hello, World!</h1>'
match9 = re.search(pattern9, text9)
print(match9.group() if match9 else "No match")

# 10. Matching URLs
pattern10 = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
text10 = 'Visit us at http://www.example.com'
match10 = re.search(pattern10, text10)
print(match10.group() if match10 else "No match")

# 11. Matching Words Starting with a Capital Letter
pattern11 = r'\b[A-Z][a-z]*\b'
text11 = 'The quick Brown fox Jumps over the Lazy Dog'
matches11 = re.findall(pattern11, text11)
print(matches11)

# 12. Matching IPv4 Addresses
pattern12 = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
text12 = 'Server address: 192.168.0.1'
match12 = re.search(pattern12, text12)
print(match12.group() if match12 else "No match")

# 13. Matching Hexadecimal Colors in CSS
pattern13 = r'#(?:[0-9a-fA-F]{3}){1,2}\b'
text13 = 'background-color: #a3c113; color: #333;'
matches13 = re.findall(pattern13, text13)
print(matches13)

# 14. Matching Optional Prefixes
pattern14 = r'Mr\.?'
text14 = 'Mr. Smith met Mr Brown.'
matches14 = re.findall(pattern14, text14)
print(matches14)

# 15. Matching Lines Starting with a Date
pattern15 = r'^\d{2}/\d{2}/\d{4}'
text15 = '''
12/31/2023: New Year's Eve
01/01/2024: New Year's Day
'''
matches15 = re.findall(pattern15, text15, re.MULTILINE)
print(matches15)

# 16. Matching Nested Brackets
pattern16 = r'({(?:[^{}]|(?1))*})'
text16 = '{ "name": "John", "age": 30, "city": "New York" }'
match16 = re.search(pattern16, text16)
print(match16.group() if match16 else "No match")

# 17. Matching Lines Containing Specific Keywords
pattern17 = r'\b(?:error|warning)\b'
text17 = '''
Error: File not found
Warning: Low disk space
Info: System is running normally
'''
matches17 = re.findall(pattern17, text17)
print(matches17)

# 18. Matching Repeated Patterns
pattern18 = r'(\w+)\s+\1'
text18 = 'hello hello world world'
matches18 = re.findall(pattern18, text18)
print(matches18)

# 19. Matching Markdown Headings
pattern19 = r'^#{1,6}\s.*$'
text19 = '''
## Introduction
### Details
#### Subsection
'''
matches19 = re.findall(pattern19, text19, re.MULTILINE)
print(matches19)

# 20. Matching Roman Numerals
pattern20 = r'^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
text20 = 'XIV is 14 in Roman numerals.'
match20 = re.search(pattern20, text20)
print(match20.group() if match20 else "No match")
