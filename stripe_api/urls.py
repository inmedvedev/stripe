from django.urls import path
from . import views


urlpatterns = [
    path('buy/<int:id>', views.BuyView.as_view()),
    path('item/<int:id>', views.ItemView.as_view()),
    path('success', views.SuccessView.as_view()),
    path('cancel', views.CancelView.as_view())
]
