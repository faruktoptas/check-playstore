import urllib2,sys

if (len(sys.argv) == 1):
	print "Please specify a list of package names. \nUsage: \npython checkplaystore.py package_list.txt"
	sys.exit()

pklist_file = sys.argv[1]
try:
	packages = open(pklist_file).readlines()
except:
	print "I/O Error. "
	sys.exit()
apps = []
for i in range(0,len(packages)):
	try:
		print "Checking " + packages[i].replace("\n","") + "... " + str(i+1) + "/" + str(len(packages))
		response = urllib2.urlopen('https://play.google.com/store/apps/details?id=' + packages[i])
		html = response.read()
		apps.append(packages[i])
	except urllib2.HTTPError:
		pklist_file = pklist_file

if (len(apps) > 0):
	print "\n" + str(len(apps)) + " of " + str(len(packages)) + " apps are found in Google Play Store"
	for i in range(0,len(apps)):
		print apps[i].replace("\n","")
else:
	print "No app found"

	