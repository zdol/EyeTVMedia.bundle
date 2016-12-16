EyeTVMedia.bundle
=====
EyeTVMedia.bundle is a plugin for Plex Media Server. It scans `.eyetv` files (EyeTV Recordings) and provides basic information and thumbnails to Plex. This is not meant to be used to stream live TV.

###Installation:

Rename downloaded file if necessary to `EyeTVMedia.bundle` and copy to `~/Library/Application Support/Plex Media Server/Plug-ins` folder on Mac or respective plugin location on other systems.

###Usage:

Make a new Library in Plex Media Server. Select type "Movies". Add a folder which contains `.eyetv` files. Under "Advanced" choose Agent: EyeTV Media.

###Caution:

Do not add the default folder that contains the `Live TV Buffer.eyetv` file (file exists only while TV app is running) - this will cause Plex to constantly scan for new files. As a better practice, move completed recordings to another folder than the default `EyeTV Archive` folder, or try keeping the Live TV Buffer in RAM (See EyeTV Recording settings.)

####Disclaimer

"EyeTVMedia.bundle" plugin is not developed by Elgato or Geniatech. The developer of this plugin is not in any way affiliated with Elgato or Geniatech. Please do not ask Elgato/Geniatech for help with or support regarding this plugin.

*All trademarks and copyrights belong to their respective owners.*

**This plugin is provided for free, as-is with no warranties.**
   

