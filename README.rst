A standards compliant UUIDv8 implementation using the [XKCD 221 random number algorithm](https://xkcd.com/221/).

What is this?
=============

[RFC 9562 - Universally Unique IDentifiers (UUIDs)](https://datatracker.ietf.org/doc/rfc9562/) defines the UUIDv8 format as:

    UUIDv8 provides a format for experimental or vendor-specific use
    cases.  The only requirement is that the variant and version bits
    MUST be set as defined in Sections 4.1 and 4.2.

This library uses the XKCD 221 random number algorithm.
This algorithm is special in that it does not provide unique values; it can only produce the number four.
Accordingly, this implementation of UUIDv8 is special in that it does not produce unique values.


Wait, shouldn't all UUIDs be unique?
====================================

The name Universally Unique IDentifiers kinda implies uniqueness, right?

Here's RFC 9562 again:

    UUIDv8's uniqueness will be implementation specific and MUST NOT be assumed.

This library takes this to the extreme; producing the exact same UUID on each invocation.
Accordingly, the author requests that UUID implementations document what properties users should expect from their specific implementation.


Is this a real concern?
=======================

A [blog post series](https://alexsci.com/blog/uuid-collection/) accompanies this library.
A [catalog of real-world UUID collisions](https://alexsci.com/blog/uuid-oops/) shows problems even when using RFC-compliant implementations.


Usage
=====

.. code-block:: python

    import uuidv8_xkcd_221
    print(uuidv8_xkcd_221.generate())
    print(uuidv8_xkcd_221.generate())
    print(uuidv8_xkcd_221.generate())

Which prints:

    UUID('00000000-0000-8000-8000-000000000004')
    UUID('00000000-0000-8000-8000-000000000004')
    UUID('00000000-0000-8000-8000-000000000004')


Security
========

The author of the XKCD webcomic, Randall Munroe, rolled a fair dice when developing his random number algorithm.
However, more information is needed to understand what properties this dice had.
Randall's comics clearly demonstrate that he [knows about securely generating random numbers](https://xkcd.com/2626/) and may have access to [dice with exotic properties](https://xkcd.com/708/).

But seriously, no, it's not a cryptographically secure random number generator.


Installation
============

Don't install this.


Disclaimer
==========

This UUID algorithm is inspired by, but not related to, the wonderful [XKCD web comic](https://xkcd.com/).
