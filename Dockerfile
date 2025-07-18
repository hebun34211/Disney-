FROM  python3.9-nodejs20-alpine


RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg git && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install -U uv && uv pip install --system -e .

CMD ["ArchMusic"]

