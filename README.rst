=========================
DIRECT DQIT Prettyprinter
=========================

Converts a "checking spec file" (a CSV file, CR-LF terminated) into a
hopefully more readable HTML report.

There is also an experimental XLSX-reading version. Only one of the
two will survive.


Installation
------------

As a standard Python module::

    pip3 install --user direct_check_specs_prettyprinter_py-0.1.tar.gz




Usage
-----

Run as follows::

    prettyprint.py CRF_1_100_101_anthro.csv > CRF_1_100_101_anthro.html


Format
-------

Right now, the files is assumed to contain at least the columns
indicated below. Column headers are case-sensitive. Order is
irrelevant. Additional columns are ignored.  Charset is assumed UTF-8.

==================    ===========
Column name           Description
==================    ===========
SpecID                TBD 
CheckID               TBD
Xcheck                TBD
Database table        TBD
Field                 TBD
Transform             TBD
Missing               TBD
Warning condition     TBD
Warning message       TBD  
Error condition       TBD
Error message         TBD
==================    ===========




Convert several files at once
-----------------------------

Assume the ``specs/`` directory contains several CSV files.
Use this loop::

    for i in specs/*.csv; do perl prettyprint.pl $i > $i.html; done



