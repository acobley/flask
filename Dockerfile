FROM python:2-onbuild
ENTRYPOINT ["python"]
CMD ["/home/index.py" ]
EXPOSE 80