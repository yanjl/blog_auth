# Copyright 2018 win10-pc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'blog'  # namespace
urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='blog/login.html'),
        name='login'),
    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name='blog/logout.html'),
        name='logout'),
    path('index/', views.BlogIndex.as_view(), name='index'),
    path('list/', views.BlogList.as_view(), name='list'),
    path('detail/<int:pk>/', views.BlogDetail.as_view(), name='detail'),
    path('publish/', views.BlogPublish.as_view(), name='publish'),
]
