from django.urls import path
from course.views import ManageCourseListView, CourseCreateView, CourseUpdateView, CourseDeleteView, \
    CourseModuleUpdateView, ContentCreateUpdateView, ContentDeleteView, ModuleContentListView

app_name = 'course'

urlpatterns = [
    path(
        'mine/', ManageCourseListView.as_view(), name='course_list'),
    path(
        'create/', CourseCreateView.as_view(), name='course_create'),
    path(
        '<pk>/edit/', CourseUpdateView.as_view(), name='course_edit'),
    path(
        '<pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
    path(
        '<pk>/module/', CourseModuleUpdateView.as_view(), name='course_module_update'),
    path(
        'module/<int:module_id>/content/<module_name>/create/', ContentCreateUpdateView.as_view(),
        name='module_content_create'),
    path(
        'module/<int:module_id>/content/<module_name>/<id>/', ContentCreateUpdateView.as_view(),
         name='module_content_update'),
    path(
        'content/<int:id>/delete/', ContentDeleteView.as_view(), name='module_content_delete'),
    path(
        'module/<int:module_id>', ModuleContentListView.as_view(), name='module_content_list'),

]