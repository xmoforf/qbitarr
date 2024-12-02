FROM python:3.13-bookworm
WORKDIR /usr/src/app

RUN pip install --no-cache-dir -U setuptools wheel pip
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENTRYPOINT ["python", "-i", "./script.py"]
CMD [ ]
