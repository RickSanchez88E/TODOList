from django.http import HttpResponse
from google.cloud import storage


def play_song(request, song_name):
    bucket_name = 'audiofile_sanchez'

    # Connect to Google Cloud Storage
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    # Get the blob (数据库的大对象) from the bucket
    blob = bucket.blob(song_name)

    # Check if the file exists
    if not blob.exists():
        return HttpResponse("File not found", status=404)

    # Set the content type for the response
    response = HttpResponse(blob.download_as_string(), content_type='audio/mpeg')

    # Set the content disposition to 'inline' to render audio in browser
    response['Content-Disposition'] = 'inline; filename="{}"'.format(song_name)

    return response
