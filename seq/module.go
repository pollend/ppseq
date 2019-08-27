package main

/*
#include "Python.h"
*/
import "C"

//export newSeq
func newSeq(self *C.PyObject, args *C.PyObject) *C.PyObject{
	var obj *C.PyObject;

	return obj;
}

var seqMethods = []C.PyMethodDef{
	{
		C.CString("_c.max"),
// 		C.PyCFunction(C.sum),
		C.METH_VARARGS, [4]byte{},
		C.CString("Add two numbers."),
	},
	{nil, nil, 0, [4]byte{}, nil},
}

func main() {}
