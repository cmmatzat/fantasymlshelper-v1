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
# getJsonDataFromUrl( url, filepath )


################################################################################
#       CONSTANTS
################################################################################

MLS_DATA_LOCAL_PATH = "/var/www/fantasymlshelper.com/public_html/data/mls/"
MLS_DATA_BASE_URL = "https://fgp-data-us.s3.amazonaws.com/json/mls_mls/"
SQUAD_FILENAME = "squads.json"


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
    # Get files from MLS
    #=============================
    print( "Downloading data..." )
    getJsonDataFromUrl( MLS_DATA_BASE_URL + SQUAD_FILENAME, MLS_DATA_LOCAL_PATH + new_folder + SQUAD_FILENAME )
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
    folder_name = datetime.datetime.now().isoformat()
    
    #=============================
    # Try to create folder
    #=============================
    try:
        os.makedirs( MLS_DATA_LOCAL_PATH + folder_name )
        print( "New Folder: " + folder_name )
        return ( folder_name + '/' )
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
#   getJsonDataFromUrl( url, filepath )
##################################################
#   Fetch JSON data from the given URL and save
#   it locally to the given filepath.
##################################################
def getJsonDataFromUrl( url, filepath ):

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
    # End try
    
    #=============================
    # Return 'None' on failure
    #=============================    
    except ValueError:
        debugPrint( "Invalid JSON Response", "DBP_ERR_CATCH" )
        return None
    # End except

    #=============================
    # Save data to local file
    #=============================
    with open( filepath, 'w' ) as output_file:
        json.dump( json_data, output_file )
        
# End function getJsonDataFromUrl()


################################################################################
#       EXECUTABLE CODE
################################################################################
aquireNewData()
