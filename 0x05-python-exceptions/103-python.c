#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <stdlib.h>
#include <float.h>

/**
* print_python_bytes - Prints basic info about Python byte objects.
* @p: A PyObject byte object.
*/
void print_python_bytes(PyObject *p)
{
    long unsigned int size;
    unsigned int i;
    char *str = NULL;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;
    str = ((PyBytesObject *)p)->ob_sval;
    printf("  size: %lu\n", size);
    printf("  trying string: %s\n", str);
    if (size < 10)
        printf("  first %lu bytes:", size + 1);
    else
        printf("  first 10 bytes:");
    for (i = 0; i <= size && i < 10; i++)
        printf(" %02hhx", str[i]);
    printf("\n");
}

/**
* print_python_float - Prints basic info about Python float objects.
* @p: A PyObject float object.
*/
void print_python_float(PyObject *p)
{
    PyFloatObject *f = (PyFloatObject *)p;
    double d = f->ob_fval;
    char *str = NULL;

    printf("[.] float object info\n");
    if (!PyFloat_Check(f))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    str = PyOS_double_to_string(d, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", str);
}

/**
* print_python_list - Prints basic info about Python lists.
* @p: A PyObject list object.
*/
void print_python_list(PyObject *p)
{
    long unsigned int size;
    unsigned int i;
    PyListObject *l = (PyListObject *)p;
    const char *tp;

    printf("[*] Python list info\n");
    if (!PyList_Check(l))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;
    printf("[*] Size of the Python List = %lu\n", size);
    printf("[*] Allocated = %lu\n", l->allocated);
    for (i = 0; i < size; i++)
    {
        tp = (l->ob_item[i])->ob_type->tp_name;
        printf("Element %i: %s\n", i, tp);
        if (!strcmp(tp, "bytes"))
            print_python_bytes(l->ob_item[i]);
        if (!strcmp(tp, "float"))
            print_python_float(l->ob_item[i]);
    }
}
