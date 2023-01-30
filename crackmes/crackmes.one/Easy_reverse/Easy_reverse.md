Challenge name: Easy_reverse
File name: rev50_linux64-bit
SHA256: bb28a152966bed0a369f30149a912982ea33b408794bfbd82e73c87ff4e184ff

First thing's first, lets run "file" against given to make sure we are dealing with ELF file format:
![[Pasted image 20230130181037.png]]

Alright, we have in fact 64-bit ELF executable, so since this is crackme challenge, lets run the file and see what is the required input:
![[Pasted image 20230130181200.png]]

So, as usual, we are supposed to find the desired password.
Let's fire up Ghidra and load our binary into it and study the contents of it - like, for example, functions.
When we let Ghidra analyze the binary, we will be able to see what functions were identified within the binary, as in this example:
![[Pasted image 20230130181505.png]]
As we can see, we have quite a few functions to consider, however in this case Ghidra was able to detect and point out the "main" function for us, so let's study this one first and see what it does.
When we double click on the "main" function, Ghidra presents us with:
![[Pasted image 20230130181646.png]]
The decompiled code is very readable and we can easily understand the program logic and flow just by reading it, so we do not really have to study disassembled code. Lines 7-12 are the most interesting to us, as that is where the password magic happens. Let's take a closer look at the code:
![[Pasted image 20230130182006.png]]
So, how does the password should look like?
Well, line 9 tells us that it should be 10 characters long, as we will meet this specific condition, after this the program interprets, in line 10, (param_2[1] + 4) as a pointer for char and reads data where (param_2[1] + 4) points at - so, where the 5th character points at, to be precise. And in this case it should be pointing at character '@'. So, to sum things up - if our input is 10 characters long, and the 5th character is '@', we should be able to grab our flag. Let's see if we are right by giving four a's + @ + five a's as an input:
![[Pasted image 20230130183401.png]]
Worked like a charm. Indeed an easy RE challenge :)