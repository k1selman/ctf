#### CTF: justCTF 2024 teaser
#### Challenge: Star
#### Category: RE
#### Solution author: k1selman

We are presented with star.tar.gz archive which contains star binary (ELF 64-bit).

Checksec for the lulz:
```
[*] '/home/user/ctf/re/jctf_teaser_2024/Star/star'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
```
Ghidra manages to identify entry function, which leads us to main (through __libc_start_main).

Main function has 9 blocks of three function calls followed by do-while interactive loop, with the interesting part being:
```
    uVar2 = thunk_FUN_00106ec0(local_68,uVar1);
    puVar3 = (undefined8 *)thunk_FUN_0010b9f0(uVar2);
    (**(code **)*puVar3)(puVar3);
```