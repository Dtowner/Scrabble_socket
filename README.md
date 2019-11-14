EE 407 Scrabble Project

This project folder consists of a server and client file to run the game, this readme file, a folder for the GNU dictionary and couple other python files that were used for testing different functions or methods that I used.  

The server and client can only be run on a local machine

The commands that were set up and functioning are listed below and what they do;

Hell0:  this command sends hello to both the client and the server and if the server doesn't receive hello from the client right away it closes the connection.  It also sets the base user name as the USER for the system that is running the client

QUIT: this command tells the server that the client would like to quit and responds with 'Goodbye' and prints this message on both the client and the server and closes the connection

USERSET: this command will set the new username of the client that it is executed on to a new user input.  Note: it can be anything and the username is initially the USER of the client

READY: this command sends 'READY' to the server which will send an ok command back and it will call start_game() NOTE:  even though it calls start_game() that function isn't set up to work across the socket and will only run the game on the server side.  

That is the extent of what the client and server are set to do
