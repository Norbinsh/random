"""
author: shay elmualem
POC / Experimential - not meant for production use.
Most simplest samples from https://boto3.readthedocs.io/en/latest/reference/services/s3.html#S3.Client.create_bucket
"""

import boto3
import sys
import itertools
from time import sleep


class AWSExp():
    """ Basic class to experiment with AWS resources, EC2, S3, RDS, and so on.
    You need to have the AWS SDK client configured """
    def __init__(self, resource_name):
        self.resource_name = resource_name
        self.valid_resources = ['ec2', 's3', 'rds']
        self.validate_resource()
        self.required_args = {
            'ec2': {
                        'create': [{'ImageId': None}, {'MinCount': None}, {'MaxCount': None}, {'InstanceType': None}],
                        'list': [],
                        'terminate': [],
                        'commands': {
                            'create': 'create_instances',
                            'list': '',
                            'terminate': 'terminate',
                            'type': 'Instance'
                                    }
                          },
            's3': {
                         'create': [
                             {'Bucket': None},
                             {'CreateBucketConfiguration': None}
                         ],
                         'list': [],
                         'terminate': [],
                        'commands': {
                            'create': 'create_bucket',
                            'list': '',
                            'terminate': 'delete',
                            'type': 'Bucket'
                        }
                                },
            'rds':
                {'create': [],
                 'list': [],
                 'terminate': [],
                 'commands': {
                            'create': '',
                          'list': '',
                            'terminate': '',
                     'type': ''
                 }
                }

        }

        self.required_create = {
            'ec2': None,
            's3': None,
            'rds': None
        }

        self.required_ec2_create = None
        self.required_s3_create = None
        self.required_rds_create = None
        self.client = boto3.resource(self.resource_name)

    def validate_resource(self):
        """ Validate that the passed resource is supported. """
        if self.resource_name not in self.valid_resources:
            raise ValueError("Resource needs to be either one of these: {valid_resources}".format
                             (valid_resources=self.valid_resources))

    def required_arguments(self, **kwargs):
        """ Raise value error when called with the given """
        raise ValueError("The following keyword arguments (key='value') are required: {required_kwargs}".format
                    (required_kwargs=[x for x in kwargs.keys()]).replace('[', '').replace(']', '').replace("'", '')
                         .replace('=None', ''))

    @staticmethod
    def return_kwarg(kwargs_list):
        """ In fact, no longer needed, we can use ** for unpacking """
        for kwarg in kwargs_list:
            yield '{}=None'.format(kwarg)

    @staticmethod
    def recursive_sleep(seconds):
        print("entered recursive sleep")
        if _response:
            return True
        recursive_sleep(seconds)

    def create_resource(self, **kwargs):
        """ Create the resource needed, based on the resource given while instantiating the
        class.
        Could easily get refactored, made it a bit too complex for no good reason.
        """

        """Super generic on purpose, we declare variable names on the fly - yes - using a dict would probably be
        better, but again - experimenting."""

        """
        Ignore (Bad approach):
        # _local_scope_required_args = exec('self.required_{}_args'.format(self.resource_name))
        # _local_scope_required_create = exec('self.required_{}_create'.format(self.resource_name))
        """

        # Build a list of keys from the main 'required *resource* args' dict
        self.required_create[self.resource_name] = list(
          itertools.chain(*[list(mini_dict.keys()) for mini_dict in self.required_args[self.resource_name]['create']]))
        # Compare if every required argument was passed when calling the function
        if [True if len([x for x in self.required_create[self.resource_name] if
                         x in (list(i for i in kwargs.keys()))]) == len(
                        self.required_args[self.resource_name]['create']) else False][0]:
            # We use exec for this to be as generic, not a must and could be considered a bad practice
            _response = None
            exec('_response = self.client.'+self.required_args[self.resource_name]["commands"]["create"]+'(**kwargs)')
            print(_response, "(Sometimes no response is returned via 'exec', need to fix / find alternative method)")
        else:
            # I over complicated things, didn't know we could just pass **dict as kwargs to a function
            # Also - dict comprehension!
            self.required_arguments(**{i:None for i in self.return_kwarg(self.required_create[self.resource_name])})

    def terminate_resource(self, *args):
        """ Terminate the instance resource on AWS """
        if args:
            for arg in args:
                _response = None
                exec('_response = self.client.' + self.required_args[self.resource_name]["commands"]["type"]+'(arg).'+self.required_args[self.resource_name]["commands"]["terminate"]+"()")
                print(_response, "(Sometimes no response is returned via 'exec', need to fix / find alternative method)")
        else:
            print("Nothing to do in this POC")
