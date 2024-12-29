from PROFESSORxSOURABH.core.bot import SUHANI
from PROFESSORxSOURABH.core.dir import dirr
from PROFESSORxSOURABH.core.git import git
from PROFESSORxSOURABH.core.userbot import Userbot
from PROFESSORxSOURABH.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = SUHANI()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
