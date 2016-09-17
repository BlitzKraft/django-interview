# Script

`get_size.py` is the script that parses the `fun-rooster-thumbnail-names.txt`
and outputs the result as specified in the problem statement. It takes no
arguments and the filename is hardcoded. That can be changed easily by changing
the `filename` variable in the script

# Server

`runserver` is a bash script that starts the server. `thumbnails` is the django
project folder. 

The server is initialized on port 3000, and can be reached by the following link:
127.0.0.1:3000

Once the page loads, a table is displayed and is sortable by clicking on the
specific column heading.
