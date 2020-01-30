#Add-on type: globalPlugin
#Definition: GlobalPlugins are responsive NVDA addons that can function anywhere in the operating system. Its scope is global. 
#Functionality: It has 2 defined functionalities 1)Announcing window class name 2) Announcing the current window's Control ID
#Shortcut keys: (NVDA+pageUp,NVDA+leftArrow) for functionality-1 and (NVDA+pageDown,NVDA+rightArrow) for functionality-2
#Note: NVDA in the keyset refers to the 'insert' key in the keyboard

#------------------------------------------------start--------------------------------------------------------------------#
import globalPluginHandler #this is the class than enables working with GlobalPlugins
from scriptHandler import script #script is an instance method which is a reference made by NVDA. Reference can be by keys. 
import ui #this is used for announcing the message in form of speech 
import api #api class enables to fetch the parameters that need to be responded      

#All our code is to be placed inside a GlobalPlugin class which extends from the globalPluginHandler class.
#This is the defined Syntax for creating GlobalPlugins
class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	@script(
		description=_("Announces the window class name of the current focus object- say a current browser, file or application"),
		gestures=["kb:NVDA+pageUp","kb:NVDA+leftArrow"] #gestures array holds all defined key combinations
	)
	#when we define the script instance method, we pass a self pointer (python code standard) and gesture object
	def script_announceWindowClassName(self, gesture): 
		focusObj = api.getFocusObject() #create an object of the class which calls the window name and the class name
		name = focusObj.name #object holds the window name
		windowClassName = focusObj.windowClassName #object holds the window class name
		ui.message("class for %s window: %s" % (name, windowClassName)) #output the window class name as string

	@script(
		description=_("Announces the window control ID of the current focus object"),
		gestures=["kb:NVDA+pageDown","kb:NVDA+rightArrow"] #gestures array holds all defined key combinations
	)
	def script_announceWindowControlID(self, gesture):
		focusObj = api.getFocusObject()
		name = focusObj.name #object holds the name
		windowControlID = focusObj.windowControlID #object holds the ID
		ui.message("Control ID for current %s window: %d" % (name, windowControlID)) #output name and ID 
		
#-------------------------------------------------end--------------------------------------------------------------------#