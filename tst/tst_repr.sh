#!/bin/sh

# $1 script
# $2 input file
# $3 expected output
# $4 comparator

OUTPUT=`mktemp`
$1 $2 $OUTPUT
$4 $3 $OUTPUT
