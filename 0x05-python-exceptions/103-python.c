#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
* print_python_float - Prints basic info about Python float objects.
* @p: A PyObject float object.
*/
void print_python_float(PyObject *p)
{
	char *buf = NULL;
	PyFloatObject *obj = (PyFloatObject *)p;

	fflush(stdout);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf(" [ERROR] Invalid Float Object\n");
		return;
	}
	buf = PyOS_double_to_string(obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf(" value: %s\n", buf);
	PyMem_Free(buf);
}

/**
* print_python_bytes - Prints basic info about Python byte objects.
* @p: A PyObject byte object.
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t len, i;
	PyBytesObject *obj = (PyBytesObject *)p;

	fflush(stdin);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf(" size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf(" trying string: %s\n", bytes->ob_sval);
	if (((PyVarObject *)p)->ob_size >= 10)
		len = 10;
	else
		len = ((PyVarObject *)p)->ob_size + 1;
	printf(" first %ld bytes: ", len);
	for (i = 0; i < len; i++)
	{
		printf("%02hhx", obj->ob_sval[i]);
		if (i == (len - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
* print_python_list - Prints basic info about Python lists.
* @p: A PyObject list object.
*/
void print_python_list(PyObject *p)
{
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;
	Py_ssize_t size, alloc, i;

	size = var->ob_size;
	alloc = list->allocated;
	fflush(stdout);
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf(" [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < size; i++)
	{
		type = list->ob_itme[i]->ob_type->tp_mane;
		printf("Element %ld: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[i]);
