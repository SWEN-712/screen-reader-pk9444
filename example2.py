#Add-on type: globalPlugin
#Definition: GlobalPlugins are responsive NVDA addons that can function anywhere in the operating system. Its scope is global. 
#Functionality: It has 2 defined functionalities 1)Announcing NVDA versionInfo 2) Announcing the current data and time
#Shortcut keys: (NVDA+leftArrow) for functionality-1 and (NVDA+rightArrow) for functionality-2
#Note: NVDA in the keyset refers to the 'insert' key in the keyboard

#---------------------------------start--------------------------------------------------------#
import globalPluginHandler #this is the class than enables working with GlobalPlugins
from scriptHandler import script #script is an instance method which is a reference made by NVDA. Reference can be by keys.
import ui #this is used for announcing the message in form of speech 
import versionInfo #this is class that calls the version object


#All our code is to be placed inside a GlobalPlugin class which extends from the globalPluginHandler class.
#This is the defined Syntax for creating GlobalPlugins
class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	@script(gesture="kb:NVDA+shift+v") #the key combination insert+shift+v gives the version info of NVDA
	def script_announceNVDAVersion(self, gesture):
		ui.message(versionInfo.version)
		
	@script(
	description = ("Describes current date and time")
	category=inputCore.SCRCAT_MISC,
	gestures = ["kb:NVDA+t", "kb:NVDA+d"] #the key combination insert+t or insert+d gives the date and time
	)
	def script_sayDateTime(self,gesture):
	
#---------------------------------end--------------------------------------------------------#