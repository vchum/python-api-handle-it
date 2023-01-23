FROM python:3

WORKDIR /app

RUN pip3 install radon 

RUN pip3 install json2tree

CMD ["/bin/bash", "-c","radon cc -j ./ > reports/cc/report.json; json2tree -j reports/cc/report.json -o reports/cc/report.html -t 1 "]
