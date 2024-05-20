from SANYAMUSIC.core.bot import SANYA
from SANYAMUSIC.core.dir import dirr
from SANYAMUSIC.core.git import git
from SANYAMUSIC.core.userbot import Userbot
from SANYAMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = SANYA()
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
