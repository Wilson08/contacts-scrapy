FROM debian:buster

ADD contacts /opt/contacts

RUN apt-get update && \
    apt-get install --assume-yes --no-install-recommends \
            gcc \
            libffi-dev \
            libssl-dev \
            libxml2-dev \
            libxslt1-dev \
            python3-pip \
            python3-dev \
            zlib1g-dev \
            && \
    rm -rf /var/cache/apt/* /var/lib/apt/lists/* && \
    rm -rf /tmp/* /var/tmp/*

RUN python3 -m pip install --no-cache-dir --upgrade \
        setuptools \
        wheel \
        && \
    python3 -m pip install --no-cache-dir --upgrade scrapy

CMD python3 /opt/contacts/__main__.py