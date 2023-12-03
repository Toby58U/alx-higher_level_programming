#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int size, allocated, i;
	PyListObject *list_obj = (PyListObject *)p;

	size = PyList_Size(p);
	allocated = list_object->allocated;

	printf("[*} Size of the Python list = %li\n", size);
	printf("[*] Allocated slots = %li\n", allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %li: %s\n", i, Py_TYPE(list_obj->ob_item[i]->tp_name);
	}
}
