from errbot import BotPlugin, botcmd
import requests
from urllib.parse import urlparse

class MidokuraSTS(BotPlugin):

    urls = [
        "https://www.midokura.com",
    ]
    
    @botcmd
    def sts_check_versions(self, msg, args):  # a command callable with !tryme
        """ Query all STS accessible endpoints and return the version. """
        data = []
        for url in self.urls:
            try:
                r = requests.get(f"{url}/actuator/version")
                data.append(f"{urlparse(url).netloc}: \`{r.json().get('app')}\`")
            except:
                data.append(f"{url} failed!")
        return "\n".join(data)
