%module kcftracker
%include "opencv.i"
%include "cpointer.i"
%include "typemaps.i"
%include "std_string.i"

%{
#include "tracker.h"
#include "kcftracker.hpp"
%}

%include "tracker.h"
%include "kcftracker.hpp"

