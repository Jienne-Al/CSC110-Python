'''Write a program that asks the user to input a word, then counts the number of letters
that are vowels a,e,i,o,u in that word. Ignore uppercase vowels A,E,I,O,U.

Sometimes the letter y will also count as a vowel, but only if it occurs at the very end of a word.
(Grammatically this rule is occasionally incorrect: gyrate has three vowels, but we’re ignoring such cases here.)

inebriate contains five letters that are vowels: i,e,i,a,e.
quickly contains three vowels: u,i,y where y is the last letter in the word
Kanye will only count as two vowels: a,e. We are not counting y because it isn’t the last letter in the word.
Your code should print out a full sentence: “The number of vowels in ‘computer’ equals 3.”

Test word: Howdydoody has 4 vowels'''

word=input("Enter a word  ")
N=len(word)
c=0
for i in word:
    if i in ['a','e','i','o','u']:
        c+=1

if word[N-1]=='y':
        c+=1
print('The number of vowels in "'+word+'" equals',c)