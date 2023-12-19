from rest_framework import serializers
from .models import Item, Register, sport_news, lab_analysis, free_analysis, verification_center, site_db, confirmed
from .models import report_scam, malicious_report, report_scammer, new_post, popularity, notification, advertise
from .models import banner, scam_site #, fraud_report



class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['id', 'name']

class RegisterSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=30)
    verify_password = serializers.CharField(max_length=30)
    name = serializers.CharField(max_length=255)
    nickname = serializers.CharField(max_length=30)
    email = serializers.EmailField()

    def validate(self, data):
        """
        Custom validation to check if password matches verify_password.
        """
        password = data.get('password')
        verify_password = data.get('verify_password')

        if password != verify_password:
            raise serializers.ValidationError({"message": "The entered passwords do not match."})

        # Add additional password validation logic here if needed

        return data

    class Meta:
        model = Register
        fields = ['id', 'username', 'password', 'verify_password', 'name', 'nickname', 'email', 'created_at']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class SportNewsAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = sport_news
        fields = ['id', 'picture', 'title', 'old_new', 'description', 'created_at']


class LabAnalysisAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = lab_analysis
        fields = ['id', 'picture', 'title', 'old_new', 'description', 'created_at']


class FreeAnalysisAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = free_analysis
        fields = ['id', 'picture', 'title', 'old_new', 'description', 'created_at']


class VerificationCenterAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = verification_center
        fields = ['id', 'picture', 'title', 'description', 'created_at']


class SiteDbAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = site_db
        fields = ['id', 'picture', 'title', 'description', 'created_at']


class Confirmed_APISerializer(serializers.ModelSerializer):
    class Meta:
        model = confirmed
        fields = ['id', 'picture', 'title', 'old_new', 'description', 'created_at']


class ReportScamAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = report_scam
        fields = ['id', 'picture', 'title', 'old_new', 'description', 'created_at']


class MaliciousReportAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = malicious_report
        fields = ['id', 'picture', 'title', 'old_new', 'description', 'created_at']


class ReportScammerAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = report_scammer
        fields = ['id', 'picture', 'title', 'old_new', 'description', 'created_at']


class NewPostAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = new_post
        fields = ['id', 'picture', 'old_new', 'date_and_time', 'description', 'created_at']


class PopularityAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = popularity
        fields = ['id', 'title', 'created_at']


class NotificationAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = notification
        fields = ['id', 'message', 'time', 'created_at']


class AdvertiseAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = advertise
        fields = ['id', 'picture', 'created_at']


class BannerAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = banner
        fields = ['id', 'picture', 'created_at']


class ScamSiteAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = scam_site
        fields = ['id', 'picture', 'title', 'description', 'created_at']


# class FraudReportSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = fraud_report
#         fields = ['id', 'number', 'title', 'date', 'check','created_at']



# class RegistrationSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Register
#         fields = ['username', 'password']