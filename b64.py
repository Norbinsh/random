"""Playing around with base64 encoded functions"""

import base64
decoded = [base64.b64decode('ZGVmIGI2NHBnKCk6IHByaW50KCJTaGF5OiByZW1haW5kZXIgaXM6XG4ge3JlbWFpbmRlcn0'
'uXG5PcmlnIHZhbHVlcyB3ZXJlIDUgbW9kdSAyIi5mb3JtYXQocmVtYWluZGVyPSA1ICUgMikpCmI2NHBnKCk='), base64.b64decode('ZXhlYyhieXRlc3RvdXRmKQ==')]
bytestoutf = decoded[0].decode('utf-8')
eval(decoded[1])
