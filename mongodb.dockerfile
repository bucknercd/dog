from mongo
LABEL maintainer="Chris Buckner<christopher.d.buckner@gmail.com>"

# This is to support noninteractive apt-get installs
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
	net-tools \
	vim \
	curl \
	telnet
