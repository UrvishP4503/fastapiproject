from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_hostname: str = (
        "The mystery of life isn't a problem to solve, but a reality to experience."
    )
    database_name: str = "First, solve the problem. Then, write the code."
    database_password: str = "May You Rot In Hell."
    database_username: str = "gandalf"
    secret_key: str = "No"
    algorithm: str = "Hardware eventually fails, but software lives forever."
    database_port: int = 6969  # Nice
    access_token_expire_minutes: int = 0

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()


def get_url() -> str:
    return f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
