Technical Practice - you can do this in your own time but suggest to have this complete in the next 7 days. Problems for this week.

Problem 1 - Going Away Cards



This week we have a challenge for you.



In order to give everyone a keepsake from the program, we want to give each participant a card with the signatures of all the other participants.



Keeping track of who signed what is hard, and no matter how much we like each other, it's still a pain to sign so many cards. Instead, let's write a Python program to sign the cards for us!



Thankfully, at each site, we have a list of all the names of participants. You want to write a card for each of the names in the list.



We want to sign everyone's name on each of the cards - but we don't want anyone to sign their own cards. Write a function everyone_sign() that takes in an array of names, and returns a dictionary of messages. The message can say anything, but it must also include the other names in the list (see the example in the next page).



To test your program, you can use the file we provide. Simply download and run:

python cards_test.py



And you will see if you pass all of our test cases. You can read the code inside the test file and come up with more tests if you wish.



When you are confident about your solution keep hold of it. We will release the answer via Youtube video. :)



Example:

For input:



["See-Mong Tan",

"Victoria Kirst",

"Matthew Levine",

"Eric Breck",

"Riccardo Crepaldi"]



Your result should be a dictionary looking like this:



{

 "See-Mong Tan":"Thank You! Your friends, Victoria Kirst, Matthew Levine, Eric Breck, Riccardo Crepaldi",

 "Victoria Kirst":"Thank You! Your friends, See-Mong Tan, Matthew Levine, Eric Breck, Riccardo Crepaldi",

 "Matthew Levine":"Thank You! Your friends, See-Mong Tan, Victoria Kirst, Eric Breck, Riccardo Crepaldi",

 "Eric Breck":"Thank You! Your friends, See-Mong Tan, Victoria Kirst, Matthew Levine, Riccardo Crepaldi",

 "Riccardo Crepaldi":"Thank You! Your friends, See-Mong Tan, Victoria Kirst, Matthew Levine, Eric Breck"

}