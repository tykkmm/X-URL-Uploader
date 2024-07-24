import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = "7355006985:AAEY8ijg4CP-8GgcliRGJja87Tby78QT7To"
    # The Telegram API things
    APP_ID = "29426486"
    API_HASH = "d71ad4ec048ab41677a1a439b21ff0c9"
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = "5976437467, 6486777792, 959184369"
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = "https://telegra.ph/file/a89b725e6e1235b606f0d.jpg"
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "https://SU2TuiBYWmMoNiNYPWuv2YXT:s799YY2jGXzHSWmWLJJQ5bye@in123.nordvpn.com:89")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = ""
