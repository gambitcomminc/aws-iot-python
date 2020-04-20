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

import json

import os 
import getopt
import sys

# use https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iot-data.html#get_thing_shadow
# requires AWSIoTDataAccess policy for the user, else get permission exception
#
# also https://forums.aws.amazon.com/thread.jspa?threadID=221549

###########################################################################
class MyApp:
	def __init__(self):
		self.region = None
		self.access = None
		self.secret = None
		self.thing = None
		self.verbose = False

	def usage(self):
		print ("Usage: listthings.py")
		print ("\t-r|--region region-name AWS_REGION")
		print ("\t-a|--access access-key  AWS_ACCESS_KEY_ID")
		print ("\t-s|--secret secret-key  AWS_SECRET_ACCESS_KEY")
		print ("\t-t|--thing thing        thing name")
		print ("\t[-v|--verbose]          verbose output")
		return

	def command_line(self):
		try:
			opts, args = getopt.getopt(sys.argv[1:], "h:p:r:a:s:t:v", ["host=", "port=", "region=", "access=", "secret=", "thing=", "verbose"])
		except getopt.GetoptError as err:
			# print help information and exit:
			print (str(err)) # will print something like "option -a not recognized"
			self.usage()
			sys.exit(1)

		for o, a in opts:
			if o in ("-v", "--verbose"):
			    self.verbose = True
			elif o in ("-r", "--region"):
				self.region = a
			elif o in ("-a", "--access"):
				self.access = a
			elif o in ("-s", "--secret"):
				self.secret = a
			elif o in ("-t", "--thing"):
				self.thing = a
			elif o in ("-h", "--host"):
				dummy = a
			elif o in ("-p", "--port"):
				dummy = a
			else:
			    assert False, "unhandled option"

		if self.region == None:
			self.usage()
			sys.exit(1)

		if self.access == None:
			self.usage()
			sys.exit(1)

		if self.secret == None:
			self.usage()
			sys.exit(1)

		if self.thing == None:
			self.usage()
			sys.exit(1)

	def start(self):
		self.command_line()

		client = boto3.client(
		    'iot-data',
		    region_name = self.region,
		    aws_access_key_id = self.access,
		    aws_secret_access_key = self.secret
		    )

		response = client.get_thing_shadow(
		    thingName = self.thing
		)

		streamingBody = response["payload"]
		rawDataBytes = streamingBody.read()  # rawDataBytes is of type 'bytes' in, Python 3.x specific
		rawDataString = rawDataBytes.decode('utf-8')  # Python 3.x specific
		jsonState = json.loads(rawDataString)
		print jsonState

###########################################################################
if __name__ == "__main__":
	main = MyApp()
	main.start()
