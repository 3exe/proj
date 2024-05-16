from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):

    bot_token: SecretStr
    yoo_token: SecretStr
    rucapcha_token: SecretStr

    time_to_top_up: int
    max_flows: int
    wallet: str
    support: str

    class Config:

        env_file = '.env'
        env_file_encoding = 'utf-8'


config = Settings()
