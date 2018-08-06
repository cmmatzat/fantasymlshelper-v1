################################################################################
#       fetch_mls_data
################################################################################
#       Version 0.0.1
#       Updated 2018-07-25
################################################################################
#       Module provides functionality to copy all relevant json data from
#       MLS needed for fantasy analysis. This is the raw data directly from
#       MLS, and as such, is not ready to be used in the web application.
################################################################################


################################################################################
#       LIBRARIES
################################################################################
import datetime
import json
import os
import requests


################################################################################
#       FUNCTION LIST
################################################################################

# aquireNewData()
# generateNewFolder()
# getJsonDataFromUrl( url )
# writeJsonDataToFile( data, filepath )


################################################################################
#       CONSTANTS
################################################################################

MLS_DATA_LOCAL_PATH = "/var/www/fantasymlshelper.com/data/public_html/data/mls/"
MLS_DATA_BASE_URL = "https://fgp-data-us.s3.amazonaws.com/json/mls_mls/"

STAT_EXTENSION = "stats/"
PLAYER_EXTENSION = "players/"

MATCH_FILENAME = "rounds.json"
PLAYER_FILENAME = "players.json"
SQUAD_FILENAME = "squads.json"
VENUE_FILENAME = "venues.json"

STAT_FILENAME = "{}.json"


################################################################################
#       FUNCTION DEFINITIONS
################################################################################

##################################################
#   aquireNewData( )
##################################################
#   Create a new folder out of the current
#   timestamp. This allows for archiving of
#   data. Return the name of the created folder
#   if successful, or pass along OSError.
##################################################
def aquireNewData( ):

    #=============================
    # Attempt to create folder
    #=============================
    try:
        new_folder = generateNewFolder()
    # End try
    
    #=============================
    # Report failure if needed
    #=============================
    except OSError:
        print("ERROR: Folder creation failed.")
        return
    # End except
    
    #=============================
    # Get squad files from MLS
    #=============================
    print( "Fetching squads..." )
    mls_url = MLS_DATA_BASE_URL + SQUAD_FILENAME
    local_path = MLS_DATA_LOCAL_PATH + new_folder + SQUAD_FILENAME 
    squads = getJsonDataFromUrl( mls_url )
    writeJsonDataToFile( squads, local_path )

    #=============================
    # Get venue files from MLS
    #=============================
    print( "Fetching venues..." )
    mls_url = MLS_DATA_BASE_URL + VENUE_FILENAME
    local_path = MLS_DATA_LOCAL_PATH + new_folder + VENUE_FILENAME 
    venues = getJsonDataFromUrl( mls_url )
    writeJsonDataToFile( venues, local_path )

    #=============================
    # Get match files from MLS
    #=============================
    print( "Fetching matches..." )
    mls_url = MLS_DATA_BASE_URL + MATCH_FILENAME
    local_path = MLS_DATA_LOCAL_PATH + new_folder + MATCH_FILENAME
    rounds = getJsonDataFromUrl( mls_url )
    writeJsonDataToFile ( rounds, local_path )
    for rnd in rounds:
        try:
            for match in rnd['matches']:
                mls_url = MLS_DATA_BASE_URL + STAT_EXTENSION + STAT_FILENAME.format( match['id'] )
                local_path = MLS_DATA_LOCAL_PATH + new_folder + STAT_EXTENSION + STAT_FILENAME.format( match['id'] )
                match = getJsonDataFromUrl( mls_url )
                writeJsonDataToFile( match, local_path )
            # End for loop
        # End try

        except KeyError:
            print("    Bad Match")
        # End except
    # End for loop

    #=============================
    # Get match files from MLS
    #=============================
    print( "Fetching players..." )
    mls_url = MLS_DATA_BASE_URL + PLAYER_FILENAME
    local_path = MLS_DATA_LOCAL_PATH + new_folder + PLAYER_FILENAME
    players = getJsonDataFromUrl( mls_url )
    writeJsonDataToFile ( rounds, local_path )
    for player in players:
        try:
            mls_url = MLS_DATA_BASE_URL + STAT_EXTENSION + PLAYER_EXTENSION + STAT_FILENAME.format( player['id'] )
            local_path = MLS_DATA_LOCAL_PATH + new_folder + STAT_EXTENSION + PLAYER_EXTENSION + STAT_FILENAME.format( player['id'] )
            player = getJsonDataFromUrl( mls_url )
            writeJsonDataToFile( player, local_path )
        # End try

        except KeyError:
            print("    Bad Player")
        # End except
    # End for loop

    print( "Data download complete." )
    
    return
# End function aquireNewData()


##################################################
#   generateNewFolder( )
##################################################
#   Create a new folder out of the current
#   timestamp. This allows for archiving of
#   data. Return the name of the created folder
#   if successful, or pass along OSError.
##################################################
def generateNewFolder( ):

    #=============================
    # Generate folder name
    #=============================
    folder_name = datetime.datetime.now().isoformat() + '/'
    
    #=============================
    # Try to create folders
    #=============================
    try:
        os.makedirs( MLS_DATA_LOCAL_PATH + folder_name )
        os.makedirs( MLS_DATA_LOCAL_PATH + folder_name + STAT_EXTENSION )
        os.makedirs( MLS_DATA_LOCAL_PATH + folder_name + STAT_EXTENSION + PLAYER_EXTENSION )
        print( "New Folder: " + folder_name )
        return ( folder_name )
    # End try
    
    #=============================
    # Pass along exceptions
    #=============================
    except OSError:
        pass
    # End except
    
    return
# End function generateNewFolder()


##################################################
#   getJsonDataFromUrl( url )
##################################################
#   Fetch JSON data from the given URL and return
#   a JSON object with the data.
##################################################
def getJsonDataFromUrl( url ):

    #=============================
    # Fetch raw data from URL
    #=============================
    response = requests.get( url )
    
    #=============================
    # Try to decode and load data
    #=============================
    try:
        decoded_response = response.content.decode( 'utf-8' )
        json_data = json.loads( decoded_response )
        return json_data
    # End try
    
    #=============================
    # Return 'None' on failure
    #=============================    
    except ValueError:
        print( "  Invalid JSON Response" )
        return None
    # End except
        
# End function getJsonDataFromUrl()


##################################################
#   writeJsonDataToFile( data, filepath )
##################################################
#   Write the given JSON data to file.
##################################################
def writeJsonDataToFile( data, filepath ):

    #=============================
    # Save data to local file
    #=============================
    with open( filepath, 'w' ) as output_file:
        json.dump( data, output_file )
    # End with
        
# End function writeJsonDataToFile()


################################################################################
#       EXECUTABLE CODE
################################################################################
aquireNewData()
