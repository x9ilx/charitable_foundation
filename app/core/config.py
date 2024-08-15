from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Благотворительный фонд поддержки котиков QRKot'
    app_description: str = (
        'Фонд собирает пожертвования на различные целевые '
        'проекты: на медицинское обслуживание нуждающихся '
        'хвостатых, на обустройство кошачьей колонии в '
        'подвале, на корм оставшимся без попечения кошкам '
        '— на любые цели, связанные с поддержкой кошачьей '
        'популяции.'
    )
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'CaMbluCeKPeTHbluKJlI04BMuPe'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    type: Optional[str] = None
    project_id: Optional[str] = None
    private_key_id: Optional[str] = None
    private_key: Optional[str] = None
    client_email: Optional[str] = None
    client_id: Optional[str] = None
    auth_uri: Optional[str] = None
    token_uri: Optional[str] = None
    auth_provider_x509_cert_url: Optional[str] = None
    client_x509_cert_url: Optional[str] = None
    email: Optional[str] = None

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
