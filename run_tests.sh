#!/bin/bash

# Activate the virtual environment named 'env'
source ./env/bin/activate

# Get the current timestamp
timestamp=$(date +%Y_%m_%d_%H_%M_%_S)

# Create a directory for this test run's report
report_directory="allure_reports/run_${timestamp}"
mkdir -p "$report_directory"

# Run the behave command to execute the tests using both the 'pretty' and 'AllureFormatter' formatters
behave -f allure_behave.formatter:AllureFormatter -o "$report_directory" -f pretty