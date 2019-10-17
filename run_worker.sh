#!/bin/bash

celery -c 1 -l DEBUG -A example.tasks worker