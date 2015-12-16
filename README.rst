.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide_addons.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
collective.relationfieldwidget
==============================================================================

Adds a Related Items type output to Plone 5 Dexterity TTW form widgets
RelationList and RelationChoice

Features
--------

- Just replaces default widgets for display mode
- uses overrides.zcml to override ploen.app.z3cform RelatedItemsWidget


Examples
--------

This add-on can be seen in action at the following sites:
- Is there a page on the internet where everybody can see the features?


Documentation
-------------

Just install the product in plone, and you should be ready to go.


Translations
------------

This product has been translated into

- Klingon (thanks, K'Plai)


Installation
------------

Install collective.relationfieldwidget by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.relationfieldwidget


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.relationfieldwidget/issues
- Source Code: https://github.com/collective/collective.relationfieldwidget
- Documentation: https://docs.plone.org/foo/bar


Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@example.com


License
-------

The project is licensed under the GPLv2.
