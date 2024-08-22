<b>CTF: justCTF 2024 teaser</b><br>
<b>Challenge: star</b><br>
<b>Category: RE</b><br>

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

Given the structure of main, it seemed that there are more 'functionalities' present in the binary, just not listed in the menu, and by
going through numbers 6, 7, 8 and 9, the following result was most interesting:

```
JCTF COMMANDER v0.1
1. create file
2. rename file
3. print file
4. delete file
5. edit file
0. exit
> 7
Input archive name:
```
