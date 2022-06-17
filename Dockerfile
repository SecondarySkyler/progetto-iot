FROM main_py

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /app

ADD . /app/

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

ENV NAME water_station

CMD ["python3", "main.py"]