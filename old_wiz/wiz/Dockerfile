FROM sanicframework/sanic:LTS
RUN mkdir -p /tmp \
  && git clone git@github.com:jwoolfe/python3.git /tmp/jwoolfe \
  && mv /tmp/jwoolfe/wiz/* /srv/ \
  && rm -rf /tmp/jwoolfe
EXPOSE 8003
ENTRYPOINT [ "python3", "/srv/server.py" ]