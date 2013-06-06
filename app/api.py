from app.models import Company, Stock
from tastypie import fields
from tastypie.authorization import Authorization
# from tastypie.exceptions import BadRequest
# from tastypie.paginator import Paginator
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS

#------------ Basic resource
# class CompanyResource(ModelResource):

#     class Meta:
#         queryset = Company.objects.all()


#------------ Allowing GET/POST/PUT/DELETE
# class CompanyResource(ModelResource):

#     class Meta:
#         queryset = Company.objects.all()
#         authorization = Authorization()


#------------ Adding more resources
# class StockResource(ModelResource):
#     company = fields.ToOneField('app.api.CompanyResource', 'company')

#     class Meta:
#         queryset = Stock.objects.all()


#------------ Excluding fields
# class StockResource(ModelResource):
#     company = fields.ToOneField('app.api.CompanyResource', 'company')

#     class Meta:
#         queryset = Stock.objects.all()
#         resource_name = 'stock'
#         excludes = ['Open', 'High', 'Low']

#------------ Showing exclusive fields
# class StockResource(ModelResource):
#     company = fields.ToOneField('app.api.CompanyResource', 'company')

#     class Meta:
#         queryset = Stock.objects.all()
#         resource_name = 'stock'
#         fields = ['company', 'Date', 'Volume']


#------------ Limiting access
# class StockResource(ModelResource):
#     company = fields.ToOneField('app.api.CompanyResource', 'company')

#     class Meta:
#         queryset = Stock.objects.all()
#         resource_name = 'stock'
#         fields = ['company', 'Date', 'Volume']
#         allowed_methods = ['get']

#------------ Filtering & ordering
class CompanyResource(ModelResource):

    class Meta:
        queryset = Company.objects.all()
        authorization = Authorization()
        filtering = {
            'name': ['exact', 'startswith']
        }
        ordering = {
            'name': ['name']
        }

class StockResource(ModelResource):
    company = fields.ToOneField('app.api.CompanyResource', 'company')

    class Meta:
        queryset = Stock.objects.all()
        resource_name = 'stock'
        fields = ['company', 'Date', 'Volume']
        allowed_methods = ['get']
        filtering = {
            'company': ALL_WITH_RELATIONS,
            'Date': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }
