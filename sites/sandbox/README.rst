============
Sandbox site
============

This site is deployed to two locations:

http://sandbox.oscar.tangentlabs.co.uk/
---------------------------------------

This site is used for testing the vanilla Oscar functionality, that is, Oscar
without any customisation.  It is not a demo site for clients or potential Oscar
users.  It is built automatically from the HEAD of the master branch every 20
minutes.

http://qa.oscar.tangentlabs.co.uk/
----------------------------------

This site is for Tangent's QA team to test release candidates.  Like the sandbox
site, it is not customised but is built from fixed tags rather than continually
updated.


=====
Notes
=====

Django CMS
----------
Integration of Django CMS using version 3.0.1 which is compatible with
Django < 1.7 (Officially).

This is an example of upgrading Django CMS from 2.4.3 to 3.0.1.

Install the CMS and note that, unlike 2.4.3, you need to install the plugins
manually (they are listed in the installed apps).
