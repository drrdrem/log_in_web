# log_in_web

# Docker
The final.tar is the docker file that contains the website,
the port is 5000 on docker side, please load the image and
type the locoalhost: ”forwarding-port” to load the web.
If one cannot load the docker image properly, one can
still access the web from source code by running ”run.py”
and type the url to run the webpage locally. Figure 1 is
the tree structure of files. The environment requirements
can be found in requirements.txt file. The overall running
procedure can be found on Figure 2. Folder ”users” contains
all user-related source code. Folder ”model” contains all
pre-trained model related source code.
One can also create a docker image based on the Dockerfile.
The framework of the project is based on Flask with
Python.

# Function
## Registration
Figure 3 shows the register page. The registration page
is the default home page of the website. One can register
an account with a unique username and a distinct email address
and then set a password. Figure 4 shows the account
duplication warning during creating a new account. The
user will be logged into the system directly once he/ she
finishes registration successfully.

# Log in
Figure 5 shows the login page. One can login based on
his/ her username and corresponding password to log into
the account. If one gives a wrong password, the web page 
will show a notification. Figure 6 is an example of incorrect
log in. One can sign out at any time through the button
on the navigation bar. The login session will be terminated
automatically if the user idles more than 10 minutes (Due
to the fact that analysis will take more than 2 minutes to
finish).
