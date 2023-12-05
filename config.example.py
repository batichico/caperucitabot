import logging
import os

BACKEND = "SlackV3"

BOT_DATA_DIR = r"/home/errbot/data"
BOT_EXTRA_PLUGIN_DIR = r"/home/errbot/plugins"
BOT_EXTRA_BACKEND_DIR= "/opt/errbot/backend-plugins/slackv3"

BOT_LOG_FILE = r"/home/errbot/errbot.log"
BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = (
    "U0000000001", # @duhow
)

BOT_IDENTITY = {
    "token": os.getenv("SLACK_TOKEN", "xoxb-..."),
    "signing_secret": os.getenv("SLACK_SECRET", "<hash string>"),
    "app_token": os.getenv("SLACK_APP_TOKEN", "xapp-1..."),
}

# @Midora user
BOT_PREFIX = "<@U000000002> "
BOT_PREFIX_OPTIONAL_ON_CHAT = True
BOT_ALT_PREFIXES = ("robotito",)
