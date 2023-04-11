#!/bin/bash

# Get the latest report directory
latest_report_directory=$(ls -td allure_reports/*/ | head -n 1)

# Serve the latest Allure report
allure serve "$latest_report_directory"