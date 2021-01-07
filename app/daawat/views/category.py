from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import  check_password
from django.views import  View
from cassandra.util import min_uuid_from_time
from datetime import datetime, timedelta

from daawat.model.categorys import Categorys
from daawat.service.astra_service import *

class Category(View):
    def get(self , request):
        return redirect('hotel')

    def post(self , request):
        userEmail = request.session["user"]
        hotel_id = request.session["hotelid"]

        now = datetime.utcnow()
        category_id = min_uuid_from_time(now)
        
        if astra_service.check_connection() == False:
            astra_service.connect()
        
        postData = request.POST
        category_name = postData.get('category_name')
        
        category = Categorys(category_id,category_name,userEmail,hotel_id)
        astra_service.create_new_category(category)
        messages.success(request,'Successfully added the '+category_name+' category !!')
        return redirect('hotel')


