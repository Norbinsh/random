"""Playing around with base64 encoded functions"""

import base64

# decode base64-encoded functions into bytes type
decoded = [base64.b64decode('ZGVmIGI2NHBnKCk6IHByaW50KCJTaGF5OiByZW1haW5kZXIgaXM6XG4ge3JlbWFpbmRlcn0'
'uXG5PcmlnIHZhbHVlcyB3ZXJlIDUgbW9kdSAyIi5mb3JtYXQocmVtYWluZGVyPSA1ICUgMikpCmI2NHBnKCk='), base64.b64decode('ZXhlYyhieXRlc3RvdXRmKQ==')]
# decode into a string literal without the b'' bytes indicator literal
bytestoutf = decoded[0].decode('utf-8')
# run it
eval(decoded[1])
