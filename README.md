Issue Summary

On May 10th, 2023, between 2:00 PM and 5:00 PM EAT, users of our web application experienced intermittent errors and slow response times. Approximately 600 users were affected. The root cause of the issue was a misconfiguration in our load balancer.

Timeline

2:00 PM EAT: The issue was detected by our monitoring system, which alerted the on-call engineer.
2:10 PM EAT: The engineer assumed that the issue was caused by high traffic and began to investigate the web server nodes and the load balancer configuration
2:30 PM EAT: After thorough investigation the engineer discovered that the issue was with the load balancer configuration.
3:00 PM EAT: The incident was escalated to the DevOps team for further investigation and resolution.
3:30 PM EAT: The DevOps team reviewed the load balancer configuration and identified the misconfiguration.
4:00 PM EAT: The DevOps team fixed the misconfiguration and restarted the load balancer.
5:00 PM EAT: The issue was resolved, and users reported normal performance.

Root Cause and Resolution

The root cause of the issue was a misconfiguration in the load balancer. Specifically, the load balancer was routing traffic to an incorrect backend server. The DevOps team fixed the misconfiguration by updating the load balancer configuration to route traffic to the correct backend server.

Corrective and Preventative Measures

To prevent similar issues in the future, the following corrective and preventative measures will be taken:

Implement automated tests to verify load balancer configuration.
Increase monitoring and alerting on load balancer performance and configuration changes.
Implement a backup load balancer to reduce the risk of downtime due to load balancer issues.
Schedule regular load balancer configuration reviews and updates.


Overall, we apologise for the inconvenience caused to our users. We are committed to improving our processes and systems to prevent similar issues in the future
