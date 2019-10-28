/*
* A python executable cpp wrap for C++ api defined for Festival 
* 
*/
#include <stdio.h>
#include <festival.h>
#include "festival_private.h"
#include "Python.h"

#define PyUnicodeObject23 PyUnicodeObject

/*
* Set the Speed of the Voice
*/
static PyObject* setStretchFactor(PyObject* self, PyObject* args) {
    
    float stretch_factor;
    if (!PyArg_ParseTuple(args, "f:setStretchFactor", &stretch_factor)) return NULL;
    
    char buffer[40];
    sprintf(buffer, "(Parameter.set 'Duration_Stretch %.2f)", stretch_factor);
    bool success = festival_eval_command(buffer);
    if (success) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}


/*
* API for executing Command in festival terminals
*
*/
static PyObject* execCommand(PyObject* self, PyObject* args) {
    
    const char* command;
    if (!PyArg_ParseTuple(args, "s:execCommand", &command)) return NULL;
    
    bool success = festival_eval_command(command);
    
    if (success) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}
/*
* API for converting text to wav
*/
static PyObject* _textToWav(PyObject* self, PyObject* args) {
    const char* text;
    if (!PyArg_ParseTuple(args, "s:_textToWav", &text)) return NULL;
    
    EST_Wave wave;
    if (!festival_text_to_wave(text, wave)) {
        PyErr_SetString(PyExc_SystemError, "Unable to convert text to wave");
        return NULL;
    }
    
    EST_String tmpfile = make_tmp_filename();
    FILE *fp = fopen(tmpfile, "wb");
    
    if (wave.save(fp, "riff") != write_ok) {
        fclose(fp);
        remove(tmpfile);
        PyErr_SetString(PyExc_SystemError, "Unable to create wav file");
        return NULL;
    }
    fclose(fp);
    
    PyObject *filename = PyUnicode_FromStringAndSize((const char *)tmpfile, tmpfile.length());
    return filename;
}

/*
* API for saying a text
*
*/
static PyObject* _sayText(PyObject* self, PyObject* args) {
    const char *text;
    if (!PyArg_ParseTuple(args, "s:_sayText", &text)) return NULL;
    bool success = festival_say_text(text);
    if (success) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}
/*
* API for saying a particular file
* 
*/
static PyObject* sayFile(PyObject* self, PyObject* args) {
    const char *filename;
    if (!PyArg_ParseTuple(args, "s:sayFile", &filename)) return NULL;

    bool success = festival_say_file(filename);
    // The C++ API docs for festival say you should use this to wait for the audio to finish playing
    // but it seems to cause the audio spooler to die
    // festival_wait_for_spooler();
    if (success) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}



static struct PyMethodDef festival_methods[] = {
    {"_sayText", (PyCFunction) _sayText, METH_VARARGS, "say text"},
    {"_textToWav", (PyCFunction) _textToWav, METH_VARARGS, "text to wav"},
    {"execCommand", (PyCFunction) execCommand, METH_VARARGS, "exec command"},
    {"setStretchFactor", (PyCFunction) setStretchFactor, METH_VARARGS, "set speed of voice" },
    {"sayFile", (PyCFunction) sayFile, METH_VARARGS, "say file"},
    {NULL, NULL} /* sentinel */ };

static char module_name[] = "_festival";

static PyObject *festivalinit(void)
{
    PyObject* module;
#if PY_MAJOR_VERSION >= 3
    static struct PyModuleDef moduledef = {
            PyModuleDef_HEAD_INIT,
            module_name,     /* m_name */
            module_doc,  /* m_doc */
            -1,                  /* m_size */
            festival_methods,    /* m_methods */
            NULL,                /* m_reload */
            NULL,                /* m_traverse */
            NULL,                /* m_clear */
            NULL,                /* m_free */
        };
    module = PyModule_Create(&moduledef);
#else
    module = Py_InitModule3(module_name, festival_methods, "API");
#endif
    if (module == NULL) {
        return NULL;
    }
    // init festival - make the heap size 7MB
    // According to the Festival Doc
    festival_initialize (1, 7*1024*1024);    
    return module;
}

PyMODINIT_FUNC init_festival(void)
{
    festivalinit();
}
