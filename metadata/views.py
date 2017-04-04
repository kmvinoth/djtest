from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.exceptions import FieldError, ObjectDoesNotExist
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import value_inline_form_set, deposit_value_inline_form_set, MetadataAttributesForm, \
    data_object_value_inline_form_set
from .models import Value, MetadataAttributes, DepositValue
from projects.models import Project, Deposit, DataObject
from projects.forms import DepositForm, DataobjectForm


@user_passes_test(lambda u: u.groups.filter(name='Project Admin').exists(), login_url='/projects/user_dashboard')
@login_required(login_url='/accounts/login')
def add_project_metadata(request, prj_name):
    prj_inst = Project.objects.get(project_name=prj_name)
    if request.method == 'POST':
        value_formset = value_inline_form_set(request.POST, request.FILES, instance=prj_inst)
        if value_formset.is_valid():
            value_formset.save()
            return redirect('/projects/admin')
        else:
            error = True
            print(error)
            value_formset = value_inline_form_set(instance=prj_inst)
            return render(request, 'metadata/add_project_metadata.html', {'formset': value_formset, 'error': error,
                                                                          'project_name': prj_name})
    else:
        value_formset = value_inline_form_set(instance=prj_inst)
        return render(request, 'metadata/add_project_metadata.html', {'formset': value_formset,
                                                                      'project_name': prj_name})


# Only project admin can add custom metadata fields
@user_passes_test(lambda u: u.groups.filter(name='Project Admin').exists(), login_url='/projects/user_dashboard')
@login_required(login_url='/accounts/login')
def add_custom_md_attributes(request, prj_name):

    if request.method == 'POST':
        custom_md_form = MetadataAttributesForm(request.POST)
        if custom_md_form.is_valid():
            custom_md_form.save()
        return redirect('/projects/admin')

    else:
        custom_md_form = MetadataAttributesForm()
        lst_custom_md_fields = MetadataAttributes.objects.filter(meta_data_level='deposit_md', meta_data_type='custom')
        return render(request, 'metadata/add_custom_md_fields.html', {'custom_md_form': custom_md_form,
                                                                      'project_name': prj_name,
                                                                      'lst_defined_label': lst_custom_md_fields})


@login_required(login_url='/accounts/login')
def member_metadata_view(request, prj_name):
    try:
        prj = Project.objects.get(project_name=prj_name)
        deposit_lst = Deposit.objects.filter(project_id=prj.id, user=request.user)
        return render(request, 'metadata/member_metadata_dashboard.html', {'project_name': prj,
                                                                           'deposit_lst': deposit_lst})

    except ObjectDoesNotExist:
        return HttpResponse('The project object does not exist')


@login_required(login_url='/accounts/login')
def create_deposit_session(request, prj_name):
    print(prj_name)
    if request.method == 'POST':
        deposit_form = DepositForm(request.POST)
        if deposit_form.is_valid():
            deposit_form.save()
            # Lesson learned : always use the 'namespace:urlname' in HttpResponseRedirect
        return HttpResponseRedirect(reverse('metadata:add_deposit', args=[prj_name]))

    else:
        deposit_form = DepositForm()
        return render(request, 'metadata/create_deposit.html', {'deposit_form': deposit_form,
                                                                'project_name': prj_name})


@login_required(login_url='/accounts/login')
def add_deposit_metadata(request, prj_name):
    # Get the last object of the deposit table, because that is recently added
    deposit_inst = Deposit.objects.last()
    if request.method == 'POST':
        deposit_value_formset = deposit_value_inline_form_set(request.POST, request.FILES, instance=deposit_inst)
        if deposit_value_formset.is_valid():
            deposit_value_formset.save()
            return redirect('/projects/admin')
        else:
            deposit_value_formset = deposit_value_inline_form_set(instance=deposit_inst)
            return render(request, 'metadata/add_deposit_metadata.html', {'deposit_formset': deposit_value_formset,
                                                                          'project_name': prj_name})
    else:
        deposit_value_formset = deposit_value_inline_form_set(instance=deposit_inst)
        return render(request, 'metadata/add_deposit_metadata.html', {'deposit_formset': deposit_value_formset,
                                                                      'project_name': prj_name})


# @login_required(login_url='/accounts/login')
# def lst_deposit_session(request, prj_name):
#     try:
#         prj_inst = Project.objects.get(project_name=prj_name)
#         edit_deposit_lst = Deposit.objects.filter(project_id=prj_inst.id, user=request.user)
#         return render(request, 'metadata/lst_previous_deposit.html', {'project_name': prj_name,
#                                                                       'deposit_lst': edit_deposit_lst})
#     except ObjectDoesNotExist:
#         return HttpResponse('The project object does not exist')


@login_required(login_url='/accounts/login')
def edit_deposit_session(request, prj_name, dep_name):
    deposit_inst = Deposit.objects.get(deposit_name=dep_name)
    if request.method == 'POST':
        deposit_value_formset = deposit_value_inline_form_set(request.POST, request.FILES, instance=deposit_inst)
        if deposit_value_formset.is_valid():
            deposit_value_formset.save()
            return redirect('/projects/admin')
        else:
            deposit_value_formset = deposit_value_inline_form_set(instance=deposit_inst)
            return render(request, 'metadata/edit_deposit_metadata.html', {'deposit_formset': deposit_value_formset,
                                                                           'project_name': prj_name,
                                                                           'deposit_name': dep_name})
    else:
        deposit_value_formset = deposit_value_inline_form_set(instance=deposit_inst)
        return render(request, 'metadata/edit_deposit_metadata.html', {'deposit_formset': deposit_value_formset,
                                                                       'project_name': prj_name,
                                                                       'deposit_name': dep_name})

# Code for Data Deposit ends here #
# ###########################################################################################################################################################################
"""
 Below are the code for Data object

"""


@login_required(login_url='/accounts/login')
def create_dataobject(request, prj_name, dep_name):
    print(prj_name)
    if request.method == 'POST':
        dataobject_form = DataobjectForm(request.POST)
        if dataobject_form.is_valid():
            dataobject_form.save()
            # Lesson learned : always use the 'namespace:urlname' in HttpResponseRedirect
        return HttpResponseRedirect(reverse('metadata:add_dataobject', args=[prj_name, dep_name]))

    else:
        dataobject_form = DataobjectForm()
        return render(request, 'metadata/create_dataobject.html', {'dataobject_form': dataobject_form,
                                                                   'project_name': prj_name,
                                                                   'deposit_name': dep_name})


@login_required(login_url='/accounts/login')
def add_dataobject_metadata(request, prj_name, dep_name):
    # Get the last object of the deposit table, because that is recently added
    data_object_inst = DataObject.objects.last()
    if request.method == 'POST':
        data_object_value_formset = data_object_value_inline_form_set(request.POST, request.FILES,
                                                                      instance=data_object_inst)
        if data_object_value_formset.is_valid():
            data_object_value_formset.save()
            return redirect('/projects/admin')
        else:
            data_object_value_formset = data_object_value_inline_form_set(instance=data_object_inst)
            return render(request, 'metadata/add_data_object_metadata.html',
                          {'data_object_formset': data_object_value_formset, 'project_name': prj_name,
                           'deposit_name': dep_name})
    else:
        data_object_value_formset = data_object_value_inline_form_set(instance=data_object_inst)
        return render(request, 'metadata/add_data_object_metadata.html',
                      {'data_object_formset': data_object_value_formset, 'project_name': prj_name,
                       'deposit_name': dep_name})



















