#!/usr/bin/env python
import os

pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

print('----------')
print('Processes')

for pid in pids:
    try:
        print(open(os.path.join('/proc', pid, 'cmdline'), 'rb').read().split(b'\x00'))
    except IOError: # proc has already terminated
        continue

print('----------')
print('Environment Variables')

for k, v in os.environ.items():
    print(f'{k}={v}')