FROM python:3.6.2
EXPOSE 5000
RUN python -m pip install -U pip==9.0.1 pipenv==8.2.6
WORKDIR /sdk

# move all the packaging files in
ADD setup.py .
ADD requirements.txt .
#ADD Pip* ./

# build and cache dependencies
RUN pipenv install --python $PYTHON_VERSION

ADD . .
RUN pipenv run pip install .
CMD pipenv run python tests/server.py
