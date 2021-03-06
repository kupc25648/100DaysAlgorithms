'''
Sometimes I read that one-time pad is an unbreakable cipher. And of course, completely broken example is usually attached.
The problem is, people confuse the definition of perfect cipher for unbreakable. If the cipher is perfect (according to Shannon), the probability distribution of obtaining cipher-text instance from different plain-texts must be uniform. In other words, given some cipher-text there is an equal chance for any plain-text to be the source.
What follows is that adversary with infinite computational power can’t get any information about plain-text from pure cipher-text.
But that’s far from unbreakable. Even correctly used OTP can be easily broken. Imagine a bank that would encrypt a digital checks with OTP, how easy would it be to rewrite $100.00 to $999.99 at well-known check position?
Is OPT a perfect cipher? Not in most implementations. While people emphasize the single use of key, they also forget about the uniformity of key distribution which is as important.
When I generated my messages I violated the one-time rule. The consequences are inevitable.
'''
ciphertext = [
    b'm\x99QH\xfc\x99\xcel\xfc>\x11\xf81\xda:\x15"6\xd3b\x07\x7f\xed\x87\xd5\xd4\xf0\xbb',
    b'x\x96^\r\xb5\x83\x86u\xeel\x0e\xf8,\xce:\x06 6\xd0b\nx\xfd\x87\xd9\xc9\xe8',
    b'm\x90O^\xfc\x80\xd3f\xe7>\x16\xf46\x89w\x05r8\xcb-\x04',
    b'`\x97O\r\xbd\x9f\xc3%\xe1q\x0e\xb15\xdbu\x0e5y\xca*\x1c7\xec\xc2\xd2\xcb',
    b"m\x90[Y\xfc\x80\xdf%\xeb\x7f\x03\xe2b\xc1{\x167y\xdf'\x16y\xa8\xc6\x97\xc2\xed\xa9p(",
    b'`\x9dN\r\xb5\x8b\x86m\xe0n\x1f\xb1*\xc8i@45\xd25\x1d7\xe9\xd0\xd6\xdf',
    b'p\x96\x1aL\xfc\x83\xcfb\xe7jZ\xfe0\x89s\x0er8\x9d&\x12n',
    b'p\x96\x1aL\xfc\x9b\xcfv\xe6q\x14\xb1-\xdb:\t<y\xd3-\x1dr',
    b'p\x8b\x1aD\xa8\xcd\xd2m\xeal\x1f\xf7-\xdb\x7f@&1\xd8b\x1fr\xfb\xd4\x97\xc1\xf0\xa2t',
    b'x\x94V\r\xa8\x85\xc7q\xafi\x1f\xb11\xcc\x7f@=+\x9d1\x16r\xe5',
    b'p\x8b\x1aO\xa9\x99\x86d\xafz\x08\xf4#\xc4:\x17;-\xd5+\x1d7\xe9\x87\xd3\xd4\xfa\xad|',
    b'p\xd8IY\xbd\x83\xc2%\xees\x13\xf5b\xddr\x05r+\xd2#\x01',
    b'v\x9e\x1aL\xfc\x9e\xd3w\xe9>\x0e\xfe0\xc4\x7f\x0e&<\xd9b\x00\x7f\xe7\xd5\xd2',
    b'x\x96^\r\x95\xcd\xcej\xe3zZ\xe6+\xddr\t<y\xd0;S\x7f\xe9\xc9\xd3',
    b"~\x8a[D\xb2\x9e\x86j\xe9>\x0e\xf9'\x89}\x0f>=\xd8,Sd\xe9\xc9\xd3",
    b'q\x97M\r\xba\x88\xd1%\xf6{\x0e\xb1*\xc6m@&1\xd8;St\xfa\xc2\xd2\xd6',
    b'm\x90HB\xa9\x8a\xce%\xe2gZ\xf7+\xc7}\x05 *\x9d6\x1c7\xfc\xcf\xd2\x86\xfb\xa9t5',
    b'n\x90SA\xb9\xcd\xcf%\xf8{\x1f\xe1b\xder\t><\x9d\x0bS`\xed\xc2\xc7',
    b'9\xd8_I\xbb\x8c\xd4%\xeer\x16\xf0,\x89j\x0f7y\x9dbS7\xa8\x87\x97\x86\xbf',
]


from string import ascii_lowercase

#set of allowed characters
letters = set(ascii_lowercase+ ' ')

#reconstructed messages
plaintext = ['']*len(ciphertext)

#take all the codes at the same position
for messages in zip(*ciphertext):
    keys = set()

    #find viable keys
    for key in range(256):
        for m in messages:
            if chr(m^key) not in letters:
                break
        else:
            keys.add(key)

    key = keys.pop() if len(keys) == 1 else None

    #reconstruct plain text
    for i,m in enumerate(messages):
        if key is not None:
            plaintext[i] += chr(m^key)
        else:
            plaintext[i] += '?'

print(plaintext)
