SHA256: 1b7d7c5ae2b5cd333dd539185581ccf5f74ba2e8c48e3a047b7bc9a44a50a59a <br />
Platform: Linux <br />
Challenge: Find the serial key and code a keygen. <br />
<br />
When we try to run our binary, we get: <br />
<img src='png/Pasted image 20230205142500.png'> <br />
Let's fire up Ghidra and load our binary into it. <br />
After the initial analysis is done by Ghidra, we can see that it was able to identify the main function of the program:<br />
<img src='png/Pasted image 20230205142555.png'><br /> 
Good for us, now we can take a look at the code that is interesting for us:<br />
<img src='png/Pasted image 20230205142712.png'><br />
The decompiled code looks like this. Right away we see that we need to do some renaming here to make it more readable for us. Every C program coded to run in a hosted execution environment contains the definition (not the prototype) of a function named `**main**`, which is the designated start of the program. Usually, we will see something like:<br />
<img src='png/Pasted image 20230205143317.png'><br />
However, Ghidra for some reason has issues with square brackets and its easier to use reference int main(int argc, char **argv) to make our code like that using "Edit Function Signature" option:<br />
<img src='png/Pasted image 20230205143411.png'><br />
Line 12 says that the function expects argc to be equal to 2 so we can enter our if-else. So it expects one argument to be passed in - let's take a look at corresponding "else" on line 46:<br />
<img src='png/Pasted image 20230205151101.png'<br />
So, the second argument is a password. The disassembled code of this part looks like:<br />
<img src='png/Pasted image 20230205151232.png'><br />
And we see LEA (Load Effective Address) being called, and what it does is computing the effective address of the second operand and storing it into argc (first operand here). Ok, lets go back at the start of our if-else and see what is done as the function goes on. On line 13 we can see that the second argument is being stored in unclear-named variable, so let's rename it to "password":<br />
<img src='png/Pasted image 20230205152534.png'><br />
Next up, on line 14 we can see length of our password being stored in "sVar3" variable, so lets rename it properly as well:<br />
<img src='png/Pasted image 20230205152920.png'><br />
It's already much more clear piece of code. We can immediately see that the password length is expected to be 9, and that the fifth character should be '-'. On line 17 new variable is being created and its value is 0, so my first guess its that will be the counter as right after it we enter while function - and indeed, this variable is being incremented by 1 in the loop, so indeed it is a counter, so since we know that we can assume this while() function is the same as for loop:<br />
for(int i = 0; i < strlen(password); i++).<br />
On line 21, it is being checked if there is '@' on i'th character of the password, and if its true, we will break out of the while loop and see "good job! now keygen me!" string.<br />
<br />
So, the serial key should be 9 characters long, have '-' as 5th character, and have '@' character. Let's test it with sample input meeting those requirements:<br />
<img src='png/Pasted image 20230205153959.png'><br />
Nice. Now, let's write simple Python script to help us here to generate desired passwords and test them against our target program:<br />
<img src='png/Pasted image 20230205155152.png'><br />
So, lets go step by step through this code:<br />
After importing all the necessary libraries, we are creating "keygen" function in which we create chars variable to specify what characters we want as an input, then we are creating key variable which selects 7 of the desired characters, and after it's done we are adding '@' to the created string and putting '-' as the 5th character, and we put everything together.<br />

Next, we create "test" function which takes program and counter as parameters and here we just specify that we want to generate new key and test it against our target program that many times as we specify in "counter" variable - all is done inside our for-loop. Within every iteration of the loop, we are printing the number of test and generated key, and after all the iterations are done, we inform that we have successfully completed X runs, where X is defined in the counter.<br />

After defining those two functions, we put them to use by invoking test function with path to our executable and number of times we want our for loop to iterate. Let's see the results:<br />
<img src='png/Pasted image 20230205160728.png'><br />
Looks just fine. We have cracked the challenge and successfuly built key generator for it:) 


