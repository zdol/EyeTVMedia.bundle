import datetime, os, time, string, plistlib
                                                                            # import logging, random
# unicodize function
def unicodize(s):
  filename = s
  if os.path.supports_unicode_filenames:
    try: filename = unicode(s.decode('utf-8'))
    except: pass
  return filename

def Start():
  pass
  
class PlexEyeTVContent(Agent.Movies):
  name = 'EyeTV Media'
  languages = [
    Locale.Language.NoLanguage
  ]
  primary_provider = True
  fallback_agent = False
  accepts_from = None
  contributes_to = None

  def search(self, results, media, lang, manual):
    
    # Compute the GUID based on the media hash.
    part = media.items[0].parts[0]
    recording_GUID = part.hash

    # get filename and modification time
    filename = unicodize(part.file)
                                                                        # mod_time = os.path.getmtime(filename)

    try:
        # get filename without .mpg extension
        basefile,junk = string.split(filename,".mpg")
        # get the .eyetvr plist file to extract metadata from
        pl = plistlib.readPlist(basefile + ".eyetvr")
        # get only the metadata needed at this point
        recording_year = pl["actual start time"].year
        recording_title = pl["info"]["recording title"]

        results.Append(MetadataSearchResult(
                    id = recording_GUID,
                    name = recording_title,
                    year = recording_year,
                    score = 100,
                    lang = lang
                  ))
    except : pass
                                                                        # results.Append(MetadataSearchResult(id = 'null', score = 100))

  def update(self, metadata, media, lang):
    # Compute the GUID based on the media hash.
    part = media.items[0].parts[0]
    recording_GUID = part.hash

    # get filename and modification time
    filename = unicodize(part.file)
                                                                        # mod_time = os.path.getmtime(filename)
                                                                        #path = os.path.dirname(media.items[0].parts[0].file)
                                                                        #date = datetime.date.fromtimestamp(mod_time)
    try:
        # get filename without .mpg extension        
        basefile,junk = string.split(filename,".mpg")
        # get the .eyetvr plist file to extract metadata from
        pl = plistlib.readPlist(basefile + ".eyetvr")

        # path = os.path.dirname(part.file)
        thumb = basefile + ".tiff"
        poster_data = Core.storage.load(thumb)
        # extract various helpful attributes from eyetv recording plist
        recording_year = pl["actual start time"].year
        recording_displayTitle = pl["display title"]
        recording_channelName = pl["channel name"]
        recording_description = pl["info"]["description"]
        recording_availableOn = pl["actual start time"].date()
        recording_duration = int(pl["actual duration"]*1000)
        recording_title = pl["info"]["recording title"]
    
        # initialize variables
        finalSummary = ""
        channel = ""
        dateformatted = ""
        separator = " • "
        recording_info = ""

        # Prepare description according to preferences
        if Prefs['showdate']:
            df = Prefs['dateformat']
            dateformatted = pl["actual start time"].strftime(df)
            recording_info = dateformatted

        if Prefs['showchannel']:
            channel = recording_channelName + " • "
            recording_info = recording_channelName
            if Prefs['showdate']:
                recording_info = recording_channelName + " • " + dateformatted

        if Prefs['showchannel'] or Prefs['showdate']:
            recording_info = recording_info + " \n"

        finalSummary = recording_info + recording_description

        # set metadata
        metadata.title = recording_title
        metadata.year = recording_year
        metadata.originally_available_at = recording_availableOn
        metadata.duration = recording_duration
        metadata.summary = finalSummary
        metadata.posters["poster"] = Proxy.Media(poster_data)

    except : pass