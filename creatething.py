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

# use https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot.html#IoT.Client.create_thing

###########################################################################
class MyApp:
	def __init__(self):
		self.access = None
		self.secret = None
		self.prefix = None
		self.count = 1
		self.verbose = False

	def usage(self):
		print ("Usage: creatething.py")
		print ("\t-a|--access access-key   AWS_ACCESS_KEY_ID")
		print ("\t-s|--secret secret-key   AWS_SECRET_ACCESS_KEY")
		print ("\t-p|--prefix thing-prefix thing name prefix")
		print ("\t[-c|--count count]       count of things to be created, default 1")
		print ("\t[-v|--verbose]    verbose output")
		return

	def command_line(self):
		try:
			opts, args = getopt.getopt(sys.argv[1:], "a:s:p:c:v", ["access=", "secret=", "prefix=", "count=", "verbose"])
		except getopt.GetoptError as err:
			# print help information and exit:
			print (str(err)) # will print something like "option -a not recognized"
			self.usage()
			sys.exit(1)

		for o, a in opts:
			if o in ("-v", "--verbose"):
			    self.verbose = True
			elif o in ("-a", "--access"):
				self.access = a
			elif o in ("-s", "--secret"):
				self.secret = a
			elif o in ("-p", "--prefix"):
				self.prefix = a
			elif o in ("-c", "--count"):
				self.count = int(a)
			else:
			    assert False, "unhandled option"

		if self.access == None:
			self.usage()
			sys.exit(1)

		if self.secret == None:
			self.usage()
			sys.exit(1)

		if self.prefix == None:
			self.usage()
			sys.exit(1)

		if self.count == None:
			self.count = 1

	def start(self):
		self.command_line()

		client = boto3.client(
		    'iot',
		    aws_access_key_id = self.access,
		    aws_secret_access_key = self.secret
		    )

		for i in range(1, self.count + 1):
			thingname = self.prefix + '-' + str(i)
			response = client.create_thing(
			    thingName = thingname
			)
			print response

###########################################################################
if __name__ == "__main__":
	main = MyApp()
	main.start()
