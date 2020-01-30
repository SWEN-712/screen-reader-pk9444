# NVDA_globalPlugins
 
## Description
This is an example of basic NVDA addons. The type of add-ons implemented is the GlobalPlugin. These are the type of addons that can function anywhere in the Operation System and have an OCR capability.
An add-on is an added functionality that offers different kinds of features. All NVDA add-ons are python scripts

## Basic GlobalPlugins Created
1. Date and Time Announcer 
2. NVDA Version Announcer
3. Window Class Name Announcer
4. Window Name and Control ID Announcer

First two add-ons are defined in example2.py file whereas the other two are defined in the example3.py file.

## Requirements
1. NVDA Application
2. Python 3.7 (32-bit) 

## Functionalities
1. Enables shortcut key combinations to be operated from anywhere in the OS as it's scope is global. 
2. Multiple key combinations enabled for all add-ons.
3. Can be customized by the developer as per the requirements.

## Running the add-ons

### Setting up NVDA
1. Start NVDA on your system.
2. Press (NVDA+n), i.e. (insert+n) to open the NVDA menu dialog box.
3. Then, go to preferences. In Preferences go to Settings.
4. Enable the Scratchpad Directory. 
5. Open the directory. It will be something like this - C:\Users\[your username]\AppData\Roaming\nvda - in there will be Scratchpad 

### Creating Python Scripts
1. Create the two add-on Scripts or copy-paste the code in a text editor (preferably Notepad++). 
2. Then save them as .py files in the GlobalPlugins subdirectory in the aforementioned Scratchpad directory.
3. Restart NVDA. You can do that by pressing (insert+q). 

### Running the add-ons 
Following are the key combinations for the GlobalPlugin add-ons: 
1. To get date and time, you either press (NVDA+t) or (NVDA+d).
2. To get the current version of the NVDA, press (NVDA+shift+v).
3. To get the current window's class name, press (NVDA + leftarrow) or (NVDA + pg up).
4. To get the current window's name and Control ID, press (NVDA + rightarrow) or (NVDA + pg down).
