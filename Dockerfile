FROM python

ENV PIP_DISABLE_PIP_VERSON_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /app
COPY . . 
RUN python -m pip install pip==24.0
RUN pip install -r requirements.txt