from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import News
from .serializers import NewsSerializer


class NewsViews(APIView):
    def get(self, request):
        all_news = News.objects.all()
        serialized_data = NewsSerializer(data=all_news, many=True)
        serialized_data.is_valid()
        return Response(data=serialized_data.data)

    def post(self, request):
        serialized_data = NewsSerializer(data=request.data)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(data=serialized_data.data)
        return Response({"error": serialized_data.errors})


    def delete(self, request):
        id = request.data['id']
        try:
            News.objects.get(id=id).delete()
            return Response({"status": "success"}, status = status.HTTP_204_NO_CONTENT)
        except:
            return Response({"status": "not found"}, status = status.HTTP_404_NOT_FOUND)


    def patch(self, request):
        news = News.objects.get(id=request.data['id'])
        serialized_data = NewsSerializer(news, data=request.data, partial=True)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(data=serialized_data.data)
        return Response({"error": serialized_data.errors})


class SingleNews(APIView):
    def get(self, request, id):

        news_data = News.objects.filter(id=id)
     

        return Response(data={
            "id": news_data.id,
            "name": news_data.name,
            "text": news_data.text,
            "created_at": news_data.created_at,
            "updated_at": news_data.updated_at,
        })


