S = str(input("Enter the string: "));
word = str(input("Enter the word: "));
S=S.replace("?","");
S=S.replace("!","");
S=S.replace(",","");


string=[]
string = S.split(' ');


def freq(string, word):
    count = 0;
    for i in string:
        if(i == word):
            count = count + 1;
    return count;
print(freq(string, word), end=' times');
