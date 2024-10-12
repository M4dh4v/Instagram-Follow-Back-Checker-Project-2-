Basically this program will show the username of people who you follow but they do not follow you back.

Needed --> python,pip

run -- pip install -r requirements.txt

Go to accounts-ex.py -- follow the instructions there

navigate to the current directory in your terminal
run -- python main.py



----
Ignore this in the console
----

DevTools listening on .....
Created TensorFlow Lite XNNPACK delegate for CPU.
Attempting to use a delegate that only supports static-sized tensors with a graph that has dynamic-sized tensors (tensor#58 is a dynamic-sized tensor).


Anything after this will be our main code
----
Main Working
----

if we are using default -- (get_list_ver2 is running):
- You will be stopped at the followers dialog box
- You NEED to scroll down and it will automatically go to the bottom of the next batch
- Continue scrolling down which will add new element

    IF U REACH THE END OF YOUR FOLLOWERS LIST AND IT IS STUCK FOR 5 SECONDS
    THIS IS YOUR SIGN TO USE -- get_list_ver1

- If the get_list_ver2 works, the followers box automatically closes and the following dialog box will open
- Continue the same scrolling action and the following dialog box and it will automatically close the chrome application and give you the result in the console

if we are using  get_list_ver2 (YOU HAVE CHANGED THE CODE SLIGHTLY):
- You will be stopped at the followers dialog box where you need to scroll down completely to the end of the dialog box
- You are prompted if you reached the end
- Unit you answer 'y', it will continue to ask every 3 seconds
- After you answer, the followers dialog box will close and the following dialog box will open
- Do the same for following dialog box where
- You have the output on the console and the chrome application will automatically close
