.. doc_test documentation master file, created by
   sphinx-quickstart on Tue Jun 18 10:58:09 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to doc_test's documentation!
====================================
.. toctree::  # html 왼쪽의 table of contents tree
   :hidden:  # tree에는 아래 항목을 추가하나 본 page에서는 숨김

   Home <self>  # Name <실제 참조 경로>

.. toctree::
   :maxdepth: 2  # 최대로 출력할 depth
   :caption: Contents:  # 소제목

   modules  # module.rst를 참고하여 내용물 출력


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
