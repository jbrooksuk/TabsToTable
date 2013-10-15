# Tabs To Table
Converts tabular data into a glorious table format.

# Installation
Available in Package Control, just search *TabsToTable*!

# Example
```
Position	Elevation
0.00	0.00
1.00	0.17
2.00	0.37
3.00	0.58
4.00	0.76
5.00	0.99
6.00	1.20
7.00	1.45
8.00	1.69
9.00	1.86
10.00	2.06
11.00	2.24
12.00	2.48
13.00	2.65
```

Converts to:

```
 Position  Elevation
	 0.00       0.00
	 1.00       0.17
	 2.00       0.37
	 3.00       0.58
	 4.00       0.76
	 5.00       0.99
	 6.00       1.20
	 7.00       1.45
	 8.00       1.69
	 9.00       1.86
	10.00       2.06
	11.00       2.24
	12.00       2.48
	13.00       2.65
```

# Usage
- **Windows:** <kbd>CTRL+Alt+T</kbd>
- **OSX:** <kbd>Super+Alt+T</kbd>
- **Linux:** <kbd>Ctrl+Alt+T</kbd>

# Configure
TabsToTable is customisable!

Valid settings are:

- `col_separator` - How are columns split up? For easier to read tables, I suggest using ` | `
- `col_align` - aligns text to the "left" or "right" of the column.
- `col_wrap` - wraps the left and right side of each column with the `col_separator` value. **This value includes no whitespace.**

# Props
Big props go to [Dr. Drang](http://www.leancrew.com/all-this/) for his post, [Updated Text Tables bundle](http://www.leancrew.com/all-this/2008/09/updated-text-tables-bundle-for-textmate/).

# License
MIT - [http://jbrooksuk.mit-license.org](http://jbrooksuk.mit-license.org)