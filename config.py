import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "28294093"))
API_HASH = getenv("API_HASH", "f24d982c45ab2f69a6cb8c0fee9630bd")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7569306898:AAHYH63zVYJtl_qIw31Lvs87wXu69c3127I")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://pallavimusic7:XH8zoUxHMuhl4v4i@cluster0.kycoyiq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 20000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002302799359))

# Get this value from @purvi_music_bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 8142003954))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/ifgovtjoftibcdjpvd8nfiokbfobffob0vrb8bd/mtv",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", "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"
)  # Fill this variable if your upstream repository is private

YTPROXY_URL = getenv("YTPROXY_URL", 'https://tgapi.xbitcode.com') ## E.G https://yt.okflix.
YT_API_KEY = "xbit_0000968756403419024924"
COOKIES_URL=getenv("COOKIES_URL" , "https://gist.githubusercontent.com/sparrow9616/f29fc6588086a3c72d92dd9c03773350/raw/4229f3f4aab4a6693fc0794d136d30f54d67ae85/gistfile1.txt")

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/RiyaUpdates")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Kittusupport")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @king_string_session_bot on Telegram
STRING1 = getenv("STRING_SESSION", "BQGajcYAOmI5qsE80u8sgT32CY9E3tXeHfrFPn63h-V1NagerXTVElM1vxKV_Gc6XBdYzQTOXE0JPz4FV_pLnnmiDrQ1P8mzuDjCq3_Zf_wV3JMcqrhK1XNUkvtJQ5TGqV6Gn9g9zlhHd2o8fojJj9GCr_dMUAN5BcQ-vkeGYT-XnhcoPztPUKyqB6kKXSUnprb09QHiO5hfoEYNOCaNWVFagyr9ds99R3qsRD1zQmnqA45HER_DtwjkIQb4shTTGk2MRgcdESNpJoe8fmWn-XUilEfSUg2DaeUuHUWlDOZpC00BgIvPSUwYiJoto4nYoYDSAeQ2gRatGyC4yAUIxOu1CT7wWgAAAAHHSubSAA")
STRING2 = getenv("STRING_SESSION2", "BQGajcYALbKzNP8g15WSFFtMMoJQreIMhie6irfMkrcLFMqJ5Vllw5bv66TkgLl6ZzC6xTeIpNDvtzYkT1mzD6xo6geEofXG4_BWw5GQ2cbExv1EyF6M7NZjJSRy60TNrQyo_NnUHoZHD6V_N3jQko4VWRNIQ1RNwyk_Xd4B1yViZ1r6otWKysqgk42ViZvkXmXjDShK2nllGABoqbzUQ3o1CLkQymgiI02pnrTm8zuynDl2cgf4Id4CfpR_qYwNP9bmdeXyexAn3DuLpiQbkwfOmcYoN6atTdajDrtx0JU_SxGR1-eZdMD1DVbxpnuiTMPbmrU348biV-C3BFCEGb2kspH85QAAAAHKXA1NAA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/f1zi29.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/bdcf5x.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/bdcf5x.jpg"
STATS_IMG_URL = "https://files.catbox.moe/bdcf5x.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/bdcf5x.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/bdcf5x.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/bdcf5x.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/bdcf5x.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/bdcf5x.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/bdcf5x.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/bdcf5x.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/bdcf5x.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
