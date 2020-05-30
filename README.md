# log_in_web
Design and implement a web-based email classification
system. This project implement both web server-side code
and front-end UI (browser) code. The system should have
login/logout functions, and also be able to run the pretrained
classification Machine Learning model.

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
![Figure 1: Files structure.](https://github.com/drrdrem/log_in_web/blob/master/figure/File_struct.png){:height=50% width=50%}
**Figure 1: Files structure.**
![Figure 2: Set up information.](https://github.com/drrdrem/log_in_web/blob/master/figure/Dockerfile.png)
**Figure 2: Set up information.**

# Function
## Registration
Figure 3 shows the register page. The registration page
is the default home page of the website. One can register
an account with a unique username and a distinct email address
and then set a password. Figure 4 shows the account
duplication warning during creating a new account. The
user will be logged into the system directly once he/ she
finishes registration successfully.
![Figure 3: Registration page.](https://github.com/drrdrem/log_in_web/blob/master/figure/Register.png)
**Figure 3: Registration page.**
![Figure 4: Account duplication warning.](https://github.com/drrdrem/log_in_web/blob/master/figure/Acc_dup.png)
**Figure 4: Account duplication warning.**

## Log in
Figure 5 shows the login page. One can login based on
his/ her username and corresponding password to log into
the account. If one gives a wrong password, the web page 
will show a notification. Figure 6 is an example of incorrect
log in. One can sign out at any time through the button
on the navigation bar. The login session will be terminated
automatically if the user idles more than 10 minutes (Due
to the fact that analysis will take more than 2 minutes to
finish).
![Figure 5: Log in page.](https://github.com/drrdrem/log_in_web/blob/master/figure/Login.png)
**Figure 5: Log in page.**

![Figure 6: Incorrect login warning.](https://github.com/drrdrem/log_in_web/blob/master/figure/Incorresct_login.png)
**Figure 6: Incorrect login warning.**

### Profile
One can access his/ her profile from his/ her email address
on the right of the navigation bar after login the account.
One can also see his/ her basic information and reset
the email address and password here. Figure 7 is an example
of user profile.
![Figure 7: Profile page.](https://github.com/drrdrem/log_in_web/blob/master/figure/User_profile.png)
**Figure 7: Profile page.**

### Updating email and password
One can update his/ her password and email address
through the user profile page. Figure 8 is the page to update
the password.
![Figure 8: Update password page.](https://github.com/drrdrem/log_in_web/blob/master/figure/Update_passwor.png)
**Figure 8: Update password page.**

### Reset password via email
If one forget the password, he/ she can also access the
account by reset the password via the email. Figure 9 shows
the reset password via email page.
![Figure 9: reset password through email page.](https://github.com/drrdrem/log_in_web/blob/master/figure/Reset_email.png)
**Figure 9: reset password through email page.**

## Upload file
After logging into the account. The web page will redirect
to the upload page to upload testing data. Figure 10
shows the upload page. One can access the upload page at
any time after log into the account. The page will show the
warning if one uploaded incompatible files.
![Figure 10: Upload file.](https://github.com/drrdrem/log_in_web/blob/master/figure/Upload.png)
**Figure 10: Upload file.**

## Results’ page
After uploading the file successfully and finishing the
analysis, the web page will redirect to results’ page and
shows the analysis results. The analysis is based on the pretrained
model.Figure 11 shows an example of the results
page.
![Figure 11: Analysis results.](https://github.com/drrdrem/log_in_web/blob/master/figure/Results.png)
**Figure 11: Analysis results.**

# Unittest
We test the overall project on duplicate registration, update
the password and then log in. We also test the functionality
of page redirection. Due to the time limitation, we did not finish 
the all potentially testing and it will leave to be the future work.
