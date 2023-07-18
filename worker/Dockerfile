FROM python:3.9-slim-buster

# upgrade pip
RUN pip install --upgrade pip

# get curl for healthchecks
RUN apt-get update && apt-get install -y curl

# permissions and nonroot user for tightened security
# RUN addgroup --system nonroot && adduser --system --group nonroot
RUN mkdir /home/app/
WORKDIR /home/app

COPY . .

# venv
ENV VIRTUAL_ENV=/home/app/venv

# python setup
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN export FLASK_APP=app.py
# RUN pip install -r requirements.txt

CMD ["python", "transcribe.py"]