################################################################################
#       generate_schedule
################################################################################
#       Version 0.0.1
#       Updated 2018-08-06
################################################################################
#       Module takes data from MLS and creates new JSON with a simple
#       fantasy schedule.
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

# generate_fantasy_schedule( )
# getMatchData( mls_match )
# getRoundData( mls_round )
# writeJsonDataToFile( data, filepath )


################################################################################
#       CONSTANTS
################################################################################

FMH_SCHEDULE_DATA_PATH = "/var/www/fantasymlshelper.com/data/public_html/data/schedule/"
MLS_DATA_LOCAL_PATH = "/var/www/fantasymlshelper.com/data/public_html/data/mls/"

MATCH_FILENAME = "rounds.json"
SCHEDULE_FILENAME = "schedule.json"
SQUAD_FILENAME = "squads.json"
VENUE_FILENAME = "venues.json"

LATEST_DATA = "latest_data.txt"
ERROR_LOG = "_error_log.txt"


################################################################################
#       FUNCTION DEFINITIONS
################################################################################

##################################################
#   generate_fantasy_schedule( )
##################################################
#   Write the given JSON data to file.
##################################################
def generate_fantasy_schedule( ):

    #=============================
    # Create new schedule dict
    #=============================
    fmh_schedule = []
    
    #=============================
    # Find latest MLS data
    #=============================
    with open( MLS_DATA_LOCAL_PATH + LATEST_DATA, 'r' ) as latest_data:
        mls_folder = latest_data.read()
    
    #=============================
    # Get latest local MLS data
    #=============================
    rounds_file = MLS_DATA_LOCAL_PATH + mls_folder + MATCH_FILENAME
    squads_file = MLS_DATA_LOCAL_PATH + mls_folder + SQUAD_FILENAME
    mls_schedule = getJsonDataFromFile( rounds_file )
    mls_squads = getJsonDataFromFile( squads_file )
    
    #=============================
    # Create round schedules
    #=============================
    for mls_round in mls_schedule:
        fmh_round = getRoundData( mls_round )
        fmh_schedule.append( fmh_round )
    # End for loop
    
    #=============================
    # Save schedule to file
    #=============================
    output_filepath = FMH_SCHEDULE_DATA_PATH + SCHEDULE_FILENAME
    writeJsonDataToFile( fmh_schedule, output_filepath )
    
# End function generate_fantasy_schedule()


##################################################
#   getMatchData( mls_match )
##################################################
#   Extract data from an MLS match and return
#   a properly formatted FMH match.
##################################################
def getMatchData( mls_match ):

    #=============================
    # Save data to local file
    #=============================
    
        
# End function getMatchData()


##################################################
#   getRoundData( mls_round )
##################################################
#   Extract data from an MLS round and return
#   a properly formatted FMH round.
##################################################
def getRoundData( mls_round ):

    #=============================
    # Create fmh round
    #=============================
    fmh_round = {}
    
    #=============================
    # Extract needed data
    #=============================
    fmh_round['round'] = mls_round['id']
    fmh_round['season'] = mls_round['type']
    fmh_round['matches'] = []
    for mls_match in mls_round['matches']:
        fmh_round['matches'].append( getMatchData( mls_match ) )
    # End for loop
        
    return fmh_round
    
# End function getRoundData()


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
generate_schedule()