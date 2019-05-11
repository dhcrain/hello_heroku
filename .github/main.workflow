workflow "New Python Syntax Checkerworkflow" {
  resolves = ["Python Syntax Checker"]
  on = "push"
}

action "Python Syntax Checker" {
  uses = "cclauss/Find-Python-syntax-errors-action@0.1.2"
}
