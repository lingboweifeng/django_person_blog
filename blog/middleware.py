from django.utils.deprecation import MiddlewareMixin
from myblog.models import Counts

class CountMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            count_nums=Counts.objects.get(id=1)
        except Counts.DoesNotExist:
            count_nums=Counts()
            count_nums.visit_nums += 1
            count_nums.save()
        count_nums.visit_nums += 1
        count_nums.save()