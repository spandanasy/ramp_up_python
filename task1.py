def main():
    try:
        ip_stmt=input("Enter a string :")
        if not ip_stmt:
            print("Input statement is not entered,Please eneter a statement")
        elif any(s.isdigit() for s in ip_stmt):
            raise ValueError("The tatement should be only string but your statment has numbers and special characters")
        else:
            print("The string you enetered is :",ip_stmt)

        #displays the number of characters present in the statement    
        no_of_chars=len(ip_stmt)
        print("No of characters present in input string is:",no_of_chars)

        #displays the number of words present in the statement
        no_of_words=len(ip_stmt.split())
        print("No of words Present in input is :",no_of_words)

        #Displays the number of duplicate characters and words present in the statement using dictionary
        chars = {}
        for word in ip_stmt:
            if word not in chars:
                chars[word] = 1
            else:
                chars[word] += 1
        
        no_of_dupchars_count=0
        for count in chars.values():
            if count > 1:
                no_of_dupchars_count += 1
        print("The Duplicate characters are:",chars)
        print("Number of duplicate words :",no_of_dupchars_count)
        
        no_of_dups=ip_stmt.lower().split(' ')
        words = {}
        for word in no_of_dups:
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1
        no_of_dupwords_count=0
        for count in words.values():
            if count > 1:
                no_of_dupwords_count += 1
        print ("The Duplicate words are :",words)
        print("Number of duplicate words :",no_of_dupwords_count)

        #Reversing the characers of the statement
        reverse_str=ip_stmt[::-1]
        print ("The reversed character is :",reverse_str)

        #Reverse the words of the statement
        reverse_words=ip_stmt.split()
        reversed_words=' '.join(reverse_words[::-1])
        print("The reversed words are :",reversed_words)

        #The new reversed statement
        print("The New statement is :",reversed_words)

        #Removing duplicate characters from the reversed statement
        words = reversed_words.split()
        chars_new_list = []
        for word in words:
            chars_new= ""
            for char in word:
                if char not in chars_new:
                    chars_new += char
            chars_new_list.append(chars_new)
        final=' '.join(chars_new_list)
        print("After removing duplicate characters in new statement are:",final)

    except Exception as e:
        print("An error occured:",e)

if __name__=="__main__":
    main()
