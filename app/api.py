from app.models import Company, Stock
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.exceptions import BadRequest
from tastypie.paginator import Paginator
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS


class CompanyResource(ModelResource):

    class Meta:
        queryset = Company.objects.all()
        # authorization = Authorization()
        # list_allowed_methods = ['get', 'post', 'delete']
        # detail_allowed_methods = ['get', 'post', 'delete']
        # filtering = {
        #     'company': ALL_WITH_RELATIONS,
        #     'classification': ('exact',)
        # }


class StockResource(ModelResource):
    company = fields.ToOneField('app.api.CompanyResource', 'company')

    class Meta:
        queryset = Stock.objects.all()
