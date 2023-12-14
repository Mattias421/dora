from dora.xp import _get_sig_str

print(_get_sig_str('9f0dabaa'))
signatures = [
    '9f0dabaa', '5a3f87bc', '1e9c6f23', 'f0b2e1d8', '73c5489a',
    'ac84d39e', '2b5e1fa7', 'e75ca894', '1d0f3eab', '8e6b49c1'
]

for sig in signatures:
    result = _get_sig_str(sig)
    print(result)
