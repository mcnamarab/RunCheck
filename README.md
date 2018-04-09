# RunCheck

RunCheck is an application used for monitoring MLB scores.  

### What Does it Do
RunCheck was inspired by and built to help organize a baseball office pool. The program is simple to use, it only requires a few setup steps and then you're done. ```RunCheck``` can be used via the CLI or on a scheduel to help you gather baseball scores based on various filters

### Get Started with RunCheck
RunCheck requires a few steps to get started.  You'll want to start  in the directory you want the application to be stored

#### Install RunCheck
1. Clone the ```RunCheck``` repo from GitHub
```sh
$ git clone https://github.com/mcnamarab/RunCheck.git
```

2. Once you have the repo cloned, you'll want to install the dependencies
```sh
$ cd RunCheck
$ pip install -r requirements.txt
```

Now that you have ```RunCheck``` installed, where you go next depends on how you want to use the application.  
- If you want to use the program via a terminal head to the bottom of the instructions.  
- If you want to set it up to run automatically, continue on below.

#### Using RunCheck on a Schedule
Get into the proper directory
```sh
$ cd auto
```

Modify and personalize the setup file.  Simply fill in the requested fields. *Make sure you save the file when you're done!*
```sh
$ sudo nano setup.py
```

At this point, the program is all setup to run via the manage.py file but we will build a crontab to automate the process. For my example, the process will run every Monday at 8 AM, but you can set it however you like.  All of the crotab instrcutions should be at the top of the crontab file.  If not here is ome more info about crontab formatting.
```sh
$ cd ..
$ crontab -e
```

Add this line to the bottom of the crontab file.  For my example, the process will run every Monday at 8 AM, but you can set it however you like.  All of the crotab instrcutions should be at the top of the crontab file.  If not here is ome more info about crontab formatting. Make sure the path to your manage.py file is correct *Be sure to save before exiting*
```
0 8 * * 1 /RunCheck/auto/manage.py
```

You're all set! Look for an email with your results at whatever time you specified. If your excited to try it out now, read the instructions below to try the program via the terminal.

#### Using RunCheck via the Command Line
Get into the proper directory
```sh
$ cd auto
```

Run the program with
```sh
$ python results.py
```
Then just answer the questions and get your results!  


### Where To From Here
This project started a simple idea and I hope continue to develop this application.  Down the road I hope to add a GUI or deploy the logic in a Flask app.








### Credits
RunCheck is powered by Zach Panzarino's ```mlbgame``` API.  Much thanks to him for his awesome work









License
----
MIT License

Copyright (c) 2018 Brendan McNamara


