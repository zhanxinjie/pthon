import re 
  
pattern = 'this'
text = 'http://blog.csdn.net/caimouse is great, this is great way!'
  
match = re.search(pattern, text) 
  
s = match.start() 
e = match.end() 
  
print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format( 
 match.re.pattern, match.string, s, e, text[s:e]))
