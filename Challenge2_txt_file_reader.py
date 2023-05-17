import string
  
# Open the txt file in read mode
textfile = open("plp.txt", "r")
# print(text)

# Create an empty dictionary
dictionary = dict()
print(dictionary) 
  
  #creating a function 
def reader():
            # Loop through each line of the file
        for line in textfile:
            
            # print(line)
            
        #     # Remove the leading spaces and newline character
            line = line.strip()
            # print(line)
        
        #     # Convert the characters in line to lowercase characters
        #    
            line = line.lower()
            # print(line)
        
        #     # Remove the punctuation marks from the line
            line = line.translate(line.maketrans("", "", string.punctuation))
            # print(line)
        
        #     # Split the line into words
            words_list = line.split(" ")
            # print(words)
        #     # Iterate over each word in line
            for word in words_list:
                # Check if the word is already in dictionary
                if word in dictionary:
                    # Increment count of word by 1
                    dictionary[word] = dictionary[word] + 1
                else:
                    # Add the word to dictionary with count 1
                    dictionary[word] = 1
                
        #sort accoding to elements with higest number
        sorted_list = sorted(dictionary.items(),key= lambda x:x[1], reverse=True)
      
        #get the first ten elements from sorted list
        res = sorted_list[:10]
        
        for x in res:
            print(x)
            
           
reader()