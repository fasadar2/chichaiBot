FROM python
LABEL authors="fasadar"
LABEL description="Telegram Bot for ChiChai"
LABEL homepage="https://github.com/fasadar/telegram-bot"
LABEL license="MIT"
LABEL maintainer="fasadar"
LABEL version="1.0"

WORKDIR /app
COPY requirements.txt ./
RUN python -m pip install -r requirements.txt
COPY . .
ENTRYPOINT ["python"]
CMD ["./launchBot.py"]

