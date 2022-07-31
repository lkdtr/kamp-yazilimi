#!/usr/bin/env bash

MANAGEPY_COMMAND=(python mudur/manage.py)
if [ "${MUDUR_DEBUG,,}" = "true" ]
then
  WEB_COMMAND=(gunicorn --chdir mudur --bind 0.0.0.0:8080 --workers 2 --access-logfile - --reload mudur.wsgi)
else
  WEB_COMMAND=(gunicorn --chdir mudur --bind 0.0.0.0:8080 --workers 8 --access-logfile - mudur.wsgi)
fi

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
  print_command "${MANAGEPY_COMMAND[@]}" "${@:2}"
  exec "${MANAGEPY_COMMAND[@]}" "${@:2}"
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
