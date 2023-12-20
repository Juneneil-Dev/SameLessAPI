import requests
import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView,Response
from .models import Item, Register, sport_news, lab_analysis, free_analysis, verification_center, site_db, confirmed
from .models import report_scam, malicious_report, report_scammer, new_post, popularity, notification, advertise
from .models import banner, scam_site, fraud_report
from .serializers import ItemSerializer, RegisterSerializer, LoginSerializer, SportNewsAPISerializer, LabAnalysisAPISerializer
from .serializers import FreeAnalysisAPISerializer, VerificationCenterAPISerializer, SiteDbAPISerializer, Confirmed_APISerializer
from .serializers import ReportScamAPISerializer, MaliciousReportAPISerializer, ReportScammerAPISerializer, NewPostAPISerializer
from .serializers import PopularityAPISerializer, NotificationAPISerializer, AdvertiseAPISerializer
from .serializers import ScamSiteAPISerializer , BannerAPISerializer, FraudReportSerializer




from django.db import connection
from django.core.cache import cache
import requests
import os


class UserView(APIView):
    def get(self, request):
        sport_news_data = sport_news.objects.all()
        lab_analysis_data = lab_analysis.objects.all()
        free_analysis_data = free_analysis.objects.all()
        verification_center_data = verification_center.objects.all()
        site_db_data = site_db.objects.all()
        confirmed_data = confirmed.objects.all()
        report_scam_data = report_scam.objects.all()
        malicious_report_data = malicious_report.objects.all()
        report_scammer_data = report_scammer.objects.all()
        new_post_data = new_post.objects.all()
        popularity_data = popularity.objects.all()
        notification_data = notification.objects.all()
        advertise_data = advertise.objects.all()
        banner_data = banner.objects.all()
        scam_site_data = scam_site.objects.all()
        fraud_report_data = fraud_report.objects.all()

        
        sport_news_serializer = SportNewsAPISerializer(sport_news_data, many=True)
        lab_analysis_serializer = LabAnalysisAPISerializer(lab_analysis_data, many=True)
        free_analysis_serializer = FreeAnalysisAPISerializer(free_analysis_data, many=True)
        verification_center_serializer = VerificationCenterAPISerializer(verification_center_data, many=True)
        site_db_serializer = SiteDbAPISerializer(site_db_data, many=True)
        confirmed_serializer = Confirmed_APISerializer(confirmed_data, many=True)
        report_scam_serializer = ReportScamAPISerializer(report_scam_data, many=True)
        malicious_report_serializer = MaliciousReportAPISerializer(malicious_report_data, many=True)
        report_scammer_serializer = ReportScammerAPISerializer(report_scammer_data, many=True)
        new_post_serializer = NewPostAPISerializer(new_post_data, many=True)
        popularity_serializer = PopularityAPISerializer(popularity_data, many=True)
        notification_serializer = NotificationAPISerializer(notification_data, many=True)
        advertise_serializer = AdvertiseAPISerializer(advertise_data, many=True)
        banner_serializer = BannerAPISerializer(banner_data, many=True)
        scam_site_serializer = ScamSiteAPISerializer(scam_site_data, many=True)
        fraud_report_serializer = FraudReportSerializer(fraud_report_data, many=True)

        response_data = {
            "sport_news": sport_news_serializer.data,
            "lab_analysis": lab_analysis_serializer.data,
            "free_analysis": free_analysis_serializer.data,
            "verification_center": verification_center_serializer.data,
            "site_db": site_db_serializer.data,
            "confirmed": confirmed_serializer.data,
            "report_scam": report_scam_serializer.data,
            "malicious_report": malicious_report_serializer.data,
            "report_scammer": report_scammer_serializer.data,
            "new_post": new_post_serializer.data,
            "popularity": popularity_serializer.data,
            "notification": notification_serializer.data,
            "advertise": advertise_serializer.data,
            "banner": banner_serializer.data,
            "scam_site": scam_site_serializer.data,
            "fraud_report": fraud_report_serializer.data,
        }

        return Response(response_data)

# from rest_framework import authentication, permissions
# from django.contrib.auth.models import User

# class ListUsers(APIView):
#     """
#     View to list all users in the system.

#     * Requires token authentication.
#     * Only admin users are able to access this view.
#     """
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAdminUser]

