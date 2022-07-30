#!/usr/bin/env bash

MANAGEPY_COMMAND=(python mudur/manage.py)
WEB_COMMAND=(gunicorn mudur.wsgi --bind 127.0.0.1:8080 --workers 8 --access-logfile -)

if [ -z "${TERM}" ]; then
  FMT_BOLD="$(tput bold)"
  FMT_NORMAL="$(tput sgr0)"
fi

print_command() {
  echo "Running: ${FMT_BOLD}${*}${FMT_NORMAL}"
}

case "${1}" in
"")
  echo "No command provided"
  exit 11
  ;;
managepy)
  print_command "${MANAGEPY_COMMAND[@]}"
  exec "${MANAGEPY_COMMAND[@]}"
  ;;
web)
  print_command "${WEB_COMMAND[@]}" "${@:2}"
  exec "${WEB_COMMAND[@]}" "${@:2}"
  ;;
*)
  print_command "${@}"
  exec "${@}"
  ;;
esac
