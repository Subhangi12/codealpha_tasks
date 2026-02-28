#write a function that takes a  string and returns the count vowels and consonants separately

def countVowelConso(userInput) :
    #define vowels
    vowels="aeiouAEIOU"
    
    countVowels=0
    countConsonants=0

    for eachchar in userInput :
        if(eachchar.isalpha()) :
            if(eachchar in vowels) :
                countVowels+=1
            else :    
                countConsonants+=1
    return countVowels ,countConsonants
#function call        
vowels, consonants =countVowelConso("Subhangi Kantha")
print(vowels,consonants)
