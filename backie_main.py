import logging
import shutil
import os
import arrow
import threading
import time

"""
 Skipping OOP, should (;)) be a fairly simple program, and thus using OOP would be overkill
"""

# Reference to a logger object
logger = logging.getLogger('backie_debugger')

# Set the logging severity to the lowest, DEBUG, which will allow us to log anything we want
logger.setLevel(logging.DEBUG)

# Handler which will log DEBUG events to the file below
fh = logging.FileHandler("C:/Scripts/logs/backie_debug.log")
fh.setLevel(logging.DEBUG)

# Create a formatter for our handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add the formatter above to our 'fh' handler
fh.setFormatter(formatter)

# Finally, add our handler to our logger
logger.addHandler(fh)

"""
 We only want to backup once a day so running the script and having a process up permanently is a "waste", instead
 it will be a schedueled task that will run once a day.
"""

# Retrieve today's date in a "file" appropriate format, this will be appended to the backed up file name
todays_date = arrow.utcnow().format("YYYY_MM_DD")
logger.debug("Today's date is set to: {0} ".format(todays_date))

# Directory that we want to back up, always the same dir in this case
dir_to_backup = "C:/Scripts/"
logger.debug("Source dir is set to: {0}".format(dir_to_backup))

# Network drive to serve as our backup location
# Right now, temporarily using a personal network drive until a better solution will be found
backup_dst = "U:/Scripts_BackUP/Scripts_{0}".format(todays_date)
logger.debug("Destination dir is set to: {0}".format(backup_dst))

# Backup source to destination dir, with "if exist" check, if exist, remove it and then update with the new dir content
def execute_backup(source_dir, destination_dir):
    if dir_exist(destination_dir):
        try:
            shutil.rmtree(destination_dir)
            logger.debug("Removed dir {0}".format(destination_dir))
        except (FileNotFoundError, NotADirectoryError, PermissionError) as e:
            logger.debug("Error occured: {0}".format(e))
    shutil.copytree(source_dir, destination_dir)
    logger.debug("Finished backing up dir {0}".format(destination_dir))

# Check whether the destination dir already exist and return True or False
def dir_exist(dir_path):
    if os.path.isdir(dir_path):
        logger.debug("Dir {0} already exist".format(dir_path))
        return True
    else:
        logger.debug("Dir {0} does not exist".format(dir_path))
        return False

execute_thread = threading.Thread(group=None, target=execute_backup, args=(dir_to_backup, backup_dst))
execute_thread.start()










