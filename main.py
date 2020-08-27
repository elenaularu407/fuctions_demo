#Create function that is triggered by http request
def importFile(request):
	
	#import libraries
	from google.cloud import storage
	from urllib import request

	#set storage client
	client2 = storage.Client()

	# get bucket
	bucket = client2.get_bucket('elena_demo') #without gs://
	blob = bucket.blob('cb_2017_us_zcta510_500k.zip')

	#See if json exists
	if blob.exists() == False :

		#copy file to google storage
		try:
			ftpfile = request.urlopen('http://www2.census.gov/geo/tiger/GENZ2017/shp/cb_2017_us_zcta510_500k.zip')
		
			blob.upload_from_file(ftpfile)
			print('copied cb_2017_us_zcta510_500k.zip to google storage')

		shutil.unpack_archive('ftpfile', 'gs://elena_demo')

		#print error if file doesn't exists
		except:
		
			print('cb_2017_us_zcta510_500k.zip does not exist')

	#print error if file already exists	in google storage
	else:

		print('file already exists in google storage') 
