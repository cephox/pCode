# pCode
a useless codegolfing language

## Execution
```bash
./pcode.py <file>
```

## Reference
### Numbers
Only integers are allowed
### Strings/Literals
Strings are encapsulated by `"`

Spaces have to be passed as string, newlines and tabs do not
```
.

```
Prints a new line, but
```
."hello"

.0
```
prints `hello0`
### Variables
`[a-z]` are user-defined variabled
### Commands
| Command | Arguments | Definition | Example |
|:-------:|:---------:|:----------:|:-------:|
| `.`     | 1         | Prints the content/result of the first argument | `.a` 
| `,`     | 0         | Returns the first line from stdin | `.,`
| ` `<br/>`<space>`|  | Used to split arguments | `+5 5` → 10
| `=`     | 2         | Stores the result of the second argument in the first argument (has to be a variable) | `=a,`
| `+`     | 2         | Returns the sum of both arguments | `=a+b5.a`
| `-`     | 2         | Returns the difference between both arguments | `=a-b5.a`
| `*`     | 2         | Returns the multiplication of both arguments | `=a*b5.a`
| `/`     | 2         | Returns the division of both arguments | `=a/b5.a`
| `%`     | 2         | Returns the rest of the division of both arguments | `=a%b5.a`


### Comments
Comments are encapsulated by `…`
```
…Simple echo program….,
```