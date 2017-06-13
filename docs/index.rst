*********************************
Data Deposit Portal documentation
*********************************

Introduction
============
The goal of this project is to develop a web-based tool to upload data in a standardized way including the acquisition of mandatory and optional metadata (See here_ for detailed information).

.. _here: http://www.zib.de/projects/online-portal-data-transfer-external-collaborators

Project setup
=============

Clone the repository from git using the command::

    git clone git@git.zib.de:rdm-deposit/djtest.git

Follow the detailed README.MD to set the project, up and running locally.

Functionalities
===============
Below is the list of functionalities that are implemented in the project.

User
----
* **User** registration.
* **Login** & **Logout** (No LDAP as of now).
* **Password** change & reset.
* **User Profile**.

Project Admin
-------------
* **Add** Project information.
* **Create** Users (Under User Management).
* **Add** and **Edit** (only user role) User to a project.
* **Add** project metadata.
* **Define** custom metadata (Deposit and Dataobject) fields.

Project Member
--------------
* **Initiate**(Create) a **Deposit session**.
* **Add** and **Edit** Deposit metadata.
* **Add DataObject** metadata (no edit option).
* **File upload** (not implemented as of now).
* **Close** the Deposit session.
* **Serialize** metadata of the deposit session.
* **Purge** the database after serialization.

Examples
========




Details
=======


.. toctree::
   :maxdepth: 2


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