#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         usernames = [user.username for user in User.objects.all()]
#         return Response(usernames)

class DumpItAPI(APIView):
    
    # def get(self,request):
    #     items = [
    #         "apple",
    #         "mango",
    #         "grapes"
    #     ]
    #     response_data = {"datas":items}
    #     return Response(response_data,status=status.HTTP_200_OK)

    # def post(self,request):
    #     response_data = {"response":"Hello Its Post method"}
    #     return Response(response_data,status=status.HTTP_200_OK)

    # def post(self,request):
    #     name = request.data.get('name')
    #     response_data = {"name": name}
    #     return Response(response_data,status=status.HTTP_200_OK)

    def get(self,request):
        items = Item.objects.all()
        items_data = ItemSerializer(items,many=True).data
        response_data = {"datas": items_data}
        return Response(response_data,status=status.HTTP_200_OK)

    def post(self,request):
        name = request.data.get('name')
        Item.objects.create(name=name)
        response_data = {"response":"item Created"}
        return Response(response_data,status=status.HTTP_200_OK)

    def put(self,request,id):
        name = request.data.get('name')
        item = Item.objects.filter(id=id).first()
        if item is None:
            response_data = {"response":"Item does not exists"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        item.name = name
        item.save()
        response_data = {"response":"item Updated"}
        return Response(response_data,status=status.HTTP_200_OK)

    # def delete(self,request):
    #     id = request.data.get('id')
    #     item = Item.objects.filter(id=id).first()
    #     if item is None:
    #         response_data = {"response": "Item does not exists"}
    #         return Response(response_data,status=status.HTTP_404_NOT_FOUND)

    #     item.delete()
    #     response_data = {"response": "item Delete"}
    #     return Response(response_data,status=status.HTTP_200_OK)

    def delete(self, request, id):
        item = Item.objects.filter(id=id).first()
        
        if item is None:
            response_data = {"response": "Item does not exist"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        response_data = {"response": "Item deleted"}
        return Response(response_data, status=status.HTTP_200_OK)


    # def registration(self, request):
    #     username = request.data.get('username')
    #     password = request.data.get('password')
        
    #     response = Register.register_user(username, password)
    #     return response

    # def reg_post(self, request):
        
    #     data = request.data

        
    #     serializer = RegisterSerializer(data=data)
    #     if serializer.is_valid():
            
    #         Register.objects.create(
    #             username=serializer.validated_data['username'],
    #             password=serializer.validated_data['password']
    #         )
            
    #         response_data = {"response": "User registered successfully"}
    #         return Response(response_data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def login_post(self, request):
        
    #     data = request.data

        
    #     serializer = LoginSerializer(data=data)
    #     if serializer.is_valid():
            
    #         username = serializer.validated_data['username']
    #         password = serializer.validated_data['password']

            
    #         try:
    #             user = Register.objects.get(username=username, password=password)
    #         except Register.DoesNotExist:
    #             response_data = {"response": "Invalid credentials"}
    #             return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)

    #         response_data = {"response": "Login successful", "user_id": user.id}
    #         return Response(response_data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPI(APIView):
    def post(self, request):
        # Get data from the request
        data = request.data

        # Validate the data using the serializer
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            # Authenticate user
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            # Check if the user exists
            try:
                user = Register.objects.get(username=username, password=password)
            except Register.DoesNotExist:
                response_data = {"response": "Invalid credentials"}
                return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)

            response_data = {"response": "Login successful", "user_id": user.id}
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterAPI(APIView):
    def get(self,request):
        items = Register.objects.all()
        items_data = RegisterSerializer(items,many=True).data
        response_data = {"datas": items_data}
        return Response(response_data,status=status.HTTP_200_OK)


    def post(self, request):
        # Get data from the request
        data = request.data

        # Validate the data using the serializer
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            # Check if the user already exists
            username = serializer.validated_data['username']
            if Register.objects.filter(username=username).exists():
                # User already exists, return an error response
                response_data = {"error": "User with this username already exists"}
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

            # Create a new user
            Register.objects.create(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password'],
                verify_password=serializer.validated_data['verify_password'],
                name=serializer.validated_data['name'],
                nickname=serializer.validated_data['nickname'],
                email=serializer.validated_data['email']
            )
            
            response_data = {"response": "User registered successfully"}
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,id):
        username = request.data.get('username')
        password = request.data.get('password')
        
        item = Register.objects.filter(id=id).first()
        if item is None:
            response_data = {"response":"Item does not exists"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        item.username = username
        item.password = password
        item.save()
        response_data = {"response":"item Updated"}
        return Response(response_data,status=status.HTTP_200_OK)

    def delete(self, request, id):
        item = Register.objects.filter(id=id).first()
        
        if item is None:
            response_data = {"response": "Item does not exist"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        response_data = {"response": "Item deleted"}
        return Response(response_data, status=status.HTTP_200_OK)        


class SportNewsAPI(APIView):

    def get(self,request):
        items = sport_news.objects.all()
        items_data = SportNewsAPISerializer(items,many=True).data
        response_data = {"datas": items_data}
        return Response(response_data,status=status.HTTP_200_OK)

    def post(self,request):
        picture = request.data.get('picture')
        title = request.data.get('title')
        old_new = request.data.get('old_new')
        description = request.data.get('description')
        


        sport_news.objects.create(picture=picture,title=title,old_new=old_new,description=description)
        response_data = {"response":"item Created"}
        return Response(response_data,status=status.HTTP_200_OK)

    def put(self,request,id):
        picture = request.data.get('picture')
        title = request.data.get('title')
        old_new = request.data.get('old_new')
        description = request.data.get('description')
        
        item = sport_news.objects.filter(id=id).first()
        if item is None:
            response_data = {"response":"Item does not exists"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        item.picture = picture
        item.title = title
        item.old_new = old_new
        item.description = description
        item.save()
        response_data = {"response":"item Updated"}
        return Response(response_data,status=status.HTTP_200_OK)

    def delete(self, request, id):
        item = sport_news.objects.filter(id=id).first()
        
        if item is None:
            response_data = {"response": "Item does not exist"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        response_data = {"response": "Item deleted"}
        return Response(response_data, status=status.HTTP_200_OK)

class LabAnalysisAPI(APIView):
    def get(self,request):
        items = lab_analysis.objects.all()
        items_data = LabAnalysisAPISerializer(items,many=True).data
        response_data = {"datas": items_data}
        return Response(response_data,status=status.HTTP_200_OK)

    def post(self,request):
        picture = request.data.get('picture')
        title = request.data.get('title')
        old_new = request.data.get('old_new')
        description = request.data.get('description')
        


        lab_analysis.objects.create(picture=picture,title=title,old_new=old_new,description=description)
        response_data = {"response":"item Created"}
        return Response(response_data,status=status.HTTP_200_OK)

    def put(self,request,id):
        picture = request.data.get('picture')
        title = request.data.get('title')
        old_new = request.data.get('old_new')
        description = request.data.get('description')
        
        item = lab_analysis.objects.filter(id=id).first()
        if item is None:
            response_data = {"response":"Item does not exists"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        item.picture = picture
        item.title = title
        item.old_new = old_new
        item.description = description
        item.save()
        response_data = {"response":"item Updated"}
        return Response(response_data,status=status.HTTP_200_OK)

    def delete(self, request, id):
        item = lab_analysis.objects.filter(id=id).first()
        
        if item is None:
            response_data = {"response": "Item does not exist"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        response_data = {"response": "Item deleted"}
        return Response(response_data, status=status.HTTP_200_OK)

class FreeAnalysisAPI(APIView):
    def get(self,request):
        items = free_analysis.objects.all()
        items_data = FreeAnalysisAPISerializer(items,many=True).data
        response_data = {"datas": items_data}
        return Response(response_data,status=status.HTTP_200_OK)

    def post(self,request):
        picture = request.data.get('picture')
        title = request.data.get('title')
        old_new = request.data.get('old_new')
        description = request.data.get('description')
        


        free_analysis.objects.create(picture=picture,title=title,old_new=old_new,description=description)
        response_data = {"response":"item Created"}
        return Response(response_data,status=status.HTTP_200_OK)

    def put(self,request,id):
        picture = request.data.get('picture')
        title = request.data.get('title')
        old_new = request.data.get('old_new')
        description = request.data.get('description')
        
        item = free_analysis.objects.filter(id=id).first()
        if item is None:
            response_data = {"response":"Item does not exists"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        item.picture = picture
        item.title = title
        item.old_new = old_new
        item.description = description
        item.save()
        response_data = {"response":"item Updated"}
        return Response(response_data,status=status.HTTP_200_OK)

    def delete(self, request, id):
        item = free_analysis.objects.filter(id=id).first()
        
        if item is None:
            response_data = {"response": "Item does not exist"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        response_data = {"response": "Item deleted"}
        return Response(response_data, status=status.HTTP_200_OK)

class VerificationCenterAPI(APIView):
    def get(self,request):
        items = verification_center.objects.all()
        items_data = VerificationCenterAPISerializer(items,many=True).data
        response_data = {"datas": items_data}
        return Response(response_data,status=status.HTTP_200_OK)

    def post(self,request):
        picture = request.data.get('picture')
        title = request.data.get('title')
        description = request.data.get('description')
        


        verification_center.objects.create(picture=picture,title=title,description=description)
        response_data = {"response":"item Created"}
        return Response(response_data,status=status.HTTP_200_OK)

    def put(self,request,id):
        picture = request.data.get('picture')
        title = request.data.get('title')
        description = request.data.get('description')
        
        item = verification_center.objects.filter(id=id).first()
        if item is None:
            response_data = {"response":"Item does not exists"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        item.picture = picture
        item.title = title
        item.description = description
        item.save()
        response_data = {"response":"item Updated"}
        return Response(response_data,status=status.HTTP_200_OK)

    def delete(self, request, id):
        item = verification_center.objects.filter(id=id).first()
        
        if item is None:
            response_data = {"response": "Item does not exist"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        response_data = {"response": "Item deleted"}
        return Response(response_data, status=status.HTTP_200_OK)

class SiteDbAPI(APIView):
    def get(self,request):
        items = site_db.objects.all()
        items_data = SiteDbAPISerializer(items,many=True).data
        response_data = {"datas": items_data}
        return Response(response_data,status=status.HTTP_200_OK)

    def post(self,request):
        picture = request.data.get('picture')
        title = request.data.get('title')
        description = request.data.get('description')
        


        site_db.objects.create(picture=picture,title=title,description=description)
        response_data = {"response":"item Created"}
        return Response(response_data,status=status.HTTP_200_OK)

    def put(self,request,id):
        picture = request.data.get('picture')
        title = request.data.get('title')
        description = request.data.get('description')
        
        item = site_db.objects.filter(id=id).first()
        if item is None:
            response_data = {"response":"Item does not exists"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        item.picture = picture
        item.title = title
        item.description = description
        item.save()
        response_data = {"response":"item Updated"}
        return Response(response_data,status=status.HTTP_200_OK)

    def delete(self, request, id):
        item = site_db.objects.filter(id=id).first()
        
        if item is None:
            response_data = {"response": "Item does not exist"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        response_data = {"response": "Item deleted"}
        return Response(response_data, status=status.HTTP_200_OK)

class Confirmed_API(APIView):
    def get(self,request):
        items = confirmed.objects.all()
        items_data = Confirmed_APISerializer(items,many=True).data
        response_data = {"datas": items_data}
        return Response(response_data,status=status.HTTP_200_OK)

    def post(self,request):
        picture = request.data.get('picture')
        title = request.data.get('title')
        old_new = request.data.get('old_new')
        description = request.data.get('description')
        


        confirmed.objects.create(picture=picture,title=title,old_new=old_new,description=description)
        response_data = {"response":"item Created"}
        return Response(response_data,status=status.HTTP_200_OK)

    def put(self,request,id):
        picture = request.data.get('picture')
        title = request.data.get('title')
        old_new = request.data.get('old_new')
        description = request.data.get('description')
        
        item = confirmed.objects.filter(id=id).first()
        if item is None:
            response_data = {"response":"Item does not exists"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        item.picture = picture
        item.title = title
        item.old_new = old_new
        item.description = description
        item.save()
        response_data = {"response":"item Updated"}
        return Response(response_data,status=status.HTTP_200_OK)

    def delete(self, request, id):
        item = confirmed.objects.filter(id=id).first()
        
        if item is None:
            response_data = {"response": "Item does not exist"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        response_data = {"response": "Item deleted"}
        return Response(response_data, status=status.HTTP_200_OK)

class ReportScamAPI(APIView):
    def get(self,request):
        items = report_scam.objects.all()
        items_data = ReportScamAPISerializer(items,many=True).data
        response_data = {"datas": items_data}
        return Response(response_data,status=status.HTTP_200_OK)

    def post(self,request):
        picture = request.data.get('picture')
        title = request.data.get('title')
        old_new = request.data.get('old_new')
        description = request.data.get('description')
        


        report_scam.objects.create(picture=picture,title=title,old_new=old_new,description=description)
        response_data = {"response":"item Created"}
        return Response(response_data,status=status.HTTP_200_OK)

    def put(self,request,id):
        picture = request.data.get('picture')
        title = request.data.get('title')
        old_new = request.data.get('old_new')
        description = request.data.get('description')
        
        item = report_scam.objects.filter(id=id).first()
        if item is None:
            response_data = {"response":"Item does not exists"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        item.picture = picture
        item.title = title
        item.old_new = old_new
        item.description = description
        item.save()
        response_data = {"response":"item Updated"}
        return Response(response_data,status=status.HTTP_200_OK)

    def delete(self, request, id):
        item = report_scam.objects.filter(id=id).first()
        
        if item is None:
            response_data = {"response": "Item does not exist"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        response_data = {"response": "Item deleted"}
        return Response(response_data, status=status.HTTP_200_OK)

class MaliciousReportAPI(APIView):
    def get(self,request):
        items = malicious_report.objects.all()
        items_data = MaliciousReportAPISerializer(items,many=True).data
        response_data = {"datas": items_data}
        return Response(response_data,status=status.HTTP_200_OK)

    def post(self,request):
        picture = request.data.get('picture')
        title = request.data.get('title')
        old_new = request.data.get('old_new')
        description = request.data.get('description')
        


        malicious_report.objects.create(picture=picture,title=title,old_new=old_new,description=description)
        response_data = {"response":"item Created"}
        return Response(response_data,status=status.HTTP_200_OK)

    def put(self,request,id):
        picture = request.data.get('picture')
        title = request.data.get('title')
        old_new = request.data.get('old_new')
        description = request.data.get('description')
        
        item = malicious_report.objects.filter(id=id).first()
        if item is None:
            response_data = {"response":"Item does not exists"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        item.picture = picture
        item.title = title
        item.old_new = old_new
        item.description = description
        item.save()
        response_data = {"response":"item Updated"}
        return Response(response_data,status=status.HTTP_200_OK)

    def delete(self, request, id):
        item = malicious_report.objects.filter(id=id).first()
        
        if item is None:
            response_data = {"response": "Item does not exist"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        response_data = {"response": "Item deleted"}
        return Response(response_data, status=status.HTTP_200_OK)

class ReportScammerAPI(APIView):
    def get(self,request):
        items = report_scammer.objects.all()
        items_data = ReportScammerAPISerializer(items,many=True).data
        response_data = {"datas": items_data}
        return Response(response_data,status=status.HTTP_200_OK)

    def post(self,request):
        picture = request.data.get('picture')
        title = request.data.get('title')
        old_new = request.data.get('old_new')
        description = request.data.get('description')
        


        report_scammer.objects.create(picture=picture,title=title,old_new=old_new,description=description)
        response_data = {"response":"item Created"}
        return Response(response_data,status=status.HTTP_200_OK)

    def put(self,request,id):
        picture = request.data.get('picture')
        title = request.data.get('title')
        old_new = request.data.get('old_new')
        description = request.data.get('description')
        
        item = report_scammer.objects.filter(id=id).first()
        if item is None:
            response_data = {"response":"Item does not exists"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        item.picture = picture
        item.title = title
        item.old_new = old_new
        item.description = description
        item.save()
        response_data = {"response":"item Updated"}
        return Response(response_data,status=status.HTTP_200_OK)

    def delete(self, request, id):
        item = report_scammer.objects.filter(id=id).first()
        
        if item is None:
            response_data = {"response": "Item does not exist"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        response_data = {"response": "Item deleted"}
        return Response(response_data, status=status.HTTP_200_OK)

class NewPostAPI(APIView):
    def get(self,request):
        items = new_post.objects.all()
        items_data = NewPostAPISerializer(items,many=True).data
        response_data = {"datas": items_data}
        return Response(response_data,status=status.HTTP_200_OK)

    def post(self,request):
        picture = request.data.get('picture')
        old_new = request.data.get('old_new')
        date_and_time = request.data.get('date_and_time')
        description = request.data.get('description')
        


        new_post.objects.create(picture=picture,old_new=old_new,date_and_time=date_and_time,description=description)
        response_data = {"response":"item Created"}
        return Response(response_data,status=status.HTTP_200_OK)

    def put(self,request,id):
        picture = request.data.get('picture')
        old_new = request.data.get('old_new')
        date_and_time = request.data.get('date_and_time')
        description = request.data.get('description')
        
        item = new_post.objects.filter(id=id).first()
        if item is None:
            response_data = {"response":"Item does not exists"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        item.picture = picture
        item.old_new = old_new
        item.date_and_time = date_and_time
        item.description = description
        item.save()
        response_data = {"response":"item Updated"}
        return Response(response_data,status=status.HTTP_200_OK)

    def delete(self, request, id):
        item = new_post.objects.filter(id=id).first()
        
        if item is None:
            response_data = {"response": "Item does not exist"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        response_data = {"response": "Item deleted"}
        return Response(response_data, status=status.HTTP_200_OK)

class PopularityAPI(APIView):
    def get(self,request):
        items = popularity.objects.all()
        items_data = PopularityAPISerializer(items,many=True).data
        response_data = {"datas": items_data}
        return Response(response_data,status=status.HTTP_200_OK)

    def post(self,request):
        title = request.data.get('title')
        


        popularity.objects.create(title=title)
        response_data = {"response":"item Created"}
        return Response(response_data,status=status.HTTP_200_OK)

    def put(self,request,id):
        title = request.data.get('title')
        
        item = popularity.objects.filter(id=id).first()
        if item is None:
            response_data = {"response":"Item does not exists"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        item.title = title
        item.save()
        response_data = {"response":"item Updated"}
        return Response(response_data,status=status.HTTP_200_OK)

    def delete(self, request, id):
        item = popularity.objects.filter(id=id).first()
        
        if item is None:
            response_data = {"response": "Item does not exist"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        response_data = {"response": "Item deleted"}
        return Response(response_data, status=status.HTTP_200_OK)

class NotificationAPI(APIView):
    def get(self,request):
        items = notification.objects.all()
        items_data = NotificationAPISerializer(items,many=True).data
        response_data = {"datas": items_data}
        return Response(response_data,status=status.HTTP_200_OK)

    def post(self,request):
        message = request.data.get('message')
        time = request.data.get('time')
        


        notification.objects.create(message=message,time=time)
        response_data = {"response":"item Created"}
        return Response(response_data,status=status.HTTP_200_OK)

    def put(self,request,id):
        message = request.data.get('message')
        time = request.data.get('time')
        
        item = notification.objects.filter(id=id).first()
        if item is None:
            response_data = {"response":"Item does not exists"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        item.message = message
        item.time = time
        item.save()
        response_data = {"response":"item Updated"}
        return Response(response_data,status=status.HTTP_200_OK)

    def delete(self, request, id):
        item = notification.objects.filter(id=id).first()
        
        if item is None:
            response_data = {"response": "Item does not exist"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        response_data = {"response": "Item deleted"}
        return Response(response_data, status=status.HTTP_200_OK)

class AdvertiseAPI(APIView):
    def get(self,request):
        items = advertise.objects.all()
        items_data = AdvertiseAPISerializer(items,many=True).data
        response_data = {"datas": items_data}
        return Response(response_data,status=status.HTTP_200_OK)

    def post(self,request):
        picture = request.data.get('picture')

        


        advertise.objects.create(picture=picture)
        response_data = {"response":"item Created"}
        return Response(response_data,status=status.HTTP_200_OK)

    def put(self,request,id):
        picture = request.data.get('picture')
        
        item = advertise.objects.filter(id=id).first()
        if item is None:
            response_data = {"response":"Item does not exists"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        item.picture = picture
        item.save()
        response_data = {"response":"item Updated"}
        return Response(response_data,status=status.HTTP_200_OK)

    def delete(self, request, id):
        item = advertise.objects.filter(id=id).first()
        
        if item is None:
            response_data = {"response": "Item does not exist"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        response_data = {"response": "Item deleted"}
        return Response(response_data, status=status.HTTP_200_OK)

class BannerAPI(APIView):
    def get(self,request):
        items = banner.objects.all()
        items_data = BannerAPISerializer(items,many=True).data
        response_data = {"datas": items_data}
        return Response(response_data,status=status.HTTP_200_OK)

    def post(self,request):
        picture = request.data.get('picture')
        


        banner.objects.create(picture=picture)
        response_data = {"response":"item Created"}
        return Response(response_data,status=status.HTTP_200_OK)

    def put(self,request,id):
        picture = request.data.get('picture')
        
        item = banner.objects.filter(id=id).first()
        if item is None:
            response_data = {"response":"Item does not exists"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        item.picture = picture
        item.save()
        response_data = {"response":"item Updated"}
        return Response(response_data,status=status.HTTP_200_OK)

    def delete(self, request, id):
        item = banner.objects.filter(id=id).first()
        
        if item is None:
            response_data = {"response": "Item does not exist"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        response_data = {"response": "Item deleted"}
        return Response(response_data, status=status.HTTP_200_OK)

class ScamSiteAPI(APIView):
    def get(self,request):
        items = scam_site.objects.all()
        items_data = ScamSiteAPISerializer(items,many=True).data
        response_data = {"datas": items_data}
        return Response(response_data,status=status.HTTP_200_OK)

    def post(self,request):
        picture = request.data.get('picture')
        title = request.data.get('title')
        description = request.data.get('description')
        


        scam_site.objects.create(picture=picture,title=title,description=description)
        response_data = {"response":"item Created"}
        return Response(response_data,status=status.HTTP_200_OK)

    def put(self,request,id):
        picture = request.data.get('picture')
        title = request.data.get('title')
        description = request.data.get('description')
        
        item = scam_site.objects.filter(id=id).first()
        if item is None:
            response_data = {"response":"Item does not exists"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        item.picture = picture
        item.title = title
        item.description = description
        item.save()
        response_data = {"response":"item Updated"}
        return Response(response_data,status=status.HTTP_200_OK)

    def delete(self, request, id):
        item = scam_site.objects.filter(id=id).first()
        
        if item is None:
            response_data = {"response": "Item does not exist"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        response_data = {"response": "Item deleted"}
        return Response(response_data, status=status.HTTP_200_OK)

class FraudReportAPI(APIView):
    def get(self,request):
        items = fraud_report.objects.all()
        items_data = FraudReportSerializer(items,many=True).data
        response_data = {"datas": items_data}
        return Response(response_data,status=status.HTTP_200_OK)

    def post(self,request):
        number = request.data.get('number')
        title = request.data.get('title')
        date = request.data.get('date')
        box_check = request.data.get('box_check')
        


        fraud_report.objects.create(number=number,title=title,date=date,box_check=box_check)
        response_data = {"response":"item Created"}
        return Response(response_data,status=status.HTTP_200_OK)

    def put(self,request,id):
        number = request.data.get('number')
        title = request.data.get('title')
        date = request.data.get('date')
        box_check = request.data.get('box_check')
        
        item = fraud_report.objects.filter(id=id).first()
        if item is None:
            response_data = {"response":"Item does not exists"}
            return Response(response_data,status=status.HTTP_404_NOT_FOUND)
        item.number = number
        item.title = title
        item.date = date
        item.box_check = box_check
        item.save()
        response_data = {"response":"item Updated"}
        return Response(response_data,status=status.HTTP_200_OK)

    def delete(self, request, id):
        item = fraud_report.objects.filter(id=id).first()
        
        if item is None:
            response_data = {"response": "Item does not exist"}
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        response_data = {"response": "Item deleted"}
        return Response(response_data, status=status.HTTP_200_OK)

class HealthCheckView(APIView):
    def get(self, request):
        # Perform additional health checks
        database_status = self.check_database_connectivity()
        cache_status = self.check_cache_availability()
        external_service_status = self.check_external_service()

        if not all([database_status, cache_status, external_service_status]):
            response_data = {"status": "ok"}
            return Response(response_data, status=status.HTTP_200_OK)
        

    def check_database_connectivity(self):
        try:
            with connection.cursor():
                pass
            return True
        except Exception as e:
            return False

    def check_cache_availability(self):
        try:
            cache.set("health_check", "ok", timeout=5)
            return cache.get("health_check") == "ok"
        except Exception as e:
            return False

    def check_external_service(self):
        try:
            response = requests.get("https://api.example.com/health")
            return response.status_code == 200
        except requests.RequestException:
            return False



