2022.04.08.ctl 2022.04.08.ctl
====================
----
* Django 3.2 compatibility

2019.12.05.ctl 2019.12.05.ctl
====================
----
* Add missing comma to setup.py

2019.12.04 2019.12.04
====================
----
* Replace more instances of deprecated Field.rel with Field.remote_field

2019.11.22 2019.11.22
====================
----

* Replace deprecated Field.rel with Field.remote_field

2019.9.24 2019.9.24
====================
----

* Fixed EasyInstance python 3 string representation.


2018.12.10 2018.12.20
====================
----

* Added Python 3 support

2018.11.19 2018.11.19
====================
----

* Switch render_to_resonse to render to ensure full context is available.


2017.12.18 2017.12.18
====================
----

* Django 1.10 fixes -- Substitute deprecated model functionality

2017.12.15 2017.12.15

====================
----

* Django 1.10 fixes -- Remove RequestContext


2017.02.14 2017.02.14
====================
----

* Fix: Adding RequestContext to render_to_response calls


2016.2.26 2016.02.26
====================
----

* Fix: Adding error handling for any tinker that tries to insert random pk.

2014.9.26 2014.09.26
====================
----

* Fix: Running tests against Django>=1.7.
* Feature: Running travis-ci for multiple version of django.
* Fix: Handle ``LookupError`` on getting models.
* Feature: More documentation.
* Feature: Change version numbering to date based.


1.3 2013-11-30
==============
----

* Fix pagination
* Add many unit-tests

1.2 2013-06-10
==============
----

* Feature #11: Testing with sTravis-ci
* Fix OneToOneField support and then Model Inheritance

1.1 2013-02-21
==============
----

* Added ChangeLog.
* Fixed #1: i18n in templates.
* Fixed #3: Transifex for translation.
* Added locale file, and ready to translate.
* Fixed #9: A bug in ordering template tags, and sites.py.
* Fixed #8: Added Pagination.
