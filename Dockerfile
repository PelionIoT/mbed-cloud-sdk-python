FROM python:3.6.2
RUN apt-get update &&\
  apt-get install -y\
  python2.7\
  python3.4
EXPOSE 5000
RUN python -m pip install -U pip==9.0.1 tox==2.9.1
WORKDIR /sdk

# move all the packaging files in
ADD setup.py .
ADD requirements.txt .
ADD tox.ini .
ADD README.md .

RUN tox --notest

ADD . .
CMD tox -e $PYTHON_SDIST
