import sublime
import sublime_plugin
import re


s = sublime.load_settings('TabsToTable.sublime-settings')

class Pref:
    def load(self):
        Pref.table_separator = s.get('table_separator', '  ')


Pref = Pref()
Pref.load()
s.add_on_change('reload', lambda:Pref.load())


class TabsToTable(sublime_plugin.TextCommand):
    def run(self, edit):
        sels = self.view.sel()

        for sel in sels:
            selected = self.view.substr(sel)

            tableText = self.normtable(selected)
            self.view.replace(edit, sel, tableText)

        self.view.sel().clear()

    # Original credit to Dr. Drang:
    # http://www.leancrew.com/all-this
    def normtable(self, text):
        # Start by turning the text into a list of lines.
        lines = text.splitlines()
        rows = len(lines)

        # Extract the content into a matrix.
        # Keep track of the number of cells per row.
        columns = 0
        content = []
        for line in lines:
            cells = line.split('\t')
            if len(cells) > columns:
                columns = len(cells)
            linecontent = [x.strip() for x in cells]
            content.append(linecontent)

        # Append cells to rows that don't have enough.
        rows = len(content)
        for i in range(rows):
            while len(content[i]) < columns:
                content[i].append('')

        # Get the width of the content in each column.
        # The minimum width will be 0.
        widths = [0] * columns
        for row in content:
            for i in range(columns):
                widths[i] = max(len(row[i]), widths[i])

        # Add whitespace to make all the columns the same width.
        # Separate columns with 2 spaces
        formatted = []
        for row in content:
            separation = [s.rjust(n) for (s, n) in zip(row, widths)]
            formatted.append(Pref.table_separator.join(separation))

        # Return the formatted table.
        return '\n'.join(formatted)
