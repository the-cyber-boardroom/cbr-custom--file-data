#!/bin/bash

uvicorn cbr_custom_file_data.lambdas.handler:app --host 0.0.0.0 --port 8080