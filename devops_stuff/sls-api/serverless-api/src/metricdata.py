MetricDataQuery = [
        {
            'Id': 'albhealthyhosts',
            'MetricStat': {
                'Metric': {
                    'Namespace': 'AWS/ApplicationELB',
                    'MetricName': 'HealthyHostCount',
                    'Dimensions': [
                        {
                            'Name': 'LoadBalancer',
                            'Value': 'app/elb-name/elb-id'
                        },
                        {
                            'Name': 'TargetGroup',
                            'Value': 'targetgroup/tg-name/tg-id'
                        },
                    ]
                },
                'Period': 300,
                'Stat': 'Maximum',
                'Unit': 'Count'
            },
            'ReturnData': True
        },
    ]