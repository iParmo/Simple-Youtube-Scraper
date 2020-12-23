from googleapiclient.discovery import build

KEY = 'your-api-key-here'
service = build('youtube', 'v3', developerKey=KEY)

ytChannel = input("Channel to scan: ")
request = service.channels().list(
    part='statistics',
    forUsername=ytChannel
)

response = request.execute()

f = open("data.txt", "a")
f.write(f'{ytChannel}´s statistics: {str(response)} \n\n')
f.close()
print(f'Youtube channel {ytChannel} has been scanned and logged to data.txt')
