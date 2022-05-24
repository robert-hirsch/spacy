FROM public.ecr.aws/lambda/python:3.8

RUN pip3 install -U spacy --target "${LAMBDA_TASK_ROOT}"
RUN python -m spacy download en_core_web_sm
COPY app.py ${LAMBDA_TASK_ROOT}

CMD ["app.lambda_handler"]