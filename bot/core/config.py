# Copyright (c) 2026 tusar404
# Licensed under the MIT License.


import os
import sys

from dotenv import load_dotenv

from .. import LOGGER

load_dotenv()


class Config:
    def __init__(self):
        self.api_id = int(os.getenv("API_ID", "0"))
        self.api_hash = os.getenv("API_HASH", "")
        self.bot_token = os.getenv("BOT_TOKEN", "")
        self.bot_id = int(self.bot_token.split(":")[0]) if ":" in self.bot_token else 0

        self.api_url = os.getenv("API_URL", "https://api.arcmusic.fun").rstrip("/")
        self.api_key = os.getenv("API_KEY", "")

        self.mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")

        self.owner_id = int(os.getenv("OWNER_ID", "0"))
        self.sudo_users = {
            int(x) for x in os.getenv("SUDO_USERS", "").replace(" ", "").split(",") if x
        }
        self.sudo_users.add(self.owner_id)

        self.require_all({
            "API_ID": self.api_id,
            "API_HASH": self.api_hash,
            "BOT_TOKEN": self.bot_token,
            "API_URL": self.api_url,
            "API_KEY": self.api_key,
            "MONGO_URI": self.mongo_uri,
            "OWNER_ID": self.owner_id,
        })

    def require_all(self, values: dict) -> None:
        missing = [name for name, value in values.items() if not value]
        if not missing:
            return
        LOGGER.error("Missing required environment variable(s): %s", ", ".join(missing))
        LOGGER.error("Copy sample.env to .env and fill these in before starting the bot.")
        sys.exit(1)


config = Config()
