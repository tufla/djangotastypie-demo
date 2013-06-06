from django.conf.urls import patterns, include, url
from tastypie.api import Api
from app.api import CompanyResource, StockResource

v1_api = Api(api_name='v1')
v1_api.register(CompanyResource())
v1_api.register(StockResource())

urlpatterns = patterns('',
    url(r'^api/', include(v1_api.urls)),
)
