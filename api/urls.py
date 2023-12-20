from django.urls import path
from .views import DumpItAPI, RegisterAPI, SportNewsAPI, LabAnalysisAPI, FreeAnalysisAPI, VerificationCenterAPI
from .views import Confirmed_API, ReportScamAPI, MaliciousReportAPI, ReportScammerAPI, NewPostAPI, PopularityAPI
from .views import AdvertiseAPI, BannerAPI, ScamSiteAPI, SiteDbAPI, NotificationAPI, LoginAPI, HealthCheckView
from .views import UserView, FraudReportAPI




urlpatterns = [
    path('', DumpItAPI.as_view()),
    # path('create/',DumpItAPI.as_view()),
    # path('update/<int:id>/',DumpItAPI.as_view()),
    # path('delete/<int:id>/',DumpItAPI.as_view()),

    path('health_check/', HealthCheckView.as_view()),
    # path('api/users/', ListUsers.as_view()),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', UserView.as_view()),

    path('login/', LoginAPI.as_view(), name='login'),
    path('get_user_register/', RegisterAPI.as_view()),

    path('register/get/',RegisterAPI.as_view()),
    path('register/create',RegisterAPI.as_view()),
    path('register/put/<int:id>/',RegisterAPI.as_view()),
    path('register/delete/<int:id>/',RegisterAPI.as_view()),

    path('sport_news/get/', SportNewsAPI.as_view()),
    path('sport_news/create/', SportNewsAPI.as_view()),
    path('sport_news/put/<int:id>/', SportNewsAPI.as_view()),
    path('sport_news/delete/<int:id>/', SportNewsAPI.as_view()),


    path('lab_analysis/get/', LabAnalysisAPI.as_view()),
    path('lab_analysis/create/', LabAnalysisAPI.as_view()),
    path('lab_analysis/put/<int:id>/', LabAnalysisAPI.as_view()),
    path('lab_analysis/delete/<int:id>/', LabAnalysisAPI.as_view()),


    path('free_analysis/get/', FreeAnalysisAPI.as_view()),
    path('free_analysis/create/', FreeAnalysisAPI.as_view()),
    path('free_analysis/put/<int:id>/', FreeAnalysisAPI.as_view()),
    path('free_analysis/delete/<int:id>/', FreeAnalysisAPI.as_view()),


    path('verification_center/get/', VerificationCenterAPI.as_view()),
    path('verification_center/create/', VerificationCenterAPI.as_view()),
    path('verification_center/put/<int:id>/', VerificationCenterAPI.as_view()),
    path('verification_center/delete/<int:id>/', VerificationCenterAPI.as_view()),


    path('site_db/get/', SiteDbAPI.as_view()),
    path('site_db/create/', SiteDbAPI.as_view()),
    path('site_db/put/<int:id>/', SiteDbAPI.as_view()),
    path('site_db/delete/<int:id>/', SiteDbAPI.as_view()),


    path('confirmed/get/', Confirmed_API.as_view()),
    path('confirmed/create/', Confirmed_API.as_view()),
    path('confirmed/put/<int:id>/', Confirmed_API.as_view()),
    path('confirmed/delete/<int:id>/', Confirmed_API.as_view()),


    path('report_scam/get/', ReportScamAPI.as_view()),
    path('report_scam/create/', ReportScamAPI.as_view()),
    path('report_scam/put/<int:id>/', ReportScamAPI.as_view()),
    path('report_scam/delete/<int:id>/', ReportScamAPI.as_view()),


    path('malicious_report/get/', MaliciousReportAPI.as_view()),
    path('malicious_report/create/', MaliciousReportAPI.as_view()),
    path('malicious_report/put/<int:id>/', MaliciousReportAPI.as_view()),
    path('malicious_report/delete/<int:id>/', MaliciousReportAPI.as_view()),


    path('report_scammer/get/', ReportScammerAPI.as_view()),
    path('report_scammer/create/', ReportScammerAPI.as_view()),
    path('report_scammer/put/<int:id>/', ReportScammerAPI.as_view()),
    path('report_scammer/delete/<int:id>/', ReportScammerAPI.as_view()),


    path('new_post/get/', NewPostAPI.as_view()),
    path('new_post/create/', NewPostAPI.as_view()),
    path('new_post/put/<int:id>/', NewPostAPI.as_view()),
    path('new_post/delete/<int:id>/', NewPostAPI.as_view()),


    path('popularity/get/', PopularityAPI.as_view()),
    path('popularity/create/', PopularityAPI.as_view()),
    path('popularity/put/<int:id>/', PopularityAPI.as_view()),
    path('popularity/delete/<int:id>/', PopularityAPI.as_view()),


    path('notification/get/', NotificationAPI.as_view()),
    path('notification/create/', NotificationAPI.as_view()),
    path('notification/put/<int:id>/', NotificationAPI.as_view()),
    path('notification/delete/<int:id>/', NotificationAPI.as_view()),


    path('advertise/get/', AdvertiseAPI.as_view()),
    path('advertise/create/', AdvertiseAPI.as_view()),
    path('advertise/put/<int:id>/', AdvertiseAPI.as_view()),
    path('advertise/delete/<int:id>/', AdvertiseAPI.as_view()),

    
    path('banner/get/', BannerAPI.as_view()),
    path('banner/create/', BannerAPI.as_view()),
    path('banner/put/<int:id>/', BannerAPI.as_view()),
    path('banner/delete/<int:id>/', BannerAPI.as_view()),


    path('scam_site/get/', ScamSiteAPI.as_view()),
    path('scam_site/create/', ScamSiteAPI.as_view()),
    path('scam_site/put/<int:id>/', ScamSiteAPI.as_view()),
    path('scam_site/delete/<int:id>/', ScamSiteAPI.as_view()),


    path('fraud_report/get/', FraudReportAPI.as_view()),
    path('fraud_report/create/', FraudReportAPI.as_view()),
    path('fraud_report/put/<int:id>/', FraudReportAPI.as_view()),
    path('fraud_report/delete/<int:id>/', FraudReportAPI.as_view()),


]