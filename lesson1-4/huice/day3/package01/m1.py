from . import hello
import imp

hello.hello_huice()
imp.reload(hello)

from . import subpackage.m
subpackage.m.print_m()
