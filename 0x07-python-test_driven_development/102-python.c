#include "python.h"


/**
 * print_python_string - function that prints a python string.
 *
 * @p: object t be evaluated
 **/

void print_python_string(PyObject *p)
{
	unsigned int l;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf(" [ERROR] Invalid String Object\n");
		return;
	}


	l = ((PyASCIIObject *)(p))->l;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf(" type: compact ascii\n");

	else
		printf(" type: compact unicode object\n");
	printf(" length: %ld\n", l);
	printf(" value: %ls\n", PyUnicode_AsWideCharString(p, &l));
}
