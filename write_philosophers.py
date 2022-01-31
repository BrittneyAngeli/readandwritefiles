#This program writes three lines of data to a file 
def main():

    #Open a file named philosophers.txt
    outfile = open('philosophers.txt', 'w')

    #Write the names of three philosophers to the file - 
    #John Locke, David Hume, and Edmund Burke 
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    #Close the file 
    outfile.close()

#This function adds user's name to the text file
def add_my_name():
    
    #Open a file named philosophers.txt to append 
    outfile = open('philosophers.txt', 'a')

    #Append my own name to the file 
    outfile.write('Brittney Solorio')

    #Close the file 
    outfile.close()

#Call the main and add_my_name functions
main()
add_my_name()