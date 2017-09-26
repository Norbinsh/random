# Base Ubuntu server image for development

FROM ubuntu:latest

RUN echo "Updating packages"
RUN apt update -y
RUN echo "Installing some goodies"
RUN apt install -y --force-yes python3 python3-pip vim openssh-server git

WORKDIR ~
CMD cat /dev/zero | ssh-keygen -q -N ""
CMD git config --global user.name "Shay Elmualem"
CMD git config --global user.email "wowshay@gmail.com"

EXPOSE 22






