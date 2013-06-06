from django.conf import settings
from django.conf.urls import patterns, include, url
from tastypie.api import Api
from app.api import CompanyResource , StockResource

v1_api = Api(api_name='v1')
v1_api.register(CompanyResource())
v1_api.register(StockResource())

v2_api = Api(api_name='v2')
v2_api.register(Company2Resource())
v1_api.register(StockResource())

urlpatterns = patterns('',
    url(r'^$', 'app.views.home'),
    url(r'^api/', include(v1_api.urls)),
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
