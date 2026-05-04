#!/bin/bash

mkdir -p logs

pytest > logs/output.log 2>&1 || true

echo "Logs saved in logs/output.log"
