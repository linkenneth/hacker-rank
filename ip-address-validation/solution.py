# def validateIPv4(line):
#     parts = line.split('.')
#     if len(parts) != 4:
#         return False
#     for part in parts:
#         if not part.isdigit():
#             return False
#         elif part != '0' and part[0] == '0':
#             return False  # no leading zeros
#         if not (0 <= int(part) <= 255):
#             return False
#     return True

import re

IPV4_PART = r'(1?\d{1,2}|2[0-4]\d|25[0-5])'
IPV4_RE = re.compile(r'\.'.join([IPV4_PART] * 4) + '$')

def validateIPv4(line):
    '''
    Regex version for practice.
    '''
    match = IPV4_RE.match(line)
    # if match:
    #     print match.groups()
    return match

# HEX_CHARS = set('0123456789abcdefABCDEF')
#
# def validateIPv6(line):
#     parts = line.split(':')
#     if len(parts) != 8:
#         return False
#     for part in parts:
#         if len(part) > 4:
#             return False
#         if not part:
#             continue
#         for c in part:
#             if c not in HEX_CHARS:
#                 return False
#         if not (0 <= int(part, base=16) <= 0xffff):
#             return False
#     return True

IPV6_PART = r'([\da-fA-F]{,4})'
IPV6_RE = re.compile(r':'.join([IPV6_PART] * 8) + '$')

def validateIPv6(line):
    match = IPV6_RE.match(line)
    # if match:
    #     print match.groups()
    return match

def validate(line):
    if validateIPv4(line):
        return 'IPv4'
    elif validateIPv6(line):
        return 'IPv6'
    else:
        return 'Neither'

N = int(raw_input())
for _ in xrange(N):
    line = raw_input()
    print validate(line)
