from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(),name='post-list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post-detail'),
    path('post/new/',views.CreatePostView.as_view(), name='post-new'),
    path('post/<int:pk>/update/',views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/',views.PostDeleteView.as_view(), name='post-delete'),
    path('drafts/', views.DraftListView.as_view(), name='post-draft-list'),
    path('post/<int:pk>/comment/',views.add_comment_to_post, name='add-comment'),
    path('comment/<int:pk>/approve/',views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/',views.comment_remove, name='comment_remove'),
    path('post/<int:pk>/publish/',views.post_publish, name='post-publish'),

]
