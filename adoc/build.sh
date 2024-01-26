#!/bin/zsh
#asciidoctor -D ../build **/*.adoc
cp  ../latex/main.pdf ../build
#linkcheck -e --no-show-redirects http://localhost:8080/TiPs_6/index.html