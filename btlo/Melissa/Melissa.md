#### Scenario

Melissa aka W97M.Melissa.A (Symantec) or Virus:W32/Melissa (F-Secure) is a macro virus dates back to March 26, 1999.  
  
This challenge should be completed in a virtual machine as it contains real malware.

Provided file name: LIST.DOC <br />
SHA256: 554701bc874da646285689df79e5002b3b1a1f76daf705bea9586640026697ca<br />

#### Q1: Submit the stream number that contains the Melissa macro in the LIST.DOC file
To answer this question, it would be a good idea to run tools like olevba or oledump against our target file, lets go with oledump for cleaner output:<br />
<img src='png/Pasted image 20230130210438.png'><br />
We can see immediately see that stream number of our interest is 7, as the letter M next to the stream indicate that given stream contains macros.

#### Q2: After identifying which version of word, Melissa will enable all macros from registry?
Answer to this question can be found easily after running olevba agains the target file, where we can spot in of the first few lines:<br />
<img src='png/Pasted image 20230130210929.png'><br />
And the Word version of interest is 9.0

#### Q3: What is the email service targeted by Melissa?
Again, with the results of olevba used against target file, we can read from the following lines:<br />
<img src='png/Pasted image 20230130211135.png'><br />
The targeted email service is Outlook.

#### Q4: How many number of email addresses were collected?
One of the things that olevba does is that it also extracts the source code of the parsed files macros, and by reading those we eventually find:<br />
<img src='png/Pasted image 20230130211337.png'><br />
Here, what is relevant for us is the for-loop, as it counts up to exactly 50 with "AddyBook.AddressEntries.Count", and from that we can understand that the number of email addresses that were collected is 50.

#### Q5: What is the string used by melissa to identify whether a PC is infected or not and decide whether to collect email addresses or not?
By studying the extracted source code which can be found right after the function from last question, we find:<br />
<img src='png/Pasted image 20230130211745.png'><br />
Which ends the execution if there is a match for "... by Kwyjibo" string, and that is the answer to the question.

#### Q6: What is the variable responsible for identifying the email username of the infected PC?
Right after the for-loop from question 4, in the same function as studied in that question, there is:<br />
<img src='png/Pasted image 20230130212007.png'><br />
Which tells us that malware is identifying the email username of the infected host by "Application.UserName" and is utilizing it in the message body.

#### Q7: What is the text in email body used for spreading melissa?
Answer is in the screenshot above, the string of interest is "Here is that document you asked for ... don't show anyone else ;-)"

#### Q8: What is the text that is inserted by Melissa in an open word document?
Right at the end of the extracted source code we can read:<br />
<img src='png/Pasted image 20230130212219.png'><br />
Answer is stored in the Selection.TypeText variable, and it says "Twenty-two points, plus triple-word-score, plus fifty points for using all my letters.  Game's over.  I'm outta here."

