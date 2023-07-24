from pytube import YouTube
vidDict={'vids':['https://youtu.be/dQw4w9WgXcQ']}
vidList=vidDict.get('vids')
for i in range(len(vidList)):
    yt=YouTube(vidList[i])
    yt.streams.filter(progressive=True).get_highest_resolution().download()