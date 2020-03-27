#
# Practicing JSON
#
import urllib.request
import json

def printResults(data):
    theJSON = json.loads(data)
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

        count = theJSON["metadata"]["count"]
        print(str(count) + " events recorded")

        for i in theJSON["features"]:
            print(i["properties"]["place"])
        print("-------------------\n")

        for i in theJSON["features"]:
            if i["properties"]["mag"] >= 4.0:
                print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
        print("-------------------\n")
def main():
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    webUrl = urllib.request.urlopen(urlData)
    print("result code : " + str(webUrl.getcode()))
    if webUrl.getcode() == 200:
        data = webUrl.read()
        printResults(data)
    else:
        print("Received error, cannot parse results")

if __name__ == '__main__':
    main()