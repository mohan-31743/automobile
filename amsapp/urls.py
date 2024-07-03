from django.urls import path
from .import views
urlpatterns=[
    path("", views.first1, name="first"),
    path("home",views.homepage,name="homepage"),
    path("all",views.all,name="allpages"),
    path("index",views.first1,name="index"),
    path("registration",views.registration,name="registration"),
    path("login",views.login,name="login"),
    path("models",views.types,name="types"),
    path("slot",views.slot,name="slot"),
    path("createprod",views.cp,name="createprod"),
    path("about",views.about,name="about"),
    path("feedback",views.feedback,name="feedback"),
    path("saveUserfunction",views.saveUserfunction,name="saveUser"),
    path("addUserfunction",views.addUserfunction,name="addUserfunction"),
    path("addproductfunction",views.saveproductfunction,name="createproduct"),
    path("savefeedbackfunction",views.savefeedbackfunction,name="savefeedbackfunction"),


    path("updateproductfunction",views.updateproductfunction,name="updateproductfunction"),
    path("updateproduct",views.up,name="updateproduct"),

    path("spares",views.getproductfunction,name="getproductfunction"),
    path("orderprod/<int:pid>/",views.orderprodfunction,name="orderprodfunction"),

    path("userlogin",views.userlogin,name="userlogin"),

    path("gets",views.getsession,name="gets"),
    path("logout",views.logout,name="logout"),

    path("profile",views.user_profile,name="profile"),

    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('otp_verification/', views.otp_verification, name='otp_verification'),
    path('new_password/', views.new_password, name='new_password'),

    path("addcategoryfun/",views.addcategoryfunction,name='addcategoryfun'),
    path("addcategory/",views.addcategory,name='addcategory'),
    path("categories/",views.getcategoryfunction,name='categories'),
    path("categories/<int:pid>/",views.viewcategoryproductfunction,name="categories"),
    path('cart/', views.view_cart, name='cart'),


    path('addcartfun',views.add_cart,name="addcartfun"),
    path('addpayment/<str:id>/<int:price>',views.add_payment,name='payment'),
    path('showpayment/',views.showpayment,name="showpayment"),
    path('deleteallcart',views.deletecart,name="deletecartprod"),
    path('viewproducts',views.allproducts,name="allp"),

    path('updaterole/<str:pid>/<int:rid>/',views.updaterole,name="uprole"),
    path("deleteuser/<int:uid>",views.deleteuser,name="deleteuser"),
    path("deletcat/<int:uid>",views.deletecat,name="deletecat"),
    path("deleteprod/<int:uid>",views.deleteprod,name="deleteprod"),

    path('addwalletpayment/<str:id>/<int:price>',views.addwallet_payment,name='payment'),
    path('rwalletpayment',views.remwallet_payment,name='rempaywallet'),
    path("wallet",views.wallet,name="logout"),

]
