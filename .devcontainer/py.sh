#! /usr/bin/env sh
cd /opt/project && poetry run python "$@" && cd - > /dev/null
