from django.shortcuts import render
from . import youtubeapi


def get_videos(channel_id):
    obj = youtubeapi.Youtube_API()

    # channel_id = 'UCGEoRAK92fUk2kY3kSJMR_Q'
    videos, res = obj.get_channel_videos(channel_id)

    details = obj.filter_details(res)

    content = []

    for i in range(len(videos)):
        data = videos[i]
        video_id = 'https://www.youtube.com/watch?v=' + str(data['snippet']['resourceId']['videoId'])
        pub_date = str(data['snippet']['publishedAt'])[:10]
        thumbnail = data['snippet']['thumbnails']['high']['url']
        title = data['snippet']['title']

        dic = {
            'title': title,
            'video_id': video_id,
            'pub_date': pub_date,
            'thumbnail': thumbnail,
        }

        content.append(dic)

    return content, details


def videos_page(request):
    channel_id = "UCGEoRAK92fUk2kY3kSJMR_Q"
    content, details = get_videos(channel_id)
    if content:
        data = {"content": content,
                "details": details
                }
    return render(request, 'videos/videos_page.html', {"data": data})
