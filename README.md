# NAME

hut - a Kibana dashboard template tool

# SYNOPSIS

**hut** [-h] [-f] *DIRECTORY* *OUTPUT*

# DESCRIPTION

Generates a Kibana JSON file called *OUTPUT* from a **template.json** file
in *DIRECTORY*. Available options are:

**-h**, **--help**

:   Show a help message and exit.

**-f**, **--force**

:   Write the JSON file even if the schema is invalid. Without this option,
    hut refuses to write the file. Either way, an error message describing
    the problem is be printed.

# TWIGS

Hut comes with a Python module offering convenience functions. You need to
import the **twigs** module at the top of your **template.json** as follows:

```
<%! import twigs %>
```

Functions from the **twigs** module are for instance called as follows:

```
[...]
"span": 4,
"title": "LSF",
"content": "${twigs.include('lsf.md')}",
"type": "text"
[...]
```

The following functions are available:

now()

:   Returns a human-readable string of the current time. This is for instance
    useful to display last change times in dashboards.

include(path)

:   Returns the contents of the file at **path**, replacing **\\n**
    by **\\\\n** to make it fit into a single line suitable for JSON. This
    is for instance useful to include Markdown contents.

links(path)

:   Adds a compact panel with links included from the file at **path**.
    This supports HTML entities so links may be e.g. `&bull;`-separated.

pulldowns(enable=True)

:   Sets up the display for queries and filters, or disable them.

nav(enable=True)

:   Sets up the timepicker menu, or disable it.

loader()

:   Sets up save and load menus.

Additionally, the **twigs** module offers the **colours** list, which
offers the 56 distinct shades which Kibana normally provides for queries.
You can define other functions and attributes in **template.json** itself, for
instance at the start of the file, and call them anywhere else in the template:

```
<%
def foo():
    return 'Foo'
%>

{
  "title": "${foo()} Monitoring Page"
}
```

# DASHBOARD DIRECTORY

Hut expects a *DIRECTORY* containing a file called **template.json**, which
is typically a Mako template (`http://www.makotemplates.org`). When run, it
moves into *DIRECTORY* such that any resource referred to from the template is
expected to be in the current *DIRECTORY*. For instance, consider a *DIRECTORY*
**home** containing **template.json** and **lsf.md**. This will create a
**text** panel including the contents of **lsf.md** with the **include()**
function which only needs its filename as path:

```
[...]
"span": 4,
"title": "LSF",
"content": "${twigs.include('lsf.md')}",
"type": "text"
[...]
```

# DASHBOARD SCHEMA

The Kibana dashboard schema is documented in
`https://www.elastic.co/guide/en/kibana/3.0/_dashboard_schema.html` but you
may want to start from an existing one on Kibana, export it to a JSON file
and work from there.  In a nutshell, there is

  - a title
  - services (for defining queries and filters)
  - a list of rows, each comprising a list of panels
  - index settings
  - pulldowns (for displaying queries and filters)
  - some navigation (e.g. the timepicker)
  - a loader
  - a style (light or dark)

You can remove keys and count on default values. You may then want to load
your JSON into Kibana, export the schema again and compare to see what those
defaults are.

The JSON expected by Kibana follows fairly strict rules. For instance,
items in lists and dictionaries are comma-separated but the last item
must not be followed with a comma. In a loop, this can be handled as follows:

```
<% i = 0 %>

% for queue in queues:

"${i}": {
  "id": ${i},
  "color": "${twigs.colours[i]}",
  "query": "${queue} AND status:PEND"
},
<% i += 1 %>

"${i}": {
  "id": ${i},
  "color": "${twigs.colours[i]}",
  "query": "${queue} AND status:RUN"
},
<% i += 1 %>

"${i}": {
  "id": ${i},
  "color": "${twigs.colours[i]}",
  "query": "${queue} AND status:PSUSP"
}${',' if i < len(queues) * 3 - 1 else ''}
<% i += 1 %>

% endfor
```

Note that you can use **<% print 'blah' %>** for printing to stdout.

# WRITING MANY DASHBOARDS

You can generate many similar dashboards from a single
template, as an alternative to templated and scripted dashboards
(`https://www.elastic.co/guide/en/kibana/3.0/templated-and-scripted-dashboards.html`),
which don't always support all types of values well. One approach
involves writing a generic template in *DIRECTORY*, making as many
symlinks as variations to this *DIRECTORY*, each with a meaningful name
(e.g. **lsf-grid-alice**), and resolve the variations from this name
(e.g. **alice**) for instance with:

```
<%
import sys, os
variation = os.path.basename(sys.argv[1].rstrip('/')).split('-')[-1]
%>
```
