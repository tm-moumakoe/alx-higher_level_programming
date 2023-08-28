#include <stdio.h>
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_float - gives data of the PyFloatObject
 * @p: the PyObject
 */
void print_python_float(PyObject *p)
{
	double val = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	val = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}

/**
 * print_python_bytes - gives data of the PyBytesObject
 * @p: the PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t len = 0, i = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	len = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	str = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes:", len < 10 ? len + 1 : 10);
	while (i < len + 1 && i < 10)
	{
		printf(" %02hhx", str[i]);
		i++;
	}
	printf("\n");
}

/**
 * print_python_list - gives data of the PyListObject
 * @p: the PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t len = 0;
	PyObject *obj;
	int i = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		len = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", len);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (i < len)
		{
			obj = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, obj->ob_type->tp_name);
			if (PyBytes_Check(obj))
				print_python_bytes(obj);
			else if (PyFloat_Check(obj))
				print_python_float(obj);
			i++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
