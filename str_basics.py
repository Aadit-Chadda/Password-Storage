string = "(b'D/2ComZ2Hg==', <class 'bytes'>)"

pa = string.lstrip("(b'")
pa = pa.rstrip("', <class 'bytes'>)")
print(pa)
