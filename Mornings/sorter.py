import sys

debug = False


def read_data():
    """
    Reads a data set from stdin and returns a list of records for further
    processing.  Each record is a tuple with each member being a,
    possibly complex Python data structure.

    The first element of the tuple is assumed to be a unique record id.
    """
    data = []
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            continue

        # DANGER DANGER - this eval can cause program execution hacks!
        # Only consume data from a trusted source.

        data.append(eval(line))

    return data


def write_sort(sorted_records):
    """
    Writes to stdout the rid's of the each record in list of sorted records.
    """

    print([data[0] for data in sorted_records])


def display_sort(test_num, sorted_records):
    """
    Displays records on stderr, line by line
    """

    if not debug:
        return

    sys.stderr.write("\n*** Test {} ***\n".format(test_num))
    for r in sorted_records:
        sys.stderr.write("\n")
        sys.stderr.write(str(r))
        sys.stderr.write("\n")


"""
run this program as
    !ipython3 sorter.py < ../test-cases/as-275-8-sorter.py-test/Inputs/test00-stdin.txt

where data_input_file is one of the input test cases.

The data structure read from the input file will look like this:
Pos:
  0    1    2        3           4        5              6
( rid, str, [ str ], (int, int), [ int ], dict:key->int, dict:key->(str, str) )

and be stored in the variable data_set

You must run the sorts in the order indicated.

The solution of the first sort example is shown below. Note how the key
function is called f0, f1, etc. You just need to implement the
function. If you know about lambda functions for key functions, you can
also do that.

IMPORTANT NOTE: Make sure that your sort is stable, in that when records
are equal with respect to the sorting criterion, their order in the
original data set is preserved.

"""
data_set = read_data()


# Sort by the record id (rid) in pos 0
def f0(r):
    return r[0]


s = sorted(data_set, key=f0)
write_sort(s)


# Sort by string in pos 1
def f1(r):
    a = [i for i in r[1]]
    return a


s = sorted(data_set, key=f1)
write_sort(s)


# Sort by length of list of strings in pos 2
def f2(r):
    return len(r[2])


s = sorted(data_set, key=f2)
write_sort(s)


# Sort by the smallest value in the list of integers at position 4, and in
# the event of a tie, sort by string in position 1
# If the list of integers is empty, use a min of zero by
#   min(list, default = 0)
def f3(r):
    a = min(r[4],default = 0),f1(r)
    return a


s = sorted(data_set, key=f3)
write_sort(s)


# Sort by the smallest key in the dictionary at pos 5
# If the dictionary is empty, use a min of zero by
#   min(keys, default = 0)
def f4(r):
    b = min(r[5].items(),default=0)
    return b


s = sorted(data_set, key=f4)
write_sort(s)


# Sort by the smallest of the keys in the dictionary at pos 5 or pos 6
# If a dictionary is empty, use a min of zero by
#   min(keys, default = 0)
def f5(r):
    b = min(r[5].items()|r[6].items(),default=0)
    return b


s = sorted(data_set, key=f5)
write_sort(s)

# Identify all records in which at least one of the integers in the list
# at pos 4 is a value in the dictionary in pos 5. Put all the records
# that don't have this property before all the records that do have
# this property.


def f6(r):
    tmp = []
    for i in r[4]:
        if i in r[5].values():
            return True
    return False

s = sorted(data_set, key=f6)
write_sort(s)
