FROM snakepacker/python:all AS builder

WORKDIR /code
RUN python3.11 -m venv /code/venv
ENV PATH="/code/venv/bin:$PATH"

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt


FROM snakepacker/python:3.11


WORKDIR /code/proj

COPY --from=builder /code/venv /code/venv

COPY ./proj .

ENV PATH="/code/venv/bin:$PATH"
ENV PYTHONPATH="/code/proj"

RUN python manage.py collectstatic --noinput
