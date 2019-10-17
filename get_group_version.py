# Copyright 2019. Gambit Communications, Inc. All Rights Reserved.
# Copyright 2013. Amazon Web Services, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Import the SDK
import boto3
import uuid

import os 
import getopt
import sys

# use https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/greengrass.html#Greengrass.Client.get_group_version

###########################################################################
class MyApp:
	def __init__(self):
		self.access = None
		self.secret = None
		self.group = None
		self.version = None
		self.verbose = False

	def usage(self):
		print ('Usage: get_group_version.py')
		print ('\t-a|--access access-key  AWS_ACCESS_KEY_ID')
		print ('\t-s|--secret secret-key  AWS_SECRET_ACCESS_KEY')
		print ('\t-g|--group  group-id    group id')
		print ('\t-V|--version version-id version id')
		print ('\t[-v|--verbose]          verbose output')
		return

	def command_line(self):
		try:
			opts, args = getopt.getopt(sys.argv[1:], 'a:s:g:V:v', ['access=', 'secret=', 'group=', 'version=', 'verbose'])
		except getopt.GetoptError as err:
			# print help information and exit:
			print (str(err)) # will print something like "option -a not recognized"
			self.usage()
			sys.exit(1)

		for o, a in opts:
			if o in ('-v', '--verbose'):
			    self.verbose = True
			elif o in ('-a', '--access'):
				self.access = a
			elif o in ('-s', '--secret'):
				self.secret = a
			elif o in ('-g', '--group'):
				self.group = a
			elif o in ('-V', '--version'):
				self.version = a
			else:
			    assert False, 'unhandled option'

		if self.access == None:
			self.usage()
			sys.exit(1)

		if self.secret == None:
			self.usage()
			sys.exit(1)

		if self.group == None:
			self.usage()
			sys.exit(1)

		if self.version == None:
			self.usage()
			sys.exit(1)

	def start(self):
		self.command_line()

		client = boto3.client(
		    'greengrass',
		    aws_access_key_id = self.access,
		    aws_secret_access_key = self.secret
		    )

		response = client.get_group_version(
			GroupId = self.group,
			GroupVersionId = self.version
		)

		print response

###########################################################################
if __name__ == '__main__':
	main = MyApp()
	main.start()
