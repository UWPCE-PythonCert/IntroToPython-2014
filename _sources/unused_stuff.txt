.. stuff to put somewhere...

switch?
--------

Many languages have a ``switch`` construct:

.. code-block:: js

    switch (expr) {
      case "Oranges":
        document.write("Oranges are $0.59 a pound.<br>");
        break;
      case "Apples":
        document.write("Apples are $0.32 a pound.<br>");
        break;
      case "Mangoes":
      case "Papayas":
        document.write("Mangoes and papayas are $2.79 a pound.<br>");
        break;
      default:
        document.write("Sorry, we are out of " + expr + ".<br>");
    }

.. nextslide::

**Not Python**

use ``if..elif..elif..else``

(or a dictionary, or subclassing....)

