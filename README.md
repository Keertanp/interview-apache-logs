The important information which should be displayed is:

- Total number of requests
- Total data transmitted over all requests
- Most requested resource
  - total number of requests for this resource
  - percentage of requests for this resource
- Remote host with the most requests
  - total number of requests from this remote host
  - percentage of requests for this resource
- Percentages of each class of HTTP status code (1xx, 2xx, 3xx, 4xx, 5xx)

## Example files

Within the `example` directory are some sample log files which were generated with the `apache_log_stats.py` script located in the `scripts` directory. Along with the sample log files are the output of statistics based on those log files. Refer to these outputs to ensure the statistics you are parsing are correct.

### Below are the steps to generate log file by script:

1. Clone this repo
   https://github.com/Keertanp/interview-apache-logs.git
   cd interview-apache-logs

2. Checkout branch `master`

3. In order to generate logs, run below command for each and every logs files and create new output files respectively:
e.g 

python apache_log_stats.py ../
examples/real_apache_logs.log -v --aggresive > ../examples/real_apache_logs_new.out

Generated output files are as below:
example1new.out
example2new.out
real_apache_logs_new.out



