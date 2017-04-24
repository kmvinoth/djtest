from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import get_object_or_404
from .forms import value_inline_form_set, deposit_value_inline_form_set, MetadataAttributesForm, \
    data_object_value_inline_form_set
from .models import MetadataAttributes
from projects.models import Project, Deposit, DataObject
from projects.forms import DepositForm, DataobjectForm


@user_passes_test(lambda u: u.groups.filter(name='Project Admin').exists(), login_url='/projects/user_dashboard')
@login_required(login_url='/accounts/login')
def add_project_metadata(request, prj_name):

    """
    Check's the logged(in) user has a role 'Project Admin' and then render the form related to the Project metadata
    (i.e Value Table), so that the Project admin can add all the Metadata related to the Project
    """

    prj_inst = Project.objects.get(project_name=prj_name)
    if request.method == 'POST':
        value_formset = value_inline_form_set(request.POST, request.FILES, instance=prj_inst)
        if value_formset.is_valid():
            value_formset.save()
            return redirect('/projects/admin')
        else:
            error = True
            # print(error)
            value_formset = value_inline_form_set(instance=prj_inst)
            return render(request, 'metadata/add_project_metadata.html', {'formset': value_formset, 'error': error,
                                                                          'project_name': prj_name})
    else:
        value_formset = value_inline_form_set(instance=prj_inst)
        return render(request, 'metadata/add_project_metadata.html', {'formset': value_formset,
                                                                      'project_name': prj_name})


@user_passes_test(lambda u: u.groups.filter(name='Project Admin').exists(), login_url='/projects/user_dashboard')
@login_required(login_url='/accounts/login')
def add_custom_md_attributes(request, prj_name):
    """
    Check's the logged(in) user has a role 'Project Admin' and allow him to add custom meta data attributes
    (i.e Attributes Table) to the project. These meta data attributes are available only for 'Data Deposit'
    and 'Data Object'.
    """

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
    """
    Metadata dashboard for the project member, where the member can create a New Deposit and edit an existing Deposit
    """
    try:
        prj = Project.objects.get(project_name=prj_name)
        deposit_lst = Deposit.objects.filter(project_id=prj.id, user=request.user)
        return render(request, 'metadata/member_metadata_dashboard.html', {'project_name': prj.project_name,
                                                                           'deposit_lst': deposit_lst})
    except ObjectDoesNotExist:
        return HttpResponse('The project object does not exist')


@login_required(login_url='/accounts/login')
def create_deposit_session(request, prj_name):
    # print(prj_name)
    """
    Let's the Project member to create a deposit session for the Project, once a deposit session has been created
    the member is redirected to the page 'add Deposit metadata'.
    """
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
    """
    Let's the Project member to add the deposit meta data related to the project, redirected page once a deposit session
    is created by the member.
    """
    # Get the last object of the deposit table, because that is recently added
    deposit_inst = Deposit.objects.last()
    # get the deposit name from the deposit instance for HttpResponseRedirect
    dep_name = deposit_inst.deposit_name
    if request.method == 'POST':
        deposit_value_formset = deposit_value_inline_form_set(request.POST, request.FILES, instance=deposit_inst)
        if deposit_value_formset.is_valid():
            deposit_value_formset.save()
            return HttpResponseRedirect(reverse('metadata:add_dataobject', args=[prj_name, dep_name]))
        else:
            session_form = DepositForm(instance=deposit_inst)
            deposit_value_formset = deposit_value_inline_form_set(instance=deposit_inst)
            return render(request, 'metadata/add_deposit_metadata.html', {'deposit_formset': deposit_value_formset,
                                                                          'project_name': prj_name,
                                                                          'session_form': session_form})
    else:
        session_form = DepositForm(instance=deposit_inst)
        deposit_value_formset = deposit_value_inline_form_set(instance=deposit_inst)
        return render(request, 'metadata/add_deposit_metadata.html', {'deposit_formset': deposit_value_formset,
                                                                      'project_name': prj_name,
                                                                      'session_form': session_form})


@login_required(login_url='/accounts/login')
def edit_deposit_session(request, prj_name, dep_name):
    """
    Let's the Project member to edit the deposit meta data related to the project.
    """
    try:
        deposit_inst = get_object_or_404(Deposit, deposit_name=dep_name)
        if request.method == 'POST':
            deposit_value_formset = deposit_value_inline_form_set(request.POST, request.FILES, instance=deposit_inst)
            if deposit_value_formset.is_valid():
                deposit_value_formset.save()
                return HttpResponseRedirect(reverse('metadata:add_dataobject', args=[prj_name, dep_name]))
            else:
                session_form = DepositForm(instance=deposit_inst)
                deposit_value_formset = deposit_value_inline_form_set(instance=deposit_inst)
                return render(request, 'metadata/edit_deposit_metadata.html', {'deposit_formset': deposit_value_formset,
                                                                               'project_name': prj_name,
                                                                               'deposit_name': dep_name,
                                                                               'session_form': session_form})
        else:
            session_form = DepositForm(instance=deposit_inst)
            deposit_value_formset = deposit_value_inline_form_set(instance=deposit_inst)
            return render(request, 'metadata/edit_deposit_metadata.html', {'deposit_formset': deposit_value_formset,
                                                                           'project_name': prj_name,
                                                                           'deposit_name': dep_name,
                                                                           'session_form': session_form})
    except ObjectDoesNotExist:
        return Http404

