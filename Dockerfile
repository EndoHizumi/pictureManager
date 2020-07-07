from python
RUN git clone https://github.com/EndoHizumi/pictureManager.git
WORKDIR /pictureManager
RUN apt update && apt install libmagic-dev
RUN  pip install -r requirements.txt
WORKDIR /data
CMD [ "python" ,"/pictureManager/app.py"]