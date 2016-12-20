import logging
import requests


DOMAIN = "tts_service"
REQUIREMENTS = ["requests"]

ATTR_PLAYER = "player"

ATTR_TEXT = "text"
DEFAULT_TEXT = "Hello World"

ATTR_VOLUME = "volume"
DEFAULT_VOLUME = 40

ATTR_API_URL = "api_url"
DEFAULT_API_URL = "http://docker.home:5005"

_LOGGER = logging.getLogger(__name__)


def setup(hass, config):

    """Setup is called when Home Assistant is loading our component."""

    def handle_say(call):

        player = call.data.get(ATTR_PLAYER)
        text = call.data.get(ATTR_TEXT, DEFAULT_TEXT)
        volume = call.data.get(ATTR_VOLUME, DEFAULT_VOLUME)
        api_url = call.data.get(ATTR_API_URL, DEFAULT_API_URL)

        _LOGGER.info("TTS: {}: {}".format(player, text))

        hass.states.set("tts_service.text", text)
        
        url = "{}/{}/say/{}/{}".format(api_url, player, text, volume)
        
        _LOGGER.info("URL: {}".format(url))
        r = requests.get(url)

    hass.services.register(DOMAIN, "say", handle_say)
    return True
