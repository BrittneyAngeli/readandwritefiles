#Python program that prints out a client list
#with numbering from the file - clients.txt

def main():
    #Open the file 
    infile = open('clients.txt', 'r')

    #Client number counter 
    client_counter = 1

    #Display each client in a numbered sequence
    for client in infile:
        print(client_counter, '. ', client.rstrip('\n'), sep ='')
        client_counter += 1

    #Close the file 
    infile.close()

main()

