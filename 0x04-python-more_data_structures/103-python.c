#include <stdio.h>
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints list information
 * @p: Python Object
 */

void print_python_list(PyObject *p)
{
	PyObject *obj;
	long i, size;
	PyListObject *list;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}

/**
 * print_python_bytes - Prints bytes information
 * @p: Python Object
 */

void print_python_bytes(PyObject *p)
{
	long size, i, lim;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;
	printf(" size: %ld\n", size);
	printf(" trying string: %s\n", str);

	if (size >= 10)
		lim = 10;
	else
		lim = size + 1;

	for (i = 0; i < limit; i++)
		if (str[i] >= 0)
			printf(" %02x", str[i]);
		else
			printf(" %02x", 256 + str[i]);
	printf("\n");
}
