from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('name', views.get_name, name='name'),
    path('result', views.result, name='result'),

    #Register, Login, About, Service, Contact
    path('about', views.about_view, name='about'),
    path('service', views.service_view, name='service'),
    # path('search', views.search_view, name='search'),
    #path('contact', views.contact_view, name='contact'),

    #Begin menu
    path('menu', views.menu_view, name='menu'),
    #Begin loss gain
    path('menu/LossGain', views.loss_gain_view, name='lossgain'),
    path('menu/lossgain/1000calo', views.loss_gain_paper_1_view, name='paper_lg(1)'),
    path('menu/lossgain/lowcarbs', views.loss_gain_paper_2_view, name='paper_lg(2)'),
    path('menu/lossgain/lowcalo', views.loss_gain_paper_3_view, name='paper_lg(3)'),
    path('menu/lossgain/lossgain_girl', views.loss_gain_paper_4_view, name='paper_lg(4)'),
    path('menu/lossgain/EatClean', views.loss_gain_paper_5_view, name='paper_lg(5)'),
    path('menu/lossgain/EatSuitable', views.loss_gain_paper_6_view, name='paper_lg(6)'),

    #Begin Vegan
    path('menu/Vegan', views.vegan_view, name='vegan'),
    path('menu/Vegan/VeganHealthy', views.vegan_paper_1_view, name='vegan_paper(1)'),
    path('menu/Vegan/VeganFood', views.vegan_paper_2_view, name='vegan_paper(2)'),
    path('menu/Vegan/VeganDesign', views.vegan_paper_3_view, name='vegan_paper(3)'),


    #Begin other
    path('menu/knowledge', views.other_view, name='other'),
    path('menu/knowledge/calo', views.other_paper_1_view, name='other_paper(1)'),
    path('menu/knowledge/taller', views.other_paper_2_view, name='other_paper(2)'),
    path('menu/knowledge/cheap_food', views.other_paper_3_view, name='other_paper(3)'),
    path('menu/knowledge/fruit', views.other_paper_4_view, name='other_paper(4)'),
    path('menu/knowledge/hieuqua', views.other_paper_5_view, name='other_paper(5)'),
    path('menu/knowledge/hanche', views.other_paper_6_view, name='other_paper(6)'),
    path('menu/knowledge/food_kid', views.other_paper_7_view, name='other_paper(7)'),

    # weight gain
    path('menu/WeightGain', views.weight_gain, name='weightgain'),
    path('menu/WeightGain/WeightGain_paper', views.weight_gain_paper, name='weightgainpaper'),
]

