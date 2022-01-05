from django.urls import re_path

from . import views

app_name = 'bookstore'
urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^account$', views.AccountView.as_view(), name='account'),
    re_path(r'^admin$', views.BookstoreAdminView.as_view(), name='admin'),
    re_path(r'^stats$', views.StatisticsView.as_view(), name='stats'),
    re_path(r'^cart$', views.CartView.as_view(), name='cart'),
    re_path(r'^cart/order', views.OrderView.as_view(), name='order'),
    re_path(r'^home$', views.home, name='home'),
    re_path(r'^login$', views.LoginFormView.as_view(), name='login'),
    re_path(r'^logout$', views.LogoutView.as_view(), name='logout'),
    re_path(r'^register$', views.RegistrationFormView.as_view(), name='register'),
    re_path(r'^book/(?P<bid>[a-zA-Z0-9]+)/review-filter-newest/(?P<rnum>[0-9]+)', views.review_filter_newest, name = 'review_filter_newest'),
    re_path(r'^book/(?P<bid>[a-zA-Z0-9]+)/review-filter-best/(?P<rnum>[0-9]+)', views.review_filter_best, name = 'review_filter_best'),
 	re_path(r'^book/(?P<bid>[a-zA-Z0-9]+)/add-to-cart$', views.add_to_cart, name = 'add_to_cart'),
 	re_path(r'^book/(?P<bid>[a-zA-Z0-9]+)/review$', views.review, name = 'review'),
    re_path(r'^book/(?P<bid>[a-zA-Z0-9]+)/review/rate/(?P<rid>[0-9]+)$', views.rate_user_review, name = 'rate_user_review'),
    
    re_path(r'^book/(?P<bid>[a-zA-Z0-9]+)', views.book_details, name = 'book_details'),
    re_path(r'^search/$', views.search, name='search'),
    re_path(r'^search/filter-author$', views.search_filter_author, name='search_filter_author'),
    re_path(r'^search/filter-year$', views.search_filter_year, name='search_filter_year'),
    re_path(r'^search/filter-score$', views.search_filter_score, name='search_filter_score'),
    re_path(r'^keyword/(?P<key>[a-zA-Z0-9]+)/(?P<specified>.*)$', views.search_specific, name='search_specific'),
]
