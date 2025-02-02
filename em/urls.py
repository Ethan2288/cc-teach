from django.urls import path, re_path, reverse_lazy
from django.views.generic import RedirectView
from .views import *

urlpatterns = [
    path('model/', ModelList.as_view(), name='model_list'),
    path('model/new/', ModelCreate.as_view(), name='model_create'),
    path('model/<int:mid>/', ModelView.as_view(), name='model_view'),
    path('model/<int:mid>/edit/', ModelEdit.as_view(), name='model_edit'),
    path('model/<int:mid>/new/', EquipCreate.as_view(), name='equip_create'),
    path('', RedirectView.as_view(url=reverse_lazy('model_list'))),
    path('equip/<int:eid>/', EquipView.as_view(), name='equip_view'),
    path('equip/<int:eid>/edit/', EquipEdit.as_view(), name='equip_edit'),
    path('equip/<int:eid>/new/', EquipLogCreate.as_view(), name='equip_log_create'),
    path('equip/<int:eid>/<int:lid>/return/', LogReturn.as_view(), name='equip_log_return'),
    path('equip/<int:eid>/<int:lid>/', LogEdit.as_view(), name='equip_log_edit'),
    path('equip/<int:eid>/<int:lid>/delete/', LogDelete.as_view(), name='equip_log_delete'),
    path('applicant/', ApplicantList.as_view(), name='applicant_list'),
    path('applicant/<int:aid>/', ApplicantView.as_view(), name='applicant_view'),
    path('applicant/new/', ApplicantCreate.as_view(), name='applicant_create'),
    path('applicant/<int:aid>/edit/', ApplicantEdit.as_view(), name='applicant_edit'),
    path('applicant/<int:aid>/new/', ApplicantLogCreate.as_view(), name='applicant_log_create'),
    path('applicant/<int:aid>/<int:lid>/return', LogReturn.as_view(), name='applicant_log_return'),
    path('applicant/<int:aid>/<int:lid>/', LogEdit.as_view(), name='applicant_log_edit'),
    path('applicant/<int:aid>/<int:lid>/delete/', LogDelete.as_view(), name='applicant_log_delete'),
    path('si/', SIList.as_view(), name='si_list'), 
    path('si/new/', SICreate.as_view(), name='si_create'),
    path('si/<int:sid>/', SIView.as_view(), name='si_view'), 
    path('si/<int:sid>/edit/', SIEdit.as_view(), name='si_edit'),
    path('si/<int:sid>/delete/', SIDelete.as_view(), name='si_delete'),
    path('inventory/', InventoryList.as_view(), name='inventory_list'),
    path('inventory/new/', InventoryLogCreate.as_view(), name='inventory_log_create'),
    path('inventory/new/<int:eid>/', InventoryLogManualCreate.as_view(), name='inventory_log_manual_create'),
    path('inventory/<int:year>/', InventoryView.as_view(), name='inventory_view'),
    path('inventory/<int:year>/delete/<int:ilid>/', InventoryLogDelete.as_view(), name='inventory_log_delete'),
    path('inventory/import/', InventoryImport.as_view(), name='inventory_import'),
    path('t/a/r/<int:rid>', TestApplicantListByRole.as_view()),
    re_path('t/a/fn/(?P<fn>.*)', TestApplicantListByFamilyName.as_view()), 
    path('t/m/y/<int:year>', TestModelListByYearAfter.as_view()),
]