""" ################################   The code for the Deposit ends here ###########################################"""


""" ################################ The code for Data object Start's from here #################################### """


@login_required(login_url='/accounts/login')
def add_dataobject_metadata(request, prj_name, dep_name):
    """
    Let's the Project member to add the Data object meta data related to the project, redirected page once a data object
    is created by the member.
    """
    # Get the last object of the deposit table, because that is recently added
    try:
        deposit_inst = get_object_or_404(Deposit, deposit_name=dep_name)
        # The below query has to be changed to filter when you have more than one data object for a deposit
        data_object_inst = DataObject.objects.get(deposit_id=deposit_inst.id)
        if request.method == 'POST':
            data_object_value_formset = data_object_value_inline_form_set(request.POST, request.FILES,
                                                                          instance=data_object_inst)
            if data_object_value_formset.is_valid():
                data_object_value_formset.save()
                return HttpResponseRedirect(reverse('metadata:member_metadata_view', args=[prj_name]))
            else:
                session_form = DepositForm(instance=deposit_inst)
                data_object_form = DataobjectForm(instance=data_object_inst)
                deposit_value_formset = deposit_value_inline_form_set(instance=deposit_inst)
                data_object_value_formset = data_object_value_inline_form_set(instance=data_object_inst)
                return render(request, 'metadata/add_data_object_metadata.html',
                              {'data_object_formset': data_object_value_formset,
                               'project_name': prj_name,
                               'deposit_name': dep_name,
                               'deposit_formset': deposit_value_formset,
                               'session_form': session_form,
                               'object_form': data_object_form
                               })
        else:
            session_form = DepositForm(instance=deposit_inst)
            data_object_form = DataobjectForm(instance=data_object_inst)
            deposit_value_formset = deposit_value_inline_form_set(instance=deposit_inst)
            data_object_value_formset = data_object_value_inline_form_set(instance=data_object_inst)
            return render(request, 'metadata/add_data_object_metadata.html',
                          {'data_object_formset': data_object_value_formset,
                           'project_name': prj_name,
                           'deposit_name': dep_name,
                           'deposit_formset': deposit_value_formset,
                           'session_form': session_form,
                           'object_form': data_object_form
                           })

    except ObjectDoesNotExist:
        return Http404


@login_required(login_url='/accounts/login')
def edit_data_object(request, prj_name, dep_name, object_name):
    """
    Let's the Project member to edit the Data object meta data related to the project.
    """
    data_object_inst = DataObject.objects.get(data_object_name=object_name)
    if request.method == 'POST':
        data_object_value_formset = data_object_value_inline_form_set(request.POST, request.FILES,
                                                                      instance=data_object_inst)
        if data_object_value_formset.is_valid():
            data_object_value_formset.save()
            return HttpResponseRedirect(reverse('metadata:object_dashboard', args=[prj_name, dep_name]))
        else:
            data_object_value_formset = data_object_value_inline_form_set(instance=data_object_inst)
            return render(request, 'metadata/edit_data_object_metadata.html',
                          {'object_formset': data_object_value_formset, 'project_name': prj_name,
                           'deposit_name': dep_name, 'object_name': object_name})
    else:
        data_object_value_formset = data_object_value_inline_form_set(instance=data_object_inst)
        return render(request, 'metadata/edit_data_object_metadata.html',
                      {'object_formset': data_object_value_formset, 'project_name': prj_name,
                       'deposit_name': dep_name, 'object_name': object_name})


@login_required(login_url='/accounts/login')
def data_object_dashboard(request, prj_name, dep_name):
    """
    DataObject dashboard for the project member, where the member can create a New Data object
    to an existing Deposit or edit an existing data object which is already created for the deposit.
    """
    try:
        deposit_inst = Deposit.objects.get(deposit_name=dep_name)
        data_object_lst = DataObject.objects.filter(deposit_id=deposit_inst.id, user=request.user)
        return render(request, 'metadata/dataobject_dashboard.html', {'project_name': prj_name,
                                                                      'dataobject_lst': data_object_lst,
                                                                      'deposit_name': dep_name})
    except ObjectDoesNotExist:
        return HttpResponse('The project object does not exist')


@login_required(login_url='/accounts/login')
def create_dataobject(request, prj_name, dep_name):
    # print(prj_name)
    """
    Let's the Project member to create a Data Object for the Project, once a data object has been created
    the member is redirected to the page 'add DataObject metadata'.
    """
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






















