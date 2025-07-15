"""
Alembic migration environment

‣ Uses a synchronous DB URL for migrations to avoid
  `MissingGreenlet` errors when the main app runs async.
‣ Falls back to the async DATABASE_URL if you haven’t set the
  sync one yet, so migrations will still run for SQLite, etc.
"""

from logging.config import fileConfig
import os
import sys
from pathlib import Path

from sqlalchemy import create_engine, pool
from alembic import context

# ------------------------------------------------------------------
# Add the backend/app directory to PYTHONPATH so imports work
# ------------------------------------------------------------------
sys.path.append(str(Path(__file__).resolve().parent.parent / "app"))

from app.config import settings     # noqa: E402
from app.models import Base         # noqa: E402

# ------------------------------------------------------------------
# Alembic Config object (for .ini options, logging, etc.)
# ------------------------------------------------------------------
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ------------------------------------------------------------------
# Tell Alembic which metadata to look at for autogeneration
# ------------------------------------------------------------------
target_metadata = Base.metadata

# ------------------------------------------------------------------
# Helper: choose a **sync** DB URL for Alembic
# ------------------------------------------------------------------
SYNC_DB_URL = os.getenv(
    "ALEMBIC_DATABASE_URL",
    # Fallback: strip the async driver if one is present
    settings.database_url.replace("+asyncpg", "")
)


# ------------------------------------------------------------------
# OFFLINE migrations (emit SQL to stdout / files)
# ------------------------------------------------------------------
def run_migrations_offline() -> None:
    context.configure(
        url=SYNC_DB_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


# ------------------------------------------------------------------
# ONLINE migrations (apply directly to DB)
# ------------------------------------------------------------------
def run_migrations_online() -> None:
    connectable = create_engine(SYNC_DB_URL, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


# ------------------------------------------------------------------
# Choose mode
# ------------------------------------------------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
