I wrote a simple python program which opens the nyan cat page:
https://www.nyan.cat/index.php?cat=original in an extra window


how to convert the python file into an exe file
1) open your terminal and type in this command: 'pip install pywebview pyinstaller'
2) crate a new folder, name it something like "nyan cat" and put in the python file and if you want an .ico file called icon.ico 
3) in your explorer click in the yellow marked field <img width="811" height="77" alt="image" src="https://github.com/user-attachments/assets/52e23ee2-9cfa-4fa9-ad3e-f51424e46a24" /> and press ctrl + c to copy the path
                   paste your path here: ⬇️
5) open your terminal and type in 'cd your_path' and press enter
6) now type in 'pyinstaller --onefile --noconsole --icon=icon.ico --name "NyanCat Launcher" nyan_app.py'
7) you will find your .exe file in a folder called dist
 









