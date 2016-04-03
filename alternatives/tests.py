#!/usr/bin/env python3

import pytest

exec('echo_client.py')


# Test the function:
print('Response from server:', echo_client('Ping'))

