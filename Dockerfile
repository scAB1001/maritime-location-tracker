FROM python:3.10

# 1) Dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgeos-dev \
    gdal-bin \
    libgdal-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

ENV POETRY_VERSION=2.0.0

# 2) Install Poetry & immediately use it
RUN set -ex \
    && curl -k -sSL https://install.python-poetry.org | python - \
    && export PATH="/root/.local/bin:$PATH" \
    && poetry --version

# 3) *Now* set ENV PATH for subsequent RUNs
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry install --no-root

COPY . /app/

EXPOSE 8000

CMD ["poetry", "run", "gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
