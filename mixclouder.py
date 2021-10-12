"""
    URY Mixclouder2

    Takes recent shows and publishes them to Mixcloud
"""

import enum


class TimeslotUploadState(enum.Enum):
    """
        Enum of the states a timeslot can be in for its upload status
        The enum value is what will be entered in the DB
        except Uploaded, where the URL will be in place
    """
    REQUESTED = "Requested"
    QUEUED = "Queued"
    OFF_AIR = "Skipped - Off Air"
    FORCE_UPLOAD = "Force Upload"
    PLAYED_OUT = "Played Out"
    UPLOADED = "Uploaded"


def main():
    """
    Steps

    1. Set up a logger - we need this for debugging when it breaks
    2. Ask API for shows to process
    3. Check loggerng actually works - don't attempt to process shows if it doesn't
    4. For each timeslot:
        1. See if we're going to upload it
        2. Request and wait for the log
        3. Fix the tracklist if neccesary
        4. Uplaod to mixcloud

    """

    ...


if __name__ == "__main__":
    main()
