Hmm.....So this bot basically is for fun. send daily text messages with images to people (originally intended as a meme-ified navratri wisher).
Ofc you can change the messages and images, just make sure you rename the images exactly or it will throw an error, works on one phone number, 
automatically startup with your device. although you'll need to refrain from touching your keyboard while it works. You are ofc free to edit it 
to work for longer periods.

**Make sure you have already logged on to whatsapp web once before on your primary browser and left it logged in**

Now, the setup steps -

1 - Download the files and place them in the same folder.

2 - In config.json, edit the Phone number and Imagepath to the recipient's number and file location of your images.

3 - history.json is empty, don't delete it's useful for the code.

4 - copy the "Automaticbot.bat", click win + R and open "shell:startup", paste the bat there.

It should not startup with computer and work. You might need to download the libraries mentioned in Main.py and 'pywin32'.

**This is only for windows user, linux and MacOS users must make their own automaticbot.bat for their own OS and adjust the Imagepath in config.json**

Feel free to contact me for any problems 😀


**New things to mention 🗣️🗣️🗣️**

Fixed an error i encountered to make sure the code doesn't misfire the message into wrong chat due to WhatsApp's chat recovery.
For the new update, you have two extra steps for setup.

1 - Open WhatsApp web and place your cursor on the paper clip icon (file selection). Alt-Tab to a session of Terminal in background and CTRL+V this - python -c "import pyautogui; print(pyautogui.position())". 

Put these coordinates in line 48 of Main.py


2 - Hover over the Photos/videos option in the drop menu and do the same process for line 50 pyautogui command.


*Why the changes were made?*

WhatsApp tries to open the last chat automatically upon running, it can interfere with the automation and cause the image to be sent to the wrong recipient unless forced to open a chat. (Yeah I made the automation do manual labour)

WhatsApp has a failsafe to prevent external bots from automating task , using a workaround with mouse clicks was necessary to bypass it.
