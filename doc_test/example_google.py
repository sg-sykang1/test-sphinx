# -*- coding: utf-8 -*-
"""Example Google style docstrings.  # module summary

# module description
This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

# section name:
# section description
# Example에는 함수, method, 모듈 등의 사용 예시를 작성
Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::
    # :: <- html에서 코드 블록 생성을 위해 사용

        $ python example_google.py

# section은 unindented text가 시작되거나 새 section이 시작되면 break
Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

# Attributes에는 모듈이나 class 등이 가지고 있는 속성을 작성
Attributes:
    # 변수 (자료형): 설명, attribute 대신 inline docstring에 설명해도 되나
    # 중요한 것은 모듈 내에서 한 방식만 일관되게 사용하기
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

# Todo는 앞으로 해야 할 일 작성
Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

module_level_variable1 = 12345

module_level_variable2 = 98765
# inline docstring 예시, 변수 바로 아래에 작성
# 자료형: description 형식으로 작성하며 여러 줄이 될 수도 있음
"""int: Module level variable documented inline.

The docstring may span multiple lines. The type may optionally be specified
on the first line, separated by a colon.
"""


def function_with_types_in_docstring(param1, param2):
    # function docstring 예시
    # PEP484에서 정의된 type annotation 사용 가능, attribute, parameter, return의 type이
    # annotation 되어 있는 경우 docstring에 추가할 필요 없음
    """Example function with types documented in the docstring.

    # "`이름`_": 하이퍼링크, 뒤에서 ".. _이름:"으로 하이퍼링크 정의
    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Args:
        # parameter (자료형): 설명.
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        # 변수형: 설명
        bool: The return value. True for success, False otherwise.

    # 위 `PEP 484`_를 받아 하이퍼링크 추가
    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """

# PEP484 annotation 예시, attribute, parameter, return의 자료형이 annotation되어 있어서
# Args에서 자료형에 대한 부분 제외
def function_with_pep484_type_annotations(param1: int, param2: str) -> bool:
    """Example function with PEP 484 type annotations.

    Args:
        param1: The first parameter.
        param2: The second parameter.

    Returns:
        The return value. True for success, False otherwise.

    """

# module 수준 함수에 대한 docstring 예시
def module_level_function(param1, param2=None, *args, **kwargs):
    # summary
    """This is an example of a module level function.

    # description
    # parameter 이름은 필수 항목이며 자료형 및 description은 선택 사항
    # ``단어``: html에서 keyword 강조 표시?
    Function parameters should be documented in the ``Args`` section. The name
    of each parameter is required. The type and description of each parameter
    is optional, but should be included if not obvious.

    # 만약 \*args, \*\*kwargs가 사용되는 경우 반드시 목록에 포함
    If \*args or \*\*kwargs are accepted,
    they should be listed as ``*args`` and ``**kwargs``.

    The format for a parameter is::

        # 이름 (자료형, optional): 설명, line은 모두 동일하게 indentation되어야 함
        name (type): description
            The description may span multiple lines. Following
            lines should be indented. The "(type)" is optional.

            Multiple paragraphs are supported in parameter
            descriptions.

    # Args는 html에서 Parameters로 자동 변경
    Args:
        param1 (int): The first parameter.
        # :obj: <- python 내부 keyword 표시?, `단어`: consolas로 강조
        # 두 번째 줄부터는 추가 indentation 필요
        param2 (:obj:`str`, optional): The second parameter. Defaults to None.
            Second line of description should be indented.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        bool: True if successful, False otherwise.

        # 자료형은 선택사항이며 Returns 바로 아래에서 ":"으로 구분됨
        The return type is optional and may be specified at the beginning of
        the ``Returns`` section followed by a colon.

        # 여러 줄인 경우 첫 번째 줄과 동일하게 indentation
        The ``Returns`` section may span multiple lines and paragraphs.
        Following lines should be indented to match the first line.

        The ``Returns`` section supports any reStructuredText formatting,
        including literal blocks::

            {
                'param1': param1,
                'param2': param2
            }

    # Raises에서는 인터페이스와 연관있는 모든 예외 기술
    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.

    """
    if param1 == param2:
        raise ValueError('param1 may not be equal to param2')
    return True


def example_generator(n):
    # generator docstring의 예시, return 대신 yield 사용
    """Generators have a ``Yields`` section instead of a ``Returns`` section.

    Args:
        n (int): The upper limit of the range to generate, from 0 to `n` - 1.

    Yields:
        int: The next number in the range of 0 to `n` - 1.

    Examples:
        # example은 doctest를 실행할 수 있는 형태로 작성되어야 하며 어떻게 사용하는지
        # 예시를 보여주어야 한다.
        Examples should be written in doctest format, and should illustrate how
        to use the function.

        >>> print([i for i in example_generator(4)])
        [0, 1, 2, 3]

    """
    for i in range(n):
        yield i


class ExampleError(Exception):
    # Exception 하위 클래스 예시 - 새로운 exception 정의
    # class와 동일한 방식으로 docstring 생성
    """Exceptions are documented in the same way as classes.

    # __init__ method는 class docstring이나 __init__ method docstring에서 기술
    # 어느 방법을 택하던지 module 수준에서는 한 방식으로 통일하기
    The __init__ method may be documented in either the class level
    docstring, or as a docstring on the __init__ method itself.

    Either form is acceptable, but the two should not be mixed. Choose one
    convention to document the __init__ method and be consistent with it.

    # Note에는 주의 사항 작성
    Note:
        Do not include the `self` parameter in the ``Args`` section.

    Args:
        msg (str): Human readable string describing the exception.
        code (:obj:`int`, optional): Error code.

    Attributes:
        msg (str): Human readable string describing the exception.
        code (int): Exception error code.

    """

    def __init__(self, msg, code):
        self.msg = msg
        self.code = code


class ExampleClass(object):
    # docstring summary는 반드시 한 줄로 표기
    """The summary line for a class docstring should fit on one line.

    # class가 public 속성을 가지고 있는 경우 "Attributes" 섹션에 정리하고
    # 함수의 "Args" 섹션과 동일한 방식으로 정리
    # 아니면 attribute 선언문에서 inline 방식으로 docstring 작성
    If the class has public attributes, they may be documented here
    in an ``Attributes`` section and follow the same formatting as a
    function's ``Args`` section. Alternatively, attributes may be documented
    inline with the attribute's declaration (see __init__ method below).

    #"@property" decorator로 생성된 property의 경우 getter method에 기술
    Properties created with the ``@property`` decorator should be documented
    in the property's getter method.

    # html에서는 안 보이는데 어디서 확인하는지 체크 필요
    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """

    def __init__(self, param1, param2, param3):
        """Example of docstring on the __init__ method.

        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.

        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            param1 (str): Description of `param1`.
            param2 (:obj:`int`, optional): Description of `param2`. Multiple
                lines are supported.
            param3 (:obj:`list` of :obj:`str`): Description of `param3`.

        """
        self.attr1 = param1
        self.attr2 = param2
        # inline docstring 예시, #: <- inline docstring 선언, "*단어*": 이탤릭화
        self.attr3 = param3  #: Doc comment *inline* with attribute

        # attribute 앞에서 docstring 예시, type 선언 추가
        #: list of str: Doc comment *before* attribute, with type specified
        self.attr4 = ['attr4']

        self.attr5 = None
        # attribute 뒤에서 docstring 예시, type 선언 추가
        """str: Docstring *after* attribute, with type specified."""

    # property는 반드시 getter에서 property에 대한 docstring 작성
    @property
    def readonly_property(self):
        """str: Properties should be documented in their getter method."""
        return 'readonly_property'

    # property에 getter와 setter가 있는 경우 getter에서 양쪽에 대한 docstring 작성
    # setter에서 별도의 작업이 포함된 경우 서술
    @property
    def readwrite_property(self):
        """:obj:`list` of :obj:`str`: Properties with both a getter and setter
        should only be documented in their getter method.

        If the setter method contains notable behavior, it should be
        mentioned here.
        """
        return ['readwrite_property']

    @readwrite_property.setter
    def readwrite_property(self, value):
        value

    def example_method(self, param1, param2):
        # class method의 경우 일반적인 함수와 유사하게 docstring 작성
        # self는 Args 섹션에서 제외하기
        """Class methods are similar to regular functions.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            param1: The first parameter.
            param2: The second parameter.

        Returns:
            True if successful, False otherwise.

        """
        return True

    # dunder method (=magic method)는 html에서 제외
    # 추가하고 싶은 경우 conf.py에 관련 옵션을 True로 변경해야 됨
    def __special__(self):
        """By default special members with docstrings are not included.

        Special members are any methods or attributes that start with and
        end with a double underscore. Any special member with a docstring
        will be included in the output, if
        ``napoleon_include_special_with_doc`` is set to True.

        This behavior can be enabled by changing the following setting in
        Sphinx's conf.py::

            napoleon_include_special_with_doc = True

        """
        pass

    def __special_without_docstring__(self):
        pass

    # private member들에 대해서도 html에서 제외
    # special과 마찬가지로 conf.py에서 별도 옵션을 True로 주지 않으면 포함 X
    def _private(self):
        """By default private members are not included.

        Private members are any methods or attributes that start with an
        underscore and are *not* special. By default they are not included
        in the output.

        This behavior can be changed such that private members *are* included
        by changing the following setting in Sphinx's conf.py::

            napoleon_include_private_with_doc = True

        """
        pass

    def _private_without_docstring(self):
        pass