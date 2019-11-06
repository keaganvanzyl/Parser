def findDuplicates(FileName):
    print('Finding duplicate tracks in %s...' fileName)
    # read in a playlist
    plist = plistlib.readPlist(fileName)
    # get the tracks from the Tracks dictionary
    tracks = pList['Tracks']
    # create a track name dictionary
    trackNames = {}
    # iterate through the tracks
    for trackID, track in tracks.items():
        try:
            name = track['name']
            duration = track['Total Time']
            # look for existing entries
            if name in trackNames:
                # if name and duration match, increment the count
                # round the track length to the nearest second
                if duration//1000 == trakNames[name][0]//1000:
                    count = trackNames[name][1]
                    trackNames[name] = (duration, count+1)
            else:
                # add dictionary entry as tuple(duratoion count)
                trackNames[name] = (duration, 1)
        except:
            # ignore, catching songs which dont have a name or duration
            pass
