# -*- coding:utf-8 -*-

from django.shortcuts import render
from common.util.pagination import Pagination

# Create your views here.

def index(request):

    try:  
        cur_page = int(request.GET.get('cur_page', '1'))  
    except ValueError:  
        cur_page = 1  
  
    # 创建分页数据
    pagination = Pagination.create_pagination(
                                      from_name='mysite.models', 
                                      model_name='Employee',
                                      cur_page=cur_page,
                                      start_page_omit_symbol = '...',
                                      end_page_omit_symbol = '...',
                                      one_page_data_size=10,
                                      show_page_item_len=9)
  
    return render(request, 'index.html',{'pagination':pagination})
