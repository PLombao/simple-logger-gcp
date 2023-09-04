# simple-logger-gcp
A simple logger for a dockerize python application with GCP upload.

This code creades a localfile log in folder /logs with a logfile system by hour with the patter name of the file like "logfile.YYYY-MM-DD_HH" as specified on config/logging.json (handlers>file).

The logs will be registered on a format "datetime | loggername (module) | LEVEL | Message as specified on config/loggging.json (formatters).
